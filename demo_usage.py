#!/usr/bin/env python3
"""
Demo script showing how to use the demoprogram package.
"""

from demoprogram import utility, calc


def main():
    print("=== Demo Program Package Usage ===\n")
    
    # Demo utility functions
    print("1. Utility Functions:")
    print("-" * 30)
    
    # String utilities
    text = "Hello, World!"
    print(f"Original text: {text}")
    print(f"Reversed: {utility.reverse_string(text)}")
    print(f"Word count: {utility.count_words(text)}")
    print(f"Is 'racecar' a palindrome? {utility.is_palindrome('racecar')}")
    print(f"Is 'hello' a palindrome? {utility.is_palindrome('hello')}")
    
    # System info
    sys_info = utility.get_system_info()
    print(f"\nSystem info: {sys_info}")
    
    print("\n" + "=" * 50 + "\n")
    
    # Demo arithmetic functions
    print("2. Arithmetic Functions:")
    print("-" * 30)
    
    # Basic arithmetic
    a, b = 10, 3
    print(f"Addition: {a} + {b} = {calc.add(a, b)}")
    print(f"Subtraction: {a} - {b} = {calc.subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {calc.multiply(a, b)}")
    print(f"Division: {a} / {b} = {calc.divide(a, b):.2f}")
    print(f"Power: {a} ^ {b} = {calc.power(a, b)}")
    
    # Advanced arithmetic
    print(f"Square root of {a}: {calc.square_root(a):.2f}")
    print(f"Factorial of {b}: {calc.factorial(b)}")
    print(f"GCD of {a} and {b}: {calc.gcd(a, b)}")
    print(f"LCM of {a} and {b}: {calc.lcm(a, b)}")
    
    # List operations
    numbers = [1, 2, 3, 4, 5]
    print(f"Average of {numbers}: {calc.average(numbers):.2f}")
    
    # Percentage
    part, total = 25, 100
    percentage_val = calc.percentage(part, total)
    print(f"{part} is {percentage_val * 100:.1f}% of {total}")
    
    # Rounding
    pi = 3.14159
    print(f"Pi rounded to 2 decimal places: {calc.round_to_decimal(pi, 2)}")
    print(f"Pi rounded to 4 decimal places: {calc.round_to_decimal(pi, 4)}")
    
    print("\n" + "=" * 50 + "\n")
    
    # Error handling examples
    print("3. Error Handling Examples:")
    print("-" * 30)
    
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Division by zero error: {e}")
    
    try:
        calc.square_root(-4)
    except ValueError as e:
        print(f"Square root error: {e}")
    
    try:
        calc.factorial(-1)
    except ValueError as e:
        print(f"Factorial error: {e}")
    
    try:
        calc.average([])
    except ValueError as e:
        print(f"Average error: {e}")


if __name__ == "__main__":
    main() 