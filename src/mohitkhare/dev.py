"""Developer productivity utilities.

    >>> from mohitkhare import timer, retry, flatten, chunk_list, dedupe
    >>> flatten([[1, 2], [3, [4, 5]]])
    [1, 2, 3, 4, 5]

More tools: https://mohitkhare.me/blog
"""

from __future__ import annotations

import time
import functools
from typing import Any, TypeVar, Callable

T = TypeVar("T")


def timer(func: Callable) -> Callable:
    """Decorator that prints execution time.

    Examples:
        >>> @timer
        ... def slow():
        ...     import time; time.sleep(0.1)
        >>> slow()
        slow took 0.100s
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,),
) -> Callable:
    """Decorator for retrying failed function calls with exponential backoff.

    Args:
        max_attempts: Maximum number of attempts.
        delay: Initial delay between retries (seconds).
        backoff: Multiplier for delay after each retry.
        exceptions: Exception types to catch.

    Examples:
        >>> @retry(max_attempts=3, delay=0.1)
        ... def flaky_api():
        ...     import random
        ...     if random.random() < 0.5:
        ...         raise ConnectionError("timeout")
        ...     return "ok"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
            raise last_exception
        return wrapper
    return decorator


def flatten(nested: list, *, depth: int = -1) -> list:
    """Flatten nested lists.

    Args:
        nested: Nested list structure.
        depth: Max depth to flatten (-1 for unlimited).

    Returns:
        Flattened list.

    Examples:
        >>> flatten([[1, 2], [3, [4, 5]]])
        [1, 2, 3, 4, 5]
        >>> flatten([[1, [2, [3]]], 4], depth=1)
        [1, [2, [3]], 4]
    """
    result = []
    for item in nested:
        if isinstance(item, list) and depth != 0:
            result.extend(flatten(item, depth=depth - 1 if depth > 0 else -1))
        else:
            result.append(item)
    return result


def chunk_list(items: list[T], size: int) -> list[list[T]]:
    """Split a list into chunks of specified size.

    Args:
        items: Input list.
        size: Chunk size.

    Returns:
        List of chunks.

    Examples:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [items[i : i + size] for i in range(0, len(items), size)]


def dedupe(items: list[T], *, key: Callable | None = None) -> list[T]:
    """Remove duplicates while preserving order.

    Args:
        items: Input list.
        key: Optional function to compute comparison key.

    Returns:
        Deduplicated list.

    Examples:
        >>> dedupe([3, 1, 2, 1, 3])
        [3, 1, 2]
        >>> dedupe(["a", "A", "b"], key=str.lower)
        ['a', 'b']
    """
    seen = set()
    result = []
    for item in items:
        k = key(item) if key else item
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result
