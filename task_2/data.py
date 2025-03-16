def get_cats(filename: str) -> list[str]:
    with open(filename, "r", encoding="UTF-8") as file:
        return file.readlines()