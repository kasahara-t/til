コンソールで直接入力する場合、`Ctrl + D`で入力を終了することができる。

```js
const getLines = async () => {
	const buffers = [];
	for await (const chunk of process.stdin) buffers.push(chunk);
	return Buffer.concat(buffers).toString().trim().split('\n');
};

getLines().then(lines => {
	// ここに処理を書く
});
```

## 参考

- [Node.jsでの標準入力の書き方をまとめてみた](https://qiita.com/saba_can00/items/02ff28a16a0d312a5259)