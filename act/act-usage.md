# actを使ってGithub Actionsをローカル環境で検証する

## 前提条件
- docker

## インストール
### asdfでのインストール
```bash
$ asdf plugin add act
$ asdf plugin list all act
$ asdf install act 0.2.61
$ asdf global act 0.2.61
```

## 使用方法
- `act push`: pushしたときの動作の検証

## 注意事項
actのランナーがnode:buster-slimで、Pythonのインストール部分で落ちていた。  
ホームディレクトリに`.actrc`を作成して、使用するコンテナを指定する。
```
-P ubuntu-latest=catthehacker/ubuntu:act-latest

```

## 参考
* [act - User Guide](https://nektosact.com/)
* [act/nektosを使ってローカル環境でgithub actions走らせてコケた時の話](https://qiita.com/sokorahen-szk/items/2c2812855b05a61ff173)