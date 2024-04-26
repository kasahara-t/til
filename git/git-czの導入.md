# git-czの導入

[git-cz](https://github.com/streamich/git-cz)をインストールして、環境やエディタごとに異なっていたcommitizenの設定を統一できる

## 前提
- npmのインストール

## インストール
以下のコマンドでインストールを行う  
（commitizenが既にグローバルインストールされているとうまくいかない？asdfを使っているからかもしれないが）

```bash
$ npm install -g git-cz
```

## 設定
設定ファイルはプロジェクトごとor任意の親フォルダに配置すればいいので、以下の設定ファイルをユーザーのルートディレクトリに配置する。  
（WindowsではCドライブ直下など）  

スコープをプロジェクトごとに設定する場合は、プロジェクトにも`changelog.config.js`を作成しておくようにする。
```js:changelog.config.js
module.exports = {
	// Emojiを非表示にするか
	disableEmoji: false,

	// types一覧
	// typesが設定されているのに、listに登録されてないとgit-czの実行時にエラーを吐く
	// 入れる値は、typesのvalueプロパティで指定した値
	list: [
		'test',
		'feat',
		'fix',
		'chore',
		'docs',
		'refactor',
		'style',
		'ci',
		'perf',
		'config',
		'package',
	],

	// コミットメッセージの最大文字数
	maxMessageLength: 64,

	// コミットメッセージの最小文字数
	minMessageLength: 3,

	// 質問の種類
	questions: ['type', 'scope', 'subject', 'body', 'breaking'],

	// scopesの種類
	// 一つも指定されてない場合、scopeの質問は行われなくなる
	scopes: [],

	// typesの種類を設定する
	types: {
		chore: {
			description: 'ビルドプロセスまたは補助ツールの変更',
			emoji: '🤖',
			value: 'chore',
		},
		ci: {
			description: 'CI関連の変更',
			emoji: '🎡',
			value: 'ci',
		},
		docs: {
			description: 'ドキュメントの変更のみ',
			emoji: '✏️',
			value: 'docs',
		},
		feat: {
			description: '新機能の追加や更新',
			emoji: '🎸',
			value: 'feat',
		},
		fix: {
			description: 'バグ修正',
			emoji: '🐛',
			value: 'fix',
		},
		perf: {
			description: 'パフォーマンスを向上させるコード変更',
			emoji: '⚡️',
			value: 'perf',
		},
		refactor: {
			description: 'リファクタリング',
			emoji: '💡',
			value: 'refactor',
		},
		release: {
			description: 'リリースコミット',
			emoji: '🏹',
			value: 'release',
		},
		style: {
			description: 'マークアップ、ホワイトスペース、フォーマット、セミコロンなどの修正',
			emoji: '💄',
			value: 'style',
		},
		test: {
			description: 'テストの追加・修正',
			emoji: '💍',
			value: 'test',
		},

		// 以下、独自で追加したtypes
		config: {
			description: '設定ファイルの追加・修正',
			emoji: '⚙️',
			value: 'config',
		},
		package: {
			description: 'パッケージの追加・更新・削除',
			emoji: '📦',
			value: 'package',
		},
	},
};

```