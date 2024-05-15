# 自動テストの結果をHTMLファイルとして出力する

1. ソリューションディレクトリの中に以下のファイルを作成する

```xml:.runsettings
<?xml version="1.0" encoding="utf-8"?>
<RunSettings>
  <!-- Configurations that affect the Test Framework -->
  <RunConfiguration>
    <ResultsDirectory>.\tests\TestResults</ResultsDirectory>
  </RunConfiguration>
<LoggerRunSettings>
    <Loggers>
      <Logger friendlyName="trx" enabled="True">
        <Configuration>
          <LogFileName>test-results.trx</LogFileName>
        </Configuration>
      </Logger>
      <Logger friendlyName="html" enabled="True">
        <Configuration>
          <LogFileName>test-results.html</LogFileName>
        </Configuration>
      </Logger>
    </Loggers>
  </LoggerRunSettings></RunSettings>
```

2. Visual Studioで\[テスト]>\[実行設定の構成]から作成した`.runsettings`ファイルを選択する
3. テストエクスプローラーでテスト実行後、`ResultsDirectory`で指定したフォルダにテスト結果が出力される

## 参考
- [.runsettings ファイルを使用して単体テストを構成する](https://learn.microsoft.com/ja-jp/visualstudio/test/configure-unit-tests-by-using-a-dot-runsettings-file?view=vs-2022)