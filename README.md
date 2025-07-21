# Demo Program Package

A simple demonstration Python package containing utility functions and arithmetic calculations.

## Features

- **Utility Functions**: String manipulation, file operations, and system information
- **Arithmetic Functions**: Basic and advanced mathematical operations
- **Error Handling**: Proper exception handling for edge cases
- **Type Hints**: Full type annotation support
- **Documentation**: Comprehensive docstrings for all functions

## Installation

### From Source
```bash
git clone <repository-url>
cd python_uv_mkdocs
pip install -e .
```

### Development Installation
```bash
pip install -e .[dev]
```

## Usage

### Basic Import
```python
from demoprogram import utility, calc
```

### Utility Functions
```python
# String operations
text = "Hello, World!"
reversed_text = utility.reverse_string(text)
word_count = utility.count_words(text)
is_palindrome = utility.is_palindrome("racecar")

# System information
sys_info = utility.get_system_info()
```

### Arithmetic Functions
```python
# Basic arithmetic
result = calc.add(5, 3)        # 8
result = calc.subtract(5, 3)   # 2
result = calc.multiply(5, 3)   # 15
result = calc.divide(6, 2)     # 3.0
result = calc.power(2, 3)      # 8

# Advanced arithmetic
result = calc.square_root(16)  # 4.0
result = calc.factorial(5)     # 120
result = calc.gcd(12, 18)      # 6
result = calc.lcm(12, 18)      # 36

# List operations
result = calc.average([1, 2, 3, 4, 5])  # 3.0

# Percentage and rounding
result = calc.percentage(25, 100)       # 0.25
result = calc.round_to_decimal(3.14159, 2)  # 3.14
```

## Available Functions

### Utility Module (`utility.py`)

- `get_file_size(file_path)`: Get file size in bytes
- `format_bytes(bytes_size)`: Format bytes to human-readable format
- `reverse_string(text)`: Reverse a string
- `is_palindrome(text)`: Check if string is palindrome
- `count_words(text)`: Count words in a string
- `get_system_info()`: Get basic system information

### Calculation Module (`calc.py`)

- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract second from first
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide first by second
- `power(base, exponent)`: Raise base to power
- `square_root(number)`: Calculate square root
- `factorial(n)`: Calculate factorial
- `gcd(a, b)`: Greatest common divisor
- `lcm(a, b)`: Least common multiple
- `average(numbers)`: Calculate average of list
- `percentage(part, total)`: Calculate percentage
- `round_to_decimal(number, decimal_places)`: Round to decimal places

## Running the Demo

### Command Line
```bash
python demo_usage.py
```

### Jupyter Notebooks
For interactive demos, use the notebooks in the `notebooks/` folder:

1. Start Jupyter from the project root:
   ```bash
   jupyter notebook
   ```

2. Navigate to `notebooks/` and open:
   - `quick_start.ipynb` - Simple template to get started
   - `demo_usage.ipynb` - Comprehensive demo with all features

3. Run the import setup cell first, then explore the functions interactively!

## Running Tests

```bash
python test_demoprogram.py
```

Or with pytest (if installed):
```bash
pytest test_demoprogram.py -v
```

## Documentation

### Building Documentation Locally

```bash
# Install documentation dependencies
pip install -r requirements-docs.txt

# Install package in development mode
pip install -e .

# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

Or use the helper script:
```bash
python build_docs.py
```

### Viewing Documentation

- **Local**: http://127.0.0.1:8000 (after running `mkdocs serve`)
- **Online**: https://ecosang.github.io/python_uv_mkdocs/

## Error Handling

The package includes proper error handling for common edge cases:

- Division by zero
- Negative numbers for square root
- Negative numbers for factorial
- Empty lists for average calculation

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library)

## Development

### Project Structure
```
demoprogram/
├── __init__.py      # Package initialization
├── utility.py       # Utility functions
└── calc.py          # Arithmetic functions

notebooks/           # Jupyter notebooks
├── __init__.py      # Makes notebooks a package
├── demo_usage.ipynb # Comprehensive demo notebook
├── quick_start.ipynb # Quick start template
├── setup_imports.py # Import helper script
└── README.md        # Notebook usage instructions

demo_usage.py        # Usage examples
test_demoprogram.py  # Unit tests
setup.py            # Package setup
README.md           # This file
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run tests to ensure everything works
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.