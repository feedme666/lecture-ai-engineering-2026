"""第1回: 素のLLMに質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする
    uv run python -m app.ask --interactive  # 会話履歴を保って続けて質問する

単発モードはツールも会話履歴も持たない「素の」呼び出しです。
対話モードではチャットセッションが会話履歴を保持します。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def _generate_response(question: str):
    client = genai.Client(api_key=get_api_key())
    return client.models.generate_content(model=MODEL, contents=question)


def ask(question: str) -> str:
    return _generate_response(question).text


def _print_response(response) -> None:
    print(response.text)
    usage = response.usage_metadata
    if usage is None:
        print("\n[usage] トークン数を取得できませんでした")
    else:
        print(
            f"\n[usage] input_tokens={usage.prompt_token_count} "
            f"output_tokens={usage.candidates_token_count}"
        )


def _interactive(question: str | None = None) -> None:
    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(model=MODEL)

    if question:
        print(f"[質問] {question}\n")
        _print_response(chat.send_message(question))

    while True:
        try:
            question = input("質問> ")
        except EOFError:
            print()
            return
        if question.strip().lower() in {"終了", "exit", "quit"}:
            return
        if not question.strip():
            continue

        print(f"\n[質問] {question}\n")
        _print_response(chat.send_message(question))


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="会話履歴を保って続けて質問する（終了: 終了 / exit / quit）",
    )
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    if args.interactive:
        try:
            _interactive(args.question)
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            raise SystemExit(1)
        return

    question = args.question or DEFAULT_QUESTION
    print(f"[質問] {question}\n")
    try:
        response = _generate_response(question)
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)
    _print_response(response)


if __name__ == "__main__":
    main()
