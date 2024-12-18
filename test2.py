# Example Python code with a 'with' statement
def read_file_content():
    file_path = "sample.txt"
    with open(file_path, "r") as file:
        content = file.read()
        print(content)


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as file:
            return file.read()


# Running the function
read_file_content()

# Creating a FileReader object and reading the file
file_reader = FileReader("sample.txt")
print(file_reader.read())
