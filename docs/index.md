# Demoprogram Package

A simple demonstration Python package containing utility functions and arithmetic calculations.

## Quick Start

```python
from demoprogram import utility, calc

# Utility functions
text = "Hello, World!"
reversed_text = utility.reverse_string(text)
word_count = utility.count_words(text)

# Arithmetic functions
result = calc.add(5, 3)
square_root = calc.square_root(16)
factorial = calc.factorial(5)
```

## Installation

```bash
# From source
git clone https://github.com/ecosang/python_uv_mkdocs.git
cd python_uv_mkdocs
pip install -e .
```

## API Documentation

- **[Utility Functions](api/utility.md)** - String manipulation, file operations, and system information
- **[Arithmetic Functions](api/calc.md)** - Basic and advanced mathematical operations

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library) 