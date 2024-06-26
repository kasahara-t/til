# Docker Specificationに準拠したDocker Composeの設定記法について

## 概要

Docker Composeを利用するために記述している設定ファイルについて、Docker Specificationに準拠したファイルを書くための規則。
一部Docker Specificationで明記されているわけではないが、作成される設定ファイルのフォーマットを統一させるための記述方法や命名規則も残しておく。

## ファイル名は`compose.yaml`にする

Docker Specificationで推奨されているファイル名のためこちらを採用。

## `compose.yaml`にはバージョンは記載しない

Docker SpecificationではComposeファイルのスキームを指定するためにversion要素を使用すべきではないとしているため、混乱を避けるために記載しない。

## 環境変数の定義方法は辞書形式で記述する

エディターのシンタックスハイライトを効かせるためにも配列形式ではなく辞書形式で記述する。真偽値や数値など、yamlの解析的に文字列以外の型として認識されてしまう値に注意。

## 機密情報はSecrets経由で渡す

機密情報の流出をできるだけ防ぐために、イメージに含めたり環境変数などで定義しないようにする。その代わりSecretsを使用して、コンテナの実行時に渡すようにすることで安全性を高めておく。  
この際、VolumeではなくSecretsを明示的に使用することで、その役割を明確にしておく。

## 変更可能性がある設定ファイルはイメージやボリュームではなくConfigs経由で渡す

アプリケーションの実行に直接的には関わらず、かつ変更の可能性がある設定ファイル（例えばNginxやMySQLの設定ファイルなど）はイメージに含めずにConfigsを使って渡すようにする。こうすることで、不必要なコンテナのビルドを防ぐことができる。  
Secretsと同じで、VolumeではなくConfigsを明示的に使用することで、その役割を明確にする。

## ネットワークの命名規則は`～～～-tier`

Docker Specificationの例を踏襲。もともとは`～～～-network`という命名規則を使用していたが、層のようにカプセル化されている印象が腑に落ちたのでこちらを使用。

## ボリュームの命名規則は`～～～-data`

Docker Specificationの例を踏襲。もともとは`～～～-store`という命名規則を使用していたが、ほかに合わせて例を踏襲することにした。

## 命名は基本的にケバブケース、SecretsやConfigsの値はスネークケース

こちらが明示的に命名するものは基本的にケバブケースを使用する。ただし、Secretsなどの最終的にファイル名として使用されるようなものはスネークケースで記述する。

## ビルドプロセスにのみ影響を与える設定は環境変数ではなくARGを使用する

これはDocker Composeの設定というよりかはDockerfileの設定だが、ビルドプロセスのみに影響を与える値が環境変数として残っていた場合、不必要な情報がが部に流れてしまうためARGを使用するようにする。

## 参考

- [雰囲気でDocker Composeを触っている状態から脱するために調べたこと（2023）](https://synamon.hatenablog.com/entry/2023/03/17/125933)

- [Compose Specification（仕様）](https://docs.docker.jp/compose/compose-file/index.html)