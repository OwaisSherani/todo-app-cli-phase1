"""
Main entry point for the Todo CLI Application.
"""
import sys
import os

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.dirname(__file__))

from src.cli.main import main


if __name__ == "__main__":
    main()