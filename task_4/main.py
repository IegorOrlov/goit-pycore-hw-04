def parse_input(user_input: str) -> tuple[str, tuple[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: tuple[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: tuple[str], contacts: dict[str, str]) -> str:
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    return f"User {name} not found."

def show_phone(args: tuple[str], contacts: dict[str, str]) -> str:
    name = args[0] if args else ""
    if contacts.get(name):
        return contacts.get(name)
    return f"User {name} not found."

def show_all(contacts: dict[str, str]) -> str:
    str = ""
    for name, phone in contacts.items():
        str= str + f"{name} {phone}\n"
    return str

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "chenge":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
