コンソールで直接入力する場合、`Ctrl + D`で入力を終了することができる。

```js
process.stdin.setEncoding("utf8");
const getLines = async () => {
	const lines = [];
	for await (const line of process.stdin) {
		lines.push(line);
	}
	return lines
}


getLines().then(lines => {
	// ここに処理を書く
});
```