# VsCodeが「リモートを開いています」で固まる

## 概要
概要の通り。WSL上のプロジェクトが急に開けなくなる。発生原因は不明……

## 対処法
`~/.vscode-server`を削除する。
削除後、再度VsCodeを開こうとするとVsCodeServerが再度インストールされ、使えるようになる。
```bash
rm -rf ~/.vscode-server
```