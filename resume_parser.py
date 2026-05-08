def parse_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    return text
