API Reference
=============

This page documents all public functions in the ``mohitkhare`` package. For tutorials
and usage patterns, visit the `blog <https://mohitkhare.me/blog>`_.

Text Utilities
--------------

Functions from ``mohitkhare.text`` for common text processing tasks.

``slugify(text, *, separator="-", max_length=200)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Convert text to a URL-safe slug. Handles unicode normalization, special characters, and
multiple separators.

**Parameters:**

- ``text`` (str) -- Input text.
- ``separator`` (str) -- Word separator (default ``"-"``).
- ``max_length`` (int) -- Maximum slug length.

**Returns:** Lowercase slug string.

.. code-block:: python

   from mohitkhare import slugify
   slugify("Hello World!")  # 'hello-world'
   slugify("Cafe & Restaurant -- Paris")  # 'cafe-restaurant-paris'

``truncate(text, length, *, suffix="...")``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Truncate text to a maximum length with a suffix.

**Parameters:**

- ``text`` (str) -- Input text.
- ``length`` (int) -- Max total length including suffix.
- ``suffix`` (str) -- Truncation indicator (default ``"..."``).

.. code-block:: python

   from mohitkhare import truncate
   truncate("Hello World", 8)  # 'Hell...'
   truncate("Short", 10)  # 'Short'

``chunk_text(text, max_chars=4000, *, overlap=200)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Split text into overlapping chunks for LLM processing. Splits on sentence boundaries
when possible.

**Parameters:**

- ``text`` (str) -- Input text.
- ``max_chars`` (int) -- Maximum characters per chunk (default 4000).
- ``overlap`` (int) -- Character overlap between consecutive chunks.

**Returns:** List of text chunks.

.. code-block:: python

   from mohitkhare import chunk_text
   chunks = chunk_text(long_document, max_chars=2000, overlap=100)

``word_count(text)``
^^^^^^^^^^^^^^^^^^^^

Count words in text. Returns integer.

``reading_time(text, *, wpm=238)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estimate reading time for text. Uses 238 WPM (average adult reading speed) by default.

**Returns:** Human-readable string like ``'3 min read'``.

.. code-block:: python

   from mohitkhare import reading_time
   reading_time("word " * 500)  # '2 min read'

Token Estimation
----------------

Functions from ``mohitkhare.tokens`` for estimating LLM token counts and API costs without
requiring a tokenizer library.

``estimate_tokens(text, *, model="gpt-4o")``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estimate token count using character-based heuristics. Supports GPT-4, Claude, LLaMA,
Mistral, and Gemini model families.

**Parameters:**

- ``text`` (str) -- Input text.
- ``model`` (str) -- Model family name (``'gpt-4'``, ``'claude'``, ``'llama'``, etc.).

**Returns:** Estimated token count (int).

.. code-block:: python

   from mohitkhare import estimate_tokens
   estimate_tokens("Hello, how are you?")  # 5
   estimate_tokens("A " * 1000, model="claude")  # 560

``estimate_cost(text, *, model="gpt-4o", is_output=False)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Estimate API cost for processing text. Includes pricing for major model families.

**Parameters:**

- ``text`` (str) -- Input or output text.
- ``model`` (str) -- Model name (``'gpt-4o'``, ``'claude-sonnet'``, ``'claude-haiku'``, etc.).
- ``is_output`` (bool) -- If True, use output pricing (typically 3-4x input).

**Returns:** Formatted cost string (e.g., ``'$0.0050'``).

.. code-block:: python

   from mohitkhare import estimate_cost
   estimate_cost("A " * 10000, model="gpt-4o")  # '$0.0050'
   estimate_cost("Short response", model="claude-haiku")  # '$0.0000'

Developer Utilities
-------------------

Functions from ``mohitkhare.dev`` for common development patterns.

``timer(func)``
^^^^^^^^^^^^^^^

Decorator that prints execution time of a function.

.. code-block:: python

   from mohitkhare import timer

   @timer
   def process_data():
       # ... heavy computation
       pass

   process_data()  # Prints: process_data took 1.234s

``retry(max_attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,))``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decorator for retrying failed function calls with exponential backoff.

**Parameters:**

- ``max_attempts`` (int) -- Maximum number of attempts.
- ``delay`` (float) -- Initial delay between retries (seconds).
- ``backoff`` (float) -- Multiplier for delay after each retry.
- ``exceptions`` (tuple) -- Exception types to catch and retry.

.. code-block:: python

   from mohitkhare import retry

   @retry(max_attempts=3, delay=0.5)
   def call_api():
       # Retries up to 3 times with 0.5s, 1s, 2s delays
       return requests.get("https://api.example.com/data")

``flatten(nested, *, depth=-1)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Flatten nested lists. Supports depth limiting.

.. code-block:: python

   from mohitkhare import flatten
   flatten([[1, 2], [3, [4, 5]]])  # [1, 2, 3, 4, 5]
   flatten([[1, [2, [3]]], 4], depth=1)  # [1, [2, [3]], 4]

``chunk_list(items, size)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Split a list into chunks of specified size.

.. code-block:: python

   from mohitkhare import chunk_list
   chunk_list([1, 2, 3, 4, 5], 2)  # [[1, 2], [3, 4], [5]]

``dedupe(items, *, key=None)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove duplicates while preserving order. Supports custom key functions.

.. code-block:: python

   from mohitkhare import dedupe
   dedupe([3, 1, 2, 1, 3])  # [3, 1, 2]
   dedupe(["a", "A", "b"], key=str.lower)  # ['a', 'b']

See Also
--------

- `Mohit Khare <https://mohitkhare.me>`_ -- Personal website
- `Blog <https://mohitkhare.me/blog>`_ -- Dev tips and tutorials
