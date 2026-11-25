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

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
