Installation
============

Install from PyPI
-----------------

.. code-block:: bash

   pip install mohitkhare

Requirements
------------

- Python 3.9 or later
- Zero runtime dependencies

Install from Source
-------------------

.. code-block:: bash

   git clone https://github.com/arnaudleroy-studio/mohitkhare-python.git
   cd mohitkhare-python
   pip install -e .

Verify Installation
-------------------

.. code-block:: python

   import mohitkhare
   print(mohitkhare.__version__)  # 0.1.0

   # Quick test
   from mohitkhare import slugify
   print(slugify("Hello World!"))  # hello-world

For more developer tips and tutorials, visit `mohitkhare.me/blog <https://mohitkhare.me/blog>`_.
