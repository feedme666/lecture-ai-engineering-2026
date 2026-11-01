from types import SimpleNamespace

from app import ask


def test_main_displays_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        text="回答",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
    )
    monkeypatch.setattr(ask, "_generate_response", lambda question: response)
    monkeypatch.setattr("sys.argv", ["app.ask", "質問"])

    ask.main()

    output = capsys.readouterr().out
    assert "回答" in output
    assert "input_tokens=12" in output
    assert "output_tokens=34" in output
    assert output.index("回答") < output.index("input_tokens=12")


def test_interactive_mode_keeps_follow_up_questions_in_same_chat(
    monkeypatch, capsys
):
    chat = SimpleNamespace(messages=[])

    def send_message(question):
        chat.messages.append(question)
        return SimpleNamespace(
            text=f"{question}への回答",
            usage_metadata=None,
        )

    chat.send_message = send_message
    chats = SimpleNamespace(create=lambda model: chat)
    monkeypatch.setattr(
        ask.genai,
        "Client",
        lambda api_key: SimpleNamespace(chats=chats),
    )
    questions = iter(["続きの質問", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(questions))
    monkeypatch.setattr("sys.argv", ["app.ask", "--interactive", "最初の質問"])

    ask.main()

    assert chat.messages == ["最初の質問", "続きの質問"]
    output = capsys.readouterr().out
    assert "最初の質問への回答" in output
    assert "続きの質問への回答" in output