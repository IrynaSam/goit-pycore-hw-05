from handlers import add_contact, change_contact, show_phone, show_all
from parse import parse_input

def main():
    contacts = {}
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args,contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))  
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))  
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()