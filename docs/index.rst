mohitkhare -- Developer Utilities & AI Tools
=============================================

**mohitkhare** is a collection of practical developer utilities for everyday coding,
AI/LLM integration, and dev productivity. Built by `Mohit Khare <https://mohitkhare.me>`_.

Zero dependencies. Works with Python 3.9+. Covers text processing, LLM token estimation,
and common developer patterns like retry with backoff, list deduplication, and timing.

Quick Start
-----------

.. code-block:: python

   from mohitkhare import slugify, truncate, reading_time

   # Text utilities
   slugify("My Blog Post Title!")  # 'my-blog-post-title'
   truncate("Long text here...", 10)  # 'Long te...'
   reading_time("word " * 500)  # '2 min read'

   # LLM token estimation
   from mohitkhare import estimate_tokens, estimate_cost
   estimate_tokens("Hello, how are you?", model="gpt-4o")  # 5
   estimate_cost("A " * 10000, model="claude-sonnet")  # '$0.0017'

   # Dev productivity
   from mohitkhare import retry, flatten, dedupe
   flatten([[1, 2], [3, [4, 5]]])  # [1, 2, 3, 4, 5]
   dedupe([3, 1, 2, 1, 3])  # [3, 1, 2]

Read more on the `blog <https://mohitkhare.me/blog>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   api

Links
-----

- **Website**: `mohitkhare.me <https://mohitkhare.me>`_
- **Blog**: `mohitkhare.me/blog <https://mohitkhare.me/blog>`_
- **PyPI**: `pypi.org/project/mohitkhare/ <https://pypi.org/project/mohitkhare/>`_
- **GitHub**: `github.com/arnaudleroy-studio/mohitkhare-python <https://github.com/arnaudleroy-studio/mohitkhare-python>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
