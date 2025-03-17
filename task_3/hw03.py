import sys
from dir_service import display_dir

def main():
    if len(sys.argv) > 1:
        display_dir(sys.argv[1])

if __name__ == "__main__":
    main()