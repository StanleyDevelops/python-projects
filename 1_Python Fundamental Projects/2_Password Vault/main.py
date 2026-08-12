from storage import load_data, save_data
from utils import add_password, search_password, delete_password, edit_password, hash_password
import getpass

password_manager = load_data()

try:
    entered_password = getpass.getpass("Enter Password manager Password: ")
    password_entered = hash_password(entered_password)
    
    with open("secret_password.txt", "r") as file:
        stored_password = file.read().strip() #removes extra spaces or newlines

    # Compare the input with the file text
    if password_entered == stored_password:
        print("Access Granted")

        while True:
            print(f"_-_-_-_-_-_-_-_-_-_- MENU _-_-_-_-_-_-_-_-_-_-")
            print(f"1. Add password")
            print(f"2. Search password")
            print(f"3. Delete password")
            print(f"4. Edit password")
            print(f"5. Save and Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if choice == 1:
                password = add_password(password_manager)
                password_manager.append(password)
                print(f"Password for {password["website"]} saved Successfully✅")

            elif choice == 2:
                if not password_manager:
                    print("No Password stored!")
                    continue
                search_password(password_manager)

            elif choice == 3:
                if not password_manager:
                    print("No Password stored!")
                    continue
                else:
                    delete_password(password_manager)

            elif choice == 4:
                if not password_manager:
                    print("No Password stored!")
                    continue
                edit_password(password_manager)

            elif choice == 5:
                print(f"Exiting...")
                save_data(password_manager)
                break
    else:
        print("Access Denied")
except IOError:
    print("File Couldn't be opened!")


