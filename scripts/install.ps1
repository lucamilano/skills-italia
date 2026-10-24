param(
    [ValidateSet('both','codex','claude')][string]$Agent = 'both',
    [ValidateSet('project','user')][string]$Scope = 'project',
    [string]$ProjectPath = (Get-Location).Path,
    [string[]]$Skill,
    [switch]$All,
    [switch]$Force,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
if ($All -and $Skill) { throw 'Use -All or -Skill, not both' }
$installerArgs = @((Join-Path $PSScriptRoot 'install.py'), '--agent', $Agent, '--scope', $Scope, '--project-path', $ProjectPath)
foreach ($name in $Skill) { $installerArgs += @('--skill', $name) }
if ($All) { $installerArgs += '--all' }
if ($Force) { $installerArgs += '--force' }
if ($DryRun) { $installerArgs += '--dry-run' }
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python @installerArgs
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 @installerArgs
} else {
    throw 'Python 3.10+ is required. Install it before running this local installer.'
}
exit $LASTEXITCODE
