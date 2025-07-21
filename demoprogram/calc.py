"""
Arithmetic calculation functions for the demo program package.
"""

import math
from typing import Union, List


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of the two numbers
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide first number by second number.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        Quotient of the division
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Raise base to the power of exponent.
    
    Args:
        base: Base number
        exponent: Exponent
        
    Returns:
        Result of base raised to exponent
    """
    return base ** exponent


def square_root(number: Union[int, float]) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: Number to find square root of
        
    Returns:
        Square root of the number
        
    Raises:
        ValueError: If number is negative
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Greatest common divisor
    """
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple of two integers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Least common multiple
    """
    return abs(a * b) // math.gcd(a, b)


def average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Average of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def percentage(part: Union[int, float], total: Union[int, float]) -> float:
    """
    Calculate what percentage part is of total.
    
    Args:
        part: Part value
        total: Total value
        
    Returns:
        Percentage as a decimal (multiply by 100 for percentage)
        
    Raises:
        ZeroDivisionError: If total is zero
    """
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero")
    return part / total


def round_to_decimal(number: float, decimal_places: int = 2) -> float:
    """
    Round a number to a specified number of decimal places.
    
    Args:
        number: Number to round
        decimal_places: Number of decimal places (default: 2)
        
    Returns:
        Rounded number
    """
    return round(number, decimal_places) 