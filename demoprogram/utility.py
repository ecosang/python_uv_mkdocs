"""
Utility functions for the demo program package.
"""

import os
import sys
from typing import List, Any


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file in bytes.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        int: File size in bytes
    """
    try:
        return os.path.getsize(file_path)
    except OSError:
        return -1


def format_bytes(bytes_size: int) -> str:
    """
    Format bytes into human-readable format.
    
    Args:
        bytes_size (int): Size in bytes
        
    Returns:
        str: Formatted string (e.g., "1.5 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} TB"


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: Reversed string
    """
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): Input string
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        int: Number of words
    """
    return len(text.split())


def get_system_info() -> dict:
    """
    Get basic system information.
    
    Returns:
        dict: System information
    """
    return {
        'platform': sys.platform,
        'python_version': sys.version,
        'executable': sys.executable
    } 