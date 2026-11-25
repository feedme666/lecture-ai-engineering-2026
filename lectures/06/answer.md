# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前："glossary_search_glossary"
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：
  - [tool call]   aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要', 'topics': ['general']})
  - [tool return] aws_aws___search_documentation -> {'content': {'result': [{'rank_order': 1, 'title': 'querying-aws-s3', 'skill_description': 'Queries S3 object metadata, …
  - [tool call]   aws_aws___search_documentation({'search_phrase': 'Using versioning in S3 buckets', 'topics': ['general']})
  - [tool return] aws_aws___search_documentation -> {'content': {'result': [{'rank_order': 1, 'title': 'What is Amazon S3?', 'context': '### S3 Versioning\n\nYou can use S3…
- 気づき・疑問：MCPサーバーの場所とプログラムの実行の場所の違いがわかりづらかったが、LLMと確認して理解ができた。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：発展
- やったこと：普段使用しているOpenCodeのmcpのサーバーについて調べた。OpenCodeのdocumentsに書いてあったcontext7と、その接続方法について調べた。
- 結果：
  - 設定を書く場所： 各設定ファイル。優先順位は以下のとおり。下にいくほど優先される。
    `~/.config/opencode/opencode.json`
    `/home/user/projects/acme/opencode.json`
    `/home/user/projects/acme/packages/web/opencode.json`
    `/etc/opencode/opencode.json`

  - コマンドで起動する書き方： "type" を "local"として、"command" に実行コマンドと引数を配列として記載する。演習では command と args が分かれていたが、OpenCodeでは一つの配列にまとめられている。
  - URL で接続する書き方： "type" を "remote" とし、"url" に接続先を記載する。
  - 有効になる範囲: プロジェクト単位で設定も可能であるし、グローバル設定も可能。
- 気づき・疑問：
  = Context7という、プログラミング関連のドキュメントを取得するためのMCPサーバーがあることを知った。
  = Context7の場合、Remoteで設定する場合は type を remote として、url に https://mcp.context7.com/mcp を指定する。Localで設定する場合は type を local として、command に ["npx", "-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"] と記載する。
  = LocalではMCPサーバーをコマンドで起動し、Remoteでは既に稼働しているMCPサーバーにURLで接続するという仕組みは、演習と共通していた。
  = Context7では、LocalでMCPサーバーを起動した場合でも、ドキュメントの取得には外部サービスとの通信が必要である。Local MCPであることと、すべての処理がローカルで完結することは異なると分かった。
