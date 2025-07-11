"""Token counting utilities."""

from __future__ import annotations


def _count_with_tiktoken(text: str, model: str) -> int:
    """Count tokens using tiktoken if available.

    If tiktoken or the model encoding is unavailable this function raises an
    exception and callers should fall back to a simpler method.
    """
    import tiktoken  # type: ignore

    try:
        enc = tiktoken.encoding_for_model(model)
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def track_tokens(prompt: str, response: str, model: str) -> tuple[int, int]:
    """Return the number of input and output tokens for the given model."""

    try:
        input_tokens = _count_with_tiktoken(prompt, model)
        output_tokens = _count_with_tiktoken(response, model)
    except Exception:
        # Fallback to whitespace tokenisation when tiktoken isn't available
        input_tokens = len(prompt.split())
        output_tokens = len(response.split())
    return input_tokens, output_tokens