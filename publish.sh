#!/usr/bin/env bash
# PDFzen 扩展源码 -> GitHub 一键发布
# 前置：brew install gh && gh auth login
set -e
cd "$(dirname "$0")"

if ! command -v gh >/dev/null 2>&1; then
  echo "未找到 gh。请先安装：brew install gh  然后运行 gh auth login" >&2
  exit 1
fi

# 打包扩展 zip（供 Chrome Web Store 上传；需一次性 $5 开发者费）
if command -v zip >/dev/null 2>&1; then
  (cd extension && zip -r ../pdfzen-extension.zip . -x '*.py')
  echo "已生成 pdfzen-extension.zip（可上传到 Chrome Web Store）"
fi

git init -q
git add -A
git commit -q -m "PDFzen Chrome extension v1.0.0 — private, open-source, no permissions"
gh repo create pdfzen --public \
  --description "Open-source Chrome extension for PDFzen — free, private, 100% in-browser PDF & image tools. No upload, no sign-up." \
  --source . --remote origin --push

USER=$(gh api user --jq .login)
open "https://github.com/$USER/pdfzen"
echo "仓库已创建并打开：https://github.com/$USER/pdfzen"
