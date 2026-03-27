"""Text processing utilities for developers.

    >>> from mohitkhare import slugify, truncate, reading_time
    >>> slugify("My Blog Post Title!")
    'my-blog-post-title'
    >>> truncate("Long text here...", 10)
    'Long te...'
    >>> reading_time("A " * 500)
    '2 min read'

More at https://mohitkhare.me/blog
"""

from __future__ import annotations

import re
import unicodedata


def slugify(text: str, *, separator: str = "-", max_length: int = 200) -> str:
    """Convert text to a URL-safe slug.

    Args:
        text: Input text.
        separator: Word separator (default '-').
        max_length: Max slug length.

    Returns:
        Lowercase slug string.

    Examples:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("Cafe & Restaurant -- Paris")
        'cafe-restaurant-paris'
        >>> slugify("mohitkhare.me Blog Post #42")
        'mohitkhare-me-blog-post-42'
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", separator, text)
    text = text.strip(separator)
    return text[:max_length]


def truncate(text: str, length: int, *, suffix: str = "...") -> str:
    """Truncate text to a maximum length with suffix.

    Args:
        text: Input text.
        length: Max total length including suffix.
        suffix: Truncation indicator.

    Returns:
        Truncated string.

    Examples:
        >>> truncate("Hello World", 8)
        'Hell...'
        >>> truncate("Short", 10)
        'Short'
    """
    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix


def chunk_text(text: str, max_chars: int = 4000, *, overlap: int = 200) -> list[str]:
    """Split text into overlapping chunks for LLM processing.

    Splits on sentence boundaries when possible.

    Args:
        text: Input text.
        max_chars: Maximum characters per chunk.
        overlap: Character overlap between chunks.

    Returns:
        List of text chunks.

    Examples:
        >>> chunks = chunk_text("Long document...", max_chars=1000)
        >>> len(chunks)
        3
    """
    if len(text) <= max_chars:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        if end < len(text):
            # Try to break at sentence boundary
            for sep in [". ", "! ", "? ", "\n\n", "\n", " "]:
                last = text.rfind(sep, start + max_chars // 2, end)
                if last > start:
                    end = last + len(sep)
                    break
        chunks.append(text[start:end].strip())
        start = end - overlap
    return chunks


def word_count(text: str) -> int:
    """Count words in text.

    Args:
        text: Input text.

    Returns:
        Number of words.
    """
    return len(text.split())


def reading_time(text: str, *, wpm: int = 238) -> str:
    """Estimate reading time for text.

    Args:
        text: Input text.
        wpm: Words per minute (default 238, average adult reading speed).

    Returns:
        Human-readable string like '3 min read'.

    Examples:
        >>> reading_time("word " * 500)
        '2 min read'
    """
    words = word_count(text)
    minutes = max(1, round(words / wpm))
    return f"{minutes} min read"
