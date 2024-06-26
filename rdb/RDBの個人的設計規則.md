# RDBの個人的設計規則

## テーブル名の接頭辞について

マスタテーブルであれば`m_`や`mst_`をつける、トランザクションテーブルであれば`t_`や`trn_`をつけるという命名規則をよく見かけるが、こういった命名規則を英語のドキュメントではあまり見かけないため、利用しない。
（テーブル設計書などを書かせたときのぱっと見の分かりやすさ優先なのだろうか？テーブル設計書をExcelで書かせるのはやめてくれ）


## 主キーにUUIDは使用しない

セキュリティや衝突可能性を考え、主キーは基本的にUUIDで定義したいところだが、**参照の局所性**を重視するために主キーは連番で定義する。  
セキュリティ的な観点でUUIDを使用する場合は、`public_id`等のカラムを容易し、そこに格納する。  
（その列にはインデックスを張って検索を高速化しておく）

### 参考
[データベースでユニークキーにUUIDを使うメリットは何ですか？](https://jp.quora.com/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%81%A7%E3%83%A6%E3%83%8B%E3%83%BC%E3%82%AF%E3%82%AD%E3%83%BC%E3%81%ABUUID%E3%82%92%E4%BD%BF%E3%81%86%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88%E3%81%AF%E4%BD%95)


## `created_at`は基本的に用意するが、`updated_at`は必要な場合にしか用意しない

主キーにUUIDを使うことにも関係してくるが、UUIDv4を使用すると生成順のソートが難しくなるため、ソート順を担保するためにも`created_at`は必ず用意しておく。実際、作成順にソートするという要件は体感多い。  
ここで大事なのは、プログラムからはこのカラムを基本的に更新しないということ。  
しかし、`updated_at`は同じ尺度で考えてはいけないと思っている。監査ログとして使いたいなら情報が少なすぎるので別にテーブルなりを用意する必要があると思うし、用意するとしても`created_at`同様にDBの責務として更新するべきなので、バッチが更新したのかユーザーが更新したのかわからなくなるから。  
要件として最後に更新された日時（またはそれに似た情報）として持つ必要があるのであれば、汎用的なものではなく、明確な命名と意識をもって用意するようにする。
