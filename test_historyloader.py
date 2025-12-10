# test_historyloader.py
"""
Tests for HistoryLoader module.
"""

import unittest
from historyloader import HistoryLoader

class TestHistoryLoader(unittest.TestCase):
    """Test cases for HistoryLoader class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HistoryLoader()
        self.assertIsInstance(instance, HistoryLoader)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HistoryLoader()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
