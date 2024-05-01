# 以前のバージョンのIMEを使うと日本語入力で落ちる

## 概要
Windows11のターミナルで日本語入力をしたところ、同じ文字が大量に生成されたり、ターミナルがクラッシュすることが多発したため調べた。  
原因はWindowsの設定で「以前のバージョンのMicrosoft IMEを使う」を有効にしていたため。もともと全角英数になるのを防ぐためにこの設定を有効にしたのだが、全角英数を許容するか、そもそも日本語でなく英語を日常的に使用するか、どちらかに割り切る必要がありそう。

## 参考

- [# Terminal hangs or prints repetitive characters when using Japanese IME #14349](https://github.com/microsoft/terminal/issues/14349)