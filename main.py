contacts_dict= {}

def input_error(func):
    def error(*args, **kwargs):
        try :
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return "Enter user name. Invalid command format "
    return error

@input_error
def hello_handler():
    return 'How can I help you?'

@input_error
def add_handler(name, phone):
    contacts_dict[name] = phone
    return f"Contact {name} added with phone {phone}."

@input_error
def change_handler(name, phone):
     contacts_dict[name] = phone
     return f"Phone number for {name} changed to {phone}."

@input_error
def phone_handler(name):
     return f"Phone number for {name}: {contacts_dict.get(name, 'Not found')}"

@input_error
def show_all_handler():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts_dict.items()])

def main():
    while True:
        user_input = input('Please, input your command...').lower()

        if user_input == "hello":
            print(hello_handler())
        elif user_input.startswith ('add'):
            try:
                _, name, phone = user_input.split()
                print(add_handler(name, phone))
            except ValueError:
                print("Invalid format. Usage: add [name] [phone]")
        elif user_input.startswith("change"):
            try:
                _, name, phone = user_input.split()
                print(change_handler(name, phone))
            except ValueError:
                print("Invalid format. Usage: change [name] [new_phone]")
        elif user_input.startswith("phone"):
            try:
                _, name = user_input.split()
                print(phone_handler(name))
            except ValueError:
                print("Invalid format. Usage: phone [name]")
        elif user_input == "show all":
            print(show_all_handler())
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()


   


