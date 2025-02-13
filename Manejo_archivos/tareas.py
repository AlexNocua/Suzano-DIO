def read_file(file_name):
    """Reads in a file.

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
            print(data)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return ""


def read_file_into_list(file_name):
    """Reads in a file and stores each line as an element in a list"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []


def write_first_line_to_file(file_contents, output_filename):
    """Writes the first line of a string to a file."""
    first_line = file_contents.split("\n")[0]
    try:
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(first_line + "\n")
    except Exception as e:
        print(f"Error writing to '{output_filename}': {e}")


def read_even_numbered_lines(file_name):
    """Reads in the even-numbered lines of a file"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for index, line in enumerate(lines, start=1) if index % 2 == 0]
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []


def read_file_in_reverse(file_name):
    """Reads a file and returns a list of the lines in reverse order"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            reversed_lines = [line.strip() for line in reversed(lines)]
            print(reversed_lines)
            return reversed_lines
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
