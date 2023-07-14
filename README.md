# line-lambda

## これはなに

LINE Messaging API での Webhook での実行用 AWS Lambda のコード群。

## 使い方

- AWS コンソールからLambdaを作成する
- `line-lambda/{Lambda名}/lambda_environment.md` 内に記載している環境変数をLambdaに登録する
- 以下を実行してコードとパッケージをZIPファイルに固める

```bash
$ ./zip_files.sh {Lambda名(ディレクトリ名)}
```

- 作成されたZIPファイルをLambdaにアップロードする
