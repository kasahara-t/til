# Github Actionsのフロー内でgit pushをするときに、403エラーで落ちる

## 対処法
リポジトリの設定で、［Settings］>［Actions］> ［General］ に遷移すると一般設定があるので、ここで一番上を選んで読み書きの権限をActionsに付与する。

## TODO
git pushを使うよりも、成果物のアップロードを行う方がセキュリティ的にも良さそう。このリポジトリもいつか変更する。
