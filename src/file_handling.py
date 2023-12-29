import os

class FileHandler:
    def __init__(self, input_path='data/input/', output_path='data/output/'):
        self.input_path = os.path.abspath(input_path)
        self.output_path = os.path.abspath(output_path)

    def read_input_files(self):
        file_contents = []
        file_list = os.listdir(self.input_path)
        for file_name in file_list:
            file_path = os.path.join(self.input_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    file_contents.append(file.read())
        return file_contents

    def write_output_files(self, content, file_name):
        output_file_path = os.path.join(self.output_path, file_name)
        with open(output_file_path, 'w') as output_file:
            output_file.write(content)
