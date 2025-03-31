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

    def test_read_file_with_python_callable(self):
        """
        Test whether read_file_with_python is callable.
        """
        self.assertTrue(callable(read_file_with_python))

    def test_read_file_with_python_returns_file_content(self):
        """
        Test whether read_file_with_python returns the proper file content
        """
        file_content = read_file_with_python(self.txt_test_file)
        self.assertEqual(file_content, self.txt_test_file_content)

    def test_read_file_with_python_non_existing_file(self):
        """
        Test whether read_file_with_python rises an error when reading from non-existing file.
        """
        with self.assertRaises(FileNotFoundError):
            read_file_with_python("data/non-existing.csv")

    def test_read_file_with_python_empty_file(self):
        """
        Test whether read_file_with_python returns empty str when reading from empty file.
        """
        file_content = read_file_with_python(self.txt_empty_file)
        self.assertEqual("", file_content)

    def test_read_file_with_pandas_callable(self):
        """
        Test whether read_file_with_python is callable.
        """
        self.assertTrue(callable(read_file_with_pandas))

    def test_read_file_with_pandas(self):
        """
        Test whether read_file_with_pandas returns the proper file content
        """
        file_content = read_file_with_pandas(self.cvs_test_file)
        expected_content = pd.read_csv(self.cvs_test_file).to_string()
        self.assertEqual(file_content, expected_content)

    def test_read_file_with_pandas_non_existing_file(self):
        """
        Test whether read_file_with_pandas rises an error when reading from non-existing file.
        """
        with self.assertRaises(FileNotFoundError):
            read_file_with_pandas("data/non-existing.csv")

    def test_read_file_with_pandas_empty_file(self):
        """
        Test whether read_file_with_pandas returns empty str when reading from empty file.
        """
        with self.assertRaises(pd.errors.EmptyDataError):
            read_file_with_pandas(self.cvs_empty_file)

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