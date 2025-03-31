import os
import unittest

from app.io.output import write_output_in_console, write_to_file_with_python
from app.io.input import read_file_with_python

class TestOutput(unittest.TestCase):
    def setUp(self):
        """
        Set up files before testing
        """
        if not os.path.exists("data"):
            os.mkdir("data")
        self.test_file = "data/test_output.txt"

    def test_write_output_in_console_callable(self):
        """
        Test whether write_output_in_console is callable
        """
        self.assertTrue(callable(write_output_in_console))

    def test_write_output_in_console_takes_output(self):
        """
        Test whether write_output_in_console takes output str
        """
        try:
            write_output_in_console("Hello World")
        except Exception as e:
            self.fail(e)
        self.assertTrue(True)

    def test_write_output_in_console_takes_none_output(self):
        """
        Test whether write_output_in_console handles None output
        """
        try:
            write_output_in_console()
        except Exception as e:
            self.fail(e)
        self.assertTrue(True)

    def test_write_to_file_with_python_callable(self):
        """
        Test whether write_to_file_with_python is callable
        """
        self.assertTrue(callable(write_to_file_with_python))

    def test_write_to_file_with_python_normal_output(self):
        """
        Test whether write_to_file_with_python writes output str in file
        """
        output = "Hello World"
        write_to_file_with_python(self.test_file, output)
        file_contents = read_file_with_python(self.test_file)
        self.assertEqual(file_contents, output)

    def test_write_to_file_with_python_empty_output(self):
        """
        Test whether write_to_file_with_python writes empty output str in file
        """
        output = ""
        write_to_file_with_python(self.test_file, output)
        file_contents = read_file_with_python(self.test_file)
        self.assertEqual(file_contents, output)

    def test_write_to_file_with_python_empty_overwrites(self):
        """
        Test whether write_to_file_with_python overwrites content in file with new
        """
        output = "Hello World"
        write_to_file_with_python(self.test_file, output)
        new_output = "Goodbye, World!"
        write_to_file_with_python(self.test_file, new_output)
        file_contents = read_file_with_python(self.test_file)
        self.assertEqual(file_contents, new_output)

    def tearDown(self):
        """
        Clean up files after testing
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()