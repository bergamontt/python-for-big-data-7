import pandas as pd

def read_input_from_console():
    """
    Reads input from console.

    Returns:
        str. Input from console as a string.
    """
    return input("Enter input: ")

def read_file_with_python(filename):
    """
    Reads content of the file using python.

    Args:
        filename (str): Name of the file be read.

    Returns:
        str. The content of the file as a string.
    """
    with open(filename, "r") as file:
        return file.read()

def read_file_with_pandas(filename):
    """
    Reads content of the CVS file using pandas.

    Args:
        filename (str): Name of the file be read.

    Returns:
        str. The content of the CSV file as a string.
    """
    df = pd.read_csv(filename)
    return df.to_string()
