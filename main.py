from app.io.input import read_input_from_console, read_file_with_python, read_file_with_pandas
from app.io.output import write_output_in_console, write_to_file_with_python

def main():
    """
    Main function to showcase the functionality of the program.

    Returns:
        None
    """
    txt_filename = "data/dummy.txt"
    csv_filename = "data/dummy.csv"
    output_filename = "data/dummy_out.txt"

    user_input = read_input_from_console()
    file_content_python = read_file_with_python(txt_filename)
    file_content_pandas = read_file_with_pandas(csv_filename)

    write_output_in_console(user_input)
    write_output_in_console(file_content_python)
    write_output_in_console(file_content_pandas)

    write_to_file_with_python(output_filename, user_input)

if __name__ == '__main__':
    main()