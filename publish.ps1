# PDFzen Chrome extension -> one-click GitHub publish
# Prereq: install GitHub CLI (winget install GitHub.cli) and run `gh auth login` once.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  Write-Error "gh not found. Install with: winget install GitHub.cli  then run: gh auth login"
}

# Package extension zip for Chrome Web Store upload (Windows has no `zip`, so this is skipped there).
if (Get-Command zip -ErrorAction SilentlyContinue) {
  Push-Location extension
  zip -r ..\pdfzen-extension.zip . -x "*.py"
  Pop-Location
  Write-Host "pdfzen-extension.zip created (upload this to Chrome Web Store)"
}

# Init repo and push to GitHub
git init -q
git add -A
git commit -q -m "PDFzen Chrome extension v1.0.0 - private, open-source, no permissions"
$repo = "pdfzen-extension"
gh repo create $repo --public `
  --description "Open-source Chrome extension for PDFzen - free, private, 100 percent in-browser PDF and image tools. No upload, no sign-up." `
  --source . --remote origin --push

$user = gh api user --jq .login
Start-Process "https://github.com/$user/$repo"
Write-Host "Repository created and opened: https://github.com/$user/$repo"
