from cat_service import get_cats_info

def main():
    cats_info = get_cats_info("/Users/yegor/Projects/GoIT/goit-pycore-hw-04/task_2/cats.txt")
    print(cats_info)

if __name__ == "__main__":
    main()