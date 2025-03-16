from data import get_saleries

def get_sum(selaries: list[float]) -> float:
    sum = 0
    for salery in selaries:
        sum= sum + salery
    return sum

def total_salary(path: str) -> tuple[float, float]:
    try:
        selaries = get_saleries(path)
        sum = get_sum(selaries)
        return (sum, sum/len(selaries))
    except FileNotFoundError as e:
        print(e)
        return None
