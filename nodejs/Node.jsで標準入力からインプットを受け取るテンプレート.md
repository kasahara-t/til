コンソールで直接入力する場合、`Ctrl + D`で入力を終了することができる。

```js
process.stdin.setEncoding("utf8");
const getLines = async () => {
	const buffers = [];
	for await (const chunk of process.stdin) {
		buffers.push(chunk);
	}
	return Buffer.concat(buffers).toString().trim().split('\n');
}

getLines().then(lines => {
	// ここに処理を書く
});
```