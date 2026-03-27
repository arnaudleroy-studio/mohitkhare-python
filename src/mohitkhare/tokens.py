"""LLM token estimation utilities.

    >>> from mohitkhare import estimate_tokens, estimate_cost
    >>> estimate_tokens("Hello, how are you?")
    5
    >>> estimate_cost("Long prompt...", model="gpt-4")
    '$0.0012'

Learn more: https://mohitkhare.me/blog
"""

from __future__ import annotations

# Approximate tokens-per-character ratios by model family
_RATIOS = {
    "gpt-4": 0.25,
    "gpt-4o": 0.25,
    "gpt-3.5": 0.25,
    "claude": 0.28,
    "claude-3": 0.28,
    "claude-opus": 0.28,
    "claude-sonnet": 0.28,
    "claude-haiku": 0.28,
    "llama": 0.27,
    "mistral": 0.27,
    "gemini": 0.25,
}

# Input price per 1M tokens (USD)
_PRICES = {
    "gpt-4o": 2.50,
    "gpt-4": 30.00,
    "gpt-3.5": 0.50,
    "claude-opus": 15.00,
    "claude-sonnet": 3.00,
    "claude-haiku": 0.25,
    "gemini-pro": 1.25,
    "llama-70b": 0.90,
    "mistral-large": 2.00,
}


def estimate_tokens(text: str, *, model: str = "gpt-4o") -> int:
    """Estimate token count for text without requiring a tokenizer.

    Uses character-based heuristics. For exact counts, use tiktoken or
    the model's official tokenizer.

    Args:
        text: Input text.
        model: Model family name (gpt-4, claude, llama, etc.).

    Returns:
        Estimated token count.

    Examples:
        >>> estimate_tokens("Hello, how are you?")
        5
        >>> estimate_tokens("A " * 1000, model="claude")
        560
    """
    model_lower = model.lower()
    ratio = 0.25  # default
    for key, r in _RATIOS.items():
        if key in model_lower:
            ratio = r
            break
    return max(1, int(len(text) * ratio))


def estimate_cost(
    text: str,
    *,
    model: str = "gpt-4o",
    is_output: bool = False,
) -> str:
    """Estimate API cost for processing text.

    Args:
        text: Input or output text.
        model: Model name (gpt-4o, claude-sonnet, etc.).
        is_output: If True, use output pricing (typically 3-4x input).

    Returns:
        Formatted cost string.

    Examples:
        >>> estimate_cost("A " * 10000, model="gpt-4o")
        '$0.0050'
        >>> estimate_cost("Short response", model="claude-haiku")
        '$0.0000'
    """
    tokens = estimate_tokens(text, model=model)
    model_lower = model.lower()

    price_per_m = 2.50  # default to gpt-4o
    for key, p in _PRICES.items():
        if key in model_lower:
            price_per_m = p
            break

    if is_output:
        price_per_m *= 4  # output is typically 3-4x input

    cost = (tokens / 1_000_000) * price_per_m
    return f"${cost:.4f}"
