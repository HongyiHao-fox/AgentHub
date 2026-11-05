import os
from typing import Dict


def get_chat_response(message: str, model: str | None = None) -> Dict[str, str]:
    """Return a chat response from OpenAI when configured, otherwise use a safe fallback."""
    if not message:
        message = "你好"

    api_key = os.getenv("OPENAI_API_KEY")
    selected_model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        return {"response": f"[mock] 你说了：{message}"}

    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        return {"response": f"[mock] 你说了：{message}"}

    try:
        client = OpenAI(api_key=api_key, timeout=30.0)
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": message}],
        )
        content = response.choices[0].message.content
        return {"response": content or f"[mock] 你说了：{message}"}
    except Exception as exc:  # pragma: no cover - network/API issues
        return {"response": f"[mock] 你说了：{message}，当前无法访问 OpenAI：{exc}"}
