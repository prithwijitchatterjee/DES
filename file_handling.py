def write_to_file(file_path, data):
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(data)

def read_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()