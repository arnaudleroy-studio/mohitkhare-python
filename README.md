# mohitkhare

Developer utilities and AI engineering tools by [Mohit Khare](https://mohitkhare.me) -- practical helpers for text processing, LLM token estimation, and everyday dev productivity.

## Install

```bash
pip install mohitkhare
```

## Text Utilities

```python
from mohitkhare import slugify, truncate, chunk_text, reading_time

# URL-safe slugs
slugify("My Blog Post Title!")       # 'my-blog-post-title'
slugify("Cafe & Restaurant -- Paris") # 'cafe-restaurant-paris'

# Smart truncation
truncate("Long article text here...", 15)  # 'Long article...'

# Chunk text for LLM processing (splits on sentence boundaries)
chunks = chunk_text(long_document, max_chars=4000, overlap=200)

# Reading time estimate
reading_time("word " * 500)  # '2 min read'
```

## LLM Token Estimation

Estimate token counts and API costs without importing heavy tokenizers.

```python
from mohitkhare import estimate_tokens, estimate_cost

# Token estimation (character-based heuristic)
estimate_tokens("Hello, how are you?")                    # 5
estimate_tokens("Long prompt " * 100, model="claude")     # ~336

# Cost estimation
estimate_cost("A " * 10000, model="gpt-4o")               # '$0.0050'
estimate_cost("Short text", model="claude-haiku")          # '$0.0000'
estimate_cost("Output text", model="gpt-4o", is_output=True)
```

Supports: GPT-4o, GPT-4, GPT-3.5, Claude (Opus/Sonnet/Haiku), Gemini, Llama, Mistral.

## Dev Productivity

```python
from mohitkhare import timer, retry, flatten, chunk_list, dedupe

# Time function execution
@timer
def slow_function():
    ...  # prints "slow_function took 1.234s"

# Retry with exponential backoff
@retry(max_attempts=3, delay=1.0, backoff=2.0)
def flaky_api_call():
    ...

# Flatten nested lists
flatten([[1, 2], [3, [4, 5]]])  # [1, 2, 3, 4, 5]

# Chunk lists for batch processing
chunk_list(range(10), 3)  # [[0,1,2], [3,4,5], [6,7,8], [9]]

# Dedupe preserving order
dedupe([3, 1, 2, 1, 3])                # [3, 1, 2]
dedupe(["a", "A", "b"], key=str.lower)  # ['a', 'b']
```

## Links

- [mohitkhare.me](https://mohitkhare.me) -- Blog and portfolio
- [Blog](https://mohitkhare.me/blog) -- AI engineering articles

## License

MIT
