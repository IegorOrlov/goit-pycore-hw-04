def load_data(filename: str) -> list[str]:
    with open(filename, "r", encoding="UTF-8") as file:
        return file.readlines()
    
def get_saleries(filename: str) -> list[float]:
    lines = load_data(filename)
    return [float(line.split(",")[1]) for line in lines]

