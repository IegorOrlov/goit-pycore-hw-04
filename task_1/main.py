from calculate_salery import total_salary

def main():
    total, average =total_salary("/Users/yegor/Projects/GoIT/goit-pycore-hw-04/task_1/salery.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()