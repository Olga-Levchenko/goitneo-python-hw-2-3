def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return {
                "parse_input": "Invalid command.",
                "add_contact": "Give me name and phone please.",
                "change_contact": "Give me name and phone please.",
                "show_phone": "Give me name please."
            }[func.__name__]
        except KeyError:
            return "Name not found."

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contact_exists = contacts.get(name) != None
    if not contact_exists:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) == 0:
        raise ValueError
    name = args[0]
    return f"{contacts[name]}"

def show_all(contacts):
    return "\n".join(map(lambda x: f"{x} {contacts[x]}", contacts))

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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()