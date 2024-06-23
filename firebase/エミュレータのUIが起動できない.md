エミュレータを起動したとき、以下のエラーが発生した。

```
node:internal/modules/cjs/loader:1163
      throw err;
      ^

Error [ERR_REQUIRE_ESM]: require() of ES Module /home/misi/.cache/firebase/emulators/ui-v1.11.7/server/server.js not supported.
server.js is treated as an ES module file as it is a .js file whose nearest parent package.json contains "type": "module" which declares all .js files in that package scope as ES modules.
Instead rename server.js to end in .cjs, change the requiring code to use dynamic import() which is available in all CommonJS modules, or change "type": "module" to "type": "commonjs" in /home/misi/package.json to treat all .js files as CommonJS (using .mjs for all ES modules instead).

    at Function.runMain (pkg/prelude/bootstrap.js:1979:12) {
  code: 'ERR_REQUIRE_ESM'
}

Node.js v18.5.0
```

結論、firebase-toolsのバージョンを13.5.0にダウングレードすると直った。

## 参考
https://github.com/firebase/firebase-tools-ui/issues/1014