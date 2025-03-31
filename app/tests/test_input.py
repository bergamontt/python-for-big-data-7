import os
import unittest
import pandas as pd
from unittest.mock import patch

from app.io.input import read_input_from_console, read_file_with_python, read_file_with_pandas

class TestInput(unittest.TestCase):
    def setUp(self):
        """
        Setups needed files before testing
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        self.txt_test_file = "data/test.txt"
        self.cvs_test_file = "data/test.cvs"
        self.txt_empty_file = "data/empty.txt"
        self.cvs_empty_file = "data/empty.csv"
        self.txt_test_file_content = "This is a test line!"
        self.csv_test_file_content = "This is also a test line!"
        with open(self.txt_test_file, "w") as file:
            file.write(self.txt_test_file_content)
        with open(self.cvs_test_file, "w") as file:
            file.write(self.csv_test_file_content)
        with open(self.txt_empty_file, "w"):
            pass
        with open(self.cvs_empty_file, "w"):
            pass

    def test_read_input_from_console_callable(self):
        """
        Test whether read_input_from_console is callable.
        """
        self.assertTrue(callable(read_input_from_console))

    def test_read_input_from_console_returns_input(self):
        """
        Test to check whether read_input_from_console returns the input as a str
        """
        with patch("builtins.input", return_value="This is a test line!"):
            user_input = read_input_from_console()
            self.assertEqual(user_input, "This is a test line!")

    def test_read_input_from_console_returns_empty(self):
        """
        Test to check whether read_input_from_console returns empty input as a str
        """
        with patch("builtins.input", return_value=""):
            user_input = read_input_from_console()
            self.assertEqual(user_input, "")

    def tearDown(self):
        """
        Clean up files after testing
        """
        if os.path.exists(self.txt_test_file):
            os.remove(self.txt_test_file)
        if os.path.exists(self.cvs_test_file):
            os.remove(self.cvs_test_file)
        if os.path.exists(self.txt_empty_file):
            os.remove(self.txt_empty_file)
        if os.path.exists(self.cvs_empty_file):
            os.remove(self.cvs_empty_file)

if __name__ == "__main__":
    unittest.main()