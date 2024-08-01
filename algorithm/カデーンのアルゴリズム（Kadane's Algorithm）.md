## 概要

連続部分配列の最大輪を効率的に求めるためのアルゴリズム。  
動的計画法の一種であり、O(n)の時間複雑度で解を求めることができる。

具体的には、次のように進行する：

1. 配列の最初の要素を maxSum と currentSum に設定する。
1. 配列の2番目の要素から順に、現在の要素と現在の要素を加えた和のうち、大きい方を currentSum に設定する。
1. これまでの最大の部分配列の和 maxSum を更新する。

## 初期アプローチ

### 問題：連続する部分配列の最大和

与えられた整数配列 numbers の連続する部分配列の中で、最大の和を求める関数を実装してください。

### 入力

整数の配列 numbers（1 ≤ |numbers| ≤ 1000, -10000 ≤ numbers[i] ≤ 10000）

### 出力

配列 numbers の連続する部分配列の中で最大の和を返す整数

## 初期解法

逐次探索で書くと以下のようなコードになり、時間複雑度はO(n^3)となってしまう。

```js
// 仮に定数とする
const numbers = [1, -3, 2, 1, -1, 3, -2];
let maxSum = Number.MIN_VALUE;

for (let i = 0; i < numbers.length; i++) {
	for (let j = i + 1; j <= numbers.length; j++) {
		const tmpNumbers = numbers.slice(i, j);
		let tmpSum = 0;
		for (let k = 0; k < tmpNumbers.length; k++) {
			tmpSum += tmpNumbers[k];
		}
		maxSum = Math.max(maxSum, tmpSum);
	}
}

console.log(maxSum);
```

## 改良解法

カデーンのアルゴリズムを使用すると、以下のようなコードになり、時間複雑度はO(n)となる。  
つまり、配列内の一度の探索だけで解を求めることができる。

```js
// 仮に定数とする
const numbers = [1, -3, 2, 1, -1, 3, -2];

let maxSum = numbers[0];
let currentSum = numbers[0];

for (let i = 1; i < numbers.length; i++) {
	currentSum = Math.max(numbers[i], currentSum + numbers[i]);
	maxSum = Math.max(maxSum, currentSum);
}

console.log(maxSum);
```