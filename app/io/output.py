def write_output_in_console(output = '\n'):
    """
    Writes output in console.

    Args:
        output (str): The output to be written in console.

    Returns:
        None
    """
    print(output)

def write_to_file_with_python(filename, output):
    """
    Writes output in file with python.

    Args:
        output (str): The output to be written in file.
        filename (str): The name of a file to be written into.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.write(output)