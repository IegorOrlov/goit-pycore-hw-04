from data import get_cats

def get_cats_info(path: str) -> list[dict[str, str]]:
    try:
        cats_str = get_cats(path)
        cats=[]
        for cat in cats_str:
            attrs = cat.strip().split(",")
            cats.append({"id" : attrs[0], "name" : attrs[1], "age" : attrs[2]})
        return cats
    except FileNotFoundError as e:
        print(e)
        return None
    except IndexError as e:
        print(f"ERROR: The file has gaps or wrong format.")
        return None
