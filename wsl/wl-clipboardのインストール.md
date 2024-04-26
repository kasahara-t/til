# wl-clipboardのインストール

wsl2でneovimを使う際、クリップボードの同期をさせようとするととても遅い。  
win32yankを以前まで使用していたが、どうやらwl-clipboardの方がより速いようなので（実際早い）、こちらを使用するようにする。

## インストール
Ubuntuの場合：
```bash
$ sudo apt update
$ sudo apt install wl-clipboard
$ . ~/.bashrc
```

## luaでの設定
neovimのinit.luaに以下を追記する
```lua
vim.opt.clipboard = 'unnamedplus'
if vim.fn.has 'wsl' == 1 then
  if vim.fn.executable 'wl-copy' == 0 then
    print "wl-clipboard not found, clipboard integration won't work"
  else
    vim.g.clipboard = {
      name = 'wl-clipboard (wsl)',
      copy = {
        ['+'] = 'wl-copy --foreground --type text/plain',
        ['*'] = 'wl-copy --foreground --primary --type text/plain',
      },
      paste = {
        ['+'] = function()
          return vim.fn.systemlist('wl-paste --no-newline|sed -r "s/\r$//"', { '' }, 1)
        end,
        ['*'] = function()
          return vim.fn.systemlist('wl-paste --primary --no-newline|sed -r "s/\r$//"', { '' }, 1)
        end,
      },
      cache_enabled = true,
    }
  end
end
```

## 参考
- [Copy into system clipboard from neovim](https://stackoverflow.com/questions/75548458/copy-into-system-clipboard-from-neovim)