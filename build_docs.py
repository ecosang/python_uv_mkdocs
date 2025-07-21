#!/usr/bin/env python3
"""
Simple script to build and serve MkDocs documentation locally.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def main():
    """Main function to build and serve documentation."""
    print("🚀 Building and serving MkDocs documentation...")
    
    # Check if we're in the right directory
    if not os.path.exists('mkdocs.yml'):
        print("❌ Error: mkdocs.yml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Install dependencies if needed
    if not run_command("pip install -r requirements-docs.txt", "Installing documentation dependencies"):
        sys.exit(1)
    
    # Install the package in development mode
    if not run_command("pip install -e .", "Installing package in development mode"):
        sys.exit(1)
    
    # Build documentation
    if not run_command("mkdocs build", "Building documentation"):
        sys.exit(1)
    
    print("\n🎉 Documentation built successfully!")
    print("📁 Built files are in the 'site' directory")
    
    # Ask if user wants to serve the documentation
    serve = input("\n🌐 Would you like to serve the documentation locally? (y/n): ").lower().strip()
    
    if serve in ['y', 'yes']:
        print("\n🚀 Starting local server...")
        print("📖 Documentation will be available at: http://127.0.0.1:8000")
        print("🛑 Press Ctrl+C to stop the server")
        
        try:
            subprocess.run("mkdocs serve", shell=True, check=True)
        except KeyboardInterrupt:
            print("\n👋 Server stopped")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main() 