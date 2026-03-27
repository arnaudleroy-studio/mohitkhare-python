"""
mohitkhare - Developer utilities and AI engineering tools.

A collection of practical developer utilities for everyday coding,
AI/LLM integration, and dev productivity.

    >>> from mohitkhare import slugify, truncate, chunk_text
    >>> slugify("Hello World!")
    'hello-world'

Blog: https://mohitkhare.me/blog
"""

__version__ = "0.1.0"
__author__ = "Mohit Khare"
__url__ = "https://mohitkhare.me"

from mohitkhare.text import slugify, truncate, chunk_text, word_count, reading_time
from mohitkhare.tokens import estimate_tokens, estimate_cost
from mohitkhare.dev import timer, retry, flatten, chunk_list, dedupe

__all__ = [
    "slugify",
    "truncate",
    "chunk_text",
    "word_count",
    "reading_time",
    "estimate_tokens",
    "estimate_cost",
    "timer",
    "retry",
    "flatten",
    "chunk_list",
    "dedupe",
]
