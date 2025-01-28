def log(data):
    file_path = "first_round.txt"
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write(data + "\n")