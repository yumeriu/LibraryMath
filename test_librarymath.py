# test_librarymath.py
"""
Tests for LibraryMath module.
"""

import unittest
from librarymath import LibraryMath

class TestLibraryMath(unittest.TestCase):
    """Test cases for LibraryMath class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LibraryMath()
        self.assertIsInstance(instance, LibraryMath)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LibraryMath()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
