# 本机环境全量扫描：环境变量、已装软件、服务、监听端口、PATH 中的运行时
# 一次调用完成；默认缓存 24h（-Refresh 重扫）；-Full 输出完整软件清单；敏感值不打印。
param([switch]$Full, [switch]$Refresh)

$ErrorActionPreference = 'SilentlyContinue'
$cacheDir = Join-Path $env:USERPROFILE '.dsh\cache'
$cacheFile = Join-Path $cacheDir 'env-probe.txt'
$cacheTtl = 24 * 3600

if (-not $Full -and -not $Refresh -and (Test-Path -LiteralPath $cacheFile)) {
    $age = (Get-Date) - (Get-Item -LiteralPath $cacheFile).LastWriteTime
    if ($age.TotalSeconds -lt $cacheTtl) {
        Write-Output '（缓存结果；-Refresh 重新扫描）'
        Get-Content -LiteralPath $cacheFile -Encoding utf8
        exit 0
    }
}

$lines = New-Object System.Collections.Generic.List[string]
function Add-Line([string]$text) { $script:lines.Add($text) }

Add-Line '## 环境摘要'

# 1) 环境变量：名称全扫；白名单显示值；敏感值不打印
$envVars = Get-ChildItem Env: | Sort-Object Name
Add-Line ('环境变量：{0} 个' -f $envVars.Count)
$showValues = 'JAVA_HOME', 'GOPATH', 'GOROOT', 'PYTHONHOME', 'NODE_PATH', 'DOTNET_ROOT', 'MYSQL_HOME', 'PGDATA'
foreach ($v in $envVars) {
    if ($showValues -contains $v.Name) { Add-Line ('  {0}={1}' -f $v.Name, $v.Value) }
}
$sensitive = $envVars | Where-Object { $_.Name -match 'KEY|TOKEN|SECRET|PASS|PWD|AUTH|CRED' }
if ($sensitive) {
    Add-Line ('  敏感变量（仅名称）：' + (($sensitive.Name | Sort-Object) -join ', '))
}

# 2) PATH 目录：只列开发相关
$pathDirs = @($env:Path -split ';' | Where-Object { $_ -and (Test-Path -LiteralPath $_) })
$devDirWords = 'Python|nodejs|npm|Java|MySQL|Redis|Git|mingw|VS Code|PyCharm'
$devDirs = @($pathDirs | Where-Object { $_ -match $devDirWords })
Add-Line ('PATH 目录：{0} 个（开发相关 {1} 个）' -f $pathDirs.Count, $devDirs.Count)
$devDirs | Select-Object -First 10 | ForEach-Object { Add-Line ('  ' + $_) }

# 3) 已安装程序：全扫注册表，按类别归并输出
$keys = @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
)
$rawApps = Get-ItemProperty -Path $keys | Where-Object { $_.DisplayName }
$apps = $rawApps | Select-Object -Property DisplayName, DisplayVersion -Unique | Sort-Object DisplayName
Add-Line ('已安装程序：{0} 个（按类别摘要）' -f ($apps | Measure-Object).Count)

$categories = [ordered]@{
    'Node.js'   = '^(Node\.js|Nodejs)'
    'Python'    = '^Python (3\.|2\.|Launcher)'
    'Java/JDK'  = '^(Java\(TM\) SE|Java SE|JDK)'
    'MySQL'     = '^MySQL Server'
    'Redis'     = '^Redis( |$)'
    'PostgreSQL'= 'PostgreSQL'
    'MongoDB'   = 'MongoDB'
    'Docker'    = '^Docker'
    'Git'       = '^Git( |$)'
    'VS Code'   = '^Microsoft Visual Studio Code'
    'PyCharm'   = '^PyCharm'
    '.NET'      = '^(\.NET|Microsoft \.NET)'
    'MinGW/C++' = '^(MinGW|MSYS2)'
    'php'       = '^PHP'
    'Go'        = '^Go( |$)'
    'Rust'      = '^Rust'
}
$matchedNames = @{}
foreach ($cat in $categories.Keys) {
    $hit = $apps | Where-Object { $_.DisplayName -match $categories[$cat] } | Select-Object -First 1
    if ($hit) {
        Add-Line ('  {0}：{1} {2}' -f $cat, $hit.DisplayName, $hit.DisplayVersion)
        $matchedNames[$hit.DisplayName] = $true
    }
}
$unmatched = $apps | Where-Object { -not $matchedNames.ContainsKey($_.DisplayName) -and $_.DisplayName -match 'node|python|java|mysql|redis|mongo|postgres|docker|git|vscode|visual studio|code|jetbrains|pycharm|php|golang|rust|dotnet|\.net|nginx|apache|sql server|composer|maven|gradle|cmake' }
if ($unmatched) {
    Add-Line ('  其他开发相关：{0}' -f (($unmatched | Select-Object -First 6 | ForEach-Object { $_.DisplayName }) -join ' / '))
}
if ($Full) {
    Add-Line '--- 完整已安装列表 ---'
    $apps | ForEach-Object { Add-Line ('  {0} {1}' -f $_.DisplayName, $_.DisplayVersion) }
}

# 4) 相关服务
$svc = Get-Service | Where-Object { $_.Name -match 'mysql|maria|postgres|mongo|redis|mssql|sql|docker|nginx|apache|iis' }
if ($svc) {
    Add-Line ('相关服务：{0} 个' -f ($svc | Measure-Object).Count)
    $svc | Sort-Object Name | ForEach-Object { Add-Line ('  {0} [{1}]' -f $_.Name, $_.Status) }
} else {
    Add-Line '相关服务：未发现'
}

# 5) 常见监听端口
$commonPorts = 80, 443, 3000, 3306, 5432, 6379, 27017, 8000, 8080
$listen = Get-NetTCPConnection -State Listen | Where-Object { $commonPorts -contains $_.LocalPort } |
    Select-Object -Property LocalPort -Unique | Sort-Object LocalPort
if ($listen) {
    Add-Line ('常见监听端口：' + (($listen | ForEach-Object { $_.LocalPort }) -join ', '))
} else {
    Add-Line '常见监听端口：无'
}

# 6) PATH 中发现的运行时（按家族归并，不逐个列出工具变体）
$families = [ordered]@{
    'Node'   = 'node'
    'npm'    = 'npm'
    'Python' = 'python'
    'pip'    = 'pip'
    'Git'    = 'git'
    'Java'   = 'java'
    'MySQL'  = 'mysql'
    'Redis'  = 'redis'
    'VS Code'= 'code'
    'Docker' = 'docker'
}
$foundFamilies = @{}
foreach ($dir in $devDirs) {
    Get-ChildItem -LiteralPath $dir -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.exe', '.cmd', '.bat' } |
        ForEach-Object {
            $n = $_.BaseName.ToLowerInvariant()
            foreach ($f in $families.Keys) {
                if ($n -eq $families[$f] -or $n.StartsWith($families[$f])) { $foundFamilies[$f] = $true }
            }
        }
}
if ($foundFamilies.Count -gt 0) {
    Add-Line ('PATH 运行时：' + (($foundFamilies.Keys | Sort-Object) -join ', '))
} else {
    Add-Line 'PATH 运行时：无'
}

Add-Line '## 说明'
Add-Line '只读扫描；未发现类别不显示。需要完整软件清单用 -Full；-Refresh 强制重扫。'

$text = ($lines -join "`n")
New-Item -ItemType Directory -Force -Path $cacheDir | Out-Null
Set-Content -LiteralPath $cacheFile -Value $text -Encoding utf8
Write-Output $text
