def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# "add username phone" --> add contact
def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please provide a name and phone number."

# "change username phone" --> change contact phone
def change_contact(args, contacts):
    try:
        name, phone = args
        # print(name)
        # print(contacts)

        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except IndexError:
        return "Error: Please provide a name."

# "phone username" --> show contact phone
def show_contacts(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        else:
            return "Contact not found."
    except IndexError:
        return "Error: Please provide a name."

# "all" --> show all contacts
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."

    phones = []
    for name, phone in contacts.items():
        phones.append(f"{name}: {phone}")
    return "\n".join(phones)



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # "close", "exit" -->  "Good bye!"
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # "hello"--> "How can I help you?"
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contacts(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


