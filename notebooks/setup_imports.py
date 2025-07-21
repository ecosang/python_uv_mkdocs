"""
Helper script to set up imports for Jupyter notebooks.
Run this in a notebook cell to add the parent directory to Python path.
"""

import sys
import os
import pathlib

def setup_imports():
    """
    Add the parent directory to Python path to enable importing the demoprogram package.
    """
    # Get the current file's directory using __file__
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"current_file_dir: {current_file_dir}")
    
    # Get the parent directory (where demoprogram package is located)
    parent_dir = str(pathlib.Path(current_file_dir).parent)
    print(f"parent_dir: {parent_dir}")

    # Add to Python path if not already there
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
        print(f"✅ Added {parent_dir} to Python path")
    else:
        print(f"✅ {parent_dir} already in Python path")
    

def test_import():
    # Try to import the package
    setup_imports()
    try:
        from demoprogram import utility, calc
        print("✅ Successfully imported demoprogram package!")
        print(f"   - utility module: {utility}")
        print(f"   - calc module: {calc}")
        return True
    except ImportError as e:
        print(f"❌ Failed to import demoprogram package: {e}")
        print(f"   Current working directory: {os.getcwd()}")
        print(f"   Python path: {sys.path[:3]}...")
        return False

def get_package_info():
    """
    Get information about the demoprogram package.
    """
    try:
        from demoprogram import utility, calc
        
        # Get available functions
        utility_functions = [func for func in dir(utility) if not func.startswith('_')]
        calc_functions = [func for func in dir(calc) if not func.startswith('_')]
        
        print("📦 Demoprogram Package Information:")
        print(f"   📁 Package location: {os.path.dirname(utility.__file__)}")
        print(f"   🔧 Utility functions: {utility_functions}")
        print(f"   🧮 Calc functions: {calc_functions}")
        
    except ImportError:
        print("❌ Package not available. Run setup_imports() first.")

if __name__ == "__main__":
    #setup_imports()
    test_import()
    get_package_info() 