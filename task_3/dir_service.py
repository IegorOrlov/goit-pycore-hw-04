from colorama import Fore
from pathlib import Path

SHIFT = " "*4

def display_dir(path: str) -> None:
    dir = Path(path)
    if dir.exists():
        display(dir, 0)
    else:
        print("No such file or directory")
    
def display(dir: Path, level: int) -> None:
    print(Fore.BLUE + SHIFT*level + dir.name + "\\")
    for path in dir.iterdir():
        if path.is_dir():
            display(path, level + 1)
        else:
            print(Fore.GREEN + SHIFT*(level + 1) + path.name)