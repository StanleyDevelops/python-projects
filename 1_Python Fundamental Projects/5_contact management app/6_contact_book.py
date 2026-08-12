from time import sleep

def add_contact():
    while True:
        try:
            phone = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid input! Phone numbers must contain digits only.")
            
    email = input("Enter your email: ").strip()
    my_dict = {"phone": phone, "email": email}
    return my_dict

my_contact = {}    
stay = True

while stay:
    print("\n==================== MENU ==================") 
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    print("============================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid option number!")
        continue
     
    # 1. ADD CONTACT
    if choice == 1:
        name = input("Enter contact name: ").strip()
        
        if name.isdigit():
            print("Names cannot be just pure numbers! Transaction aborted.")
            continue
            
        contact = add_contact()
        my_contact[name] = contact
        print(f"'{name}' successfully added to contacts!")

    # 2. VIEW ALL
    elif choice == 2:
        if not my_contact:
            print("Contact book is empty!")
            continue

        print(f"\n--- Displaying All Contacts ({len(my_contact)}) ---")
        for name, details in my_contact.items():
            print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")

    # 3. SEARCH CONTACT
    elif choice == 3:
        if not my_contact:
            print("No contacts stored to search from!")
            continue

        search_contact = input("Enter name to search: ").strip()
        
        if search_contact in my_contact:
            details = my_contact[search_contact]
            print(f"\n Match Found for '{search_contact}':")
            print(f"   Phone: {details['phone']}")
            print(f"   Email: {details['email']}")
        else:
            print(f"No entry found for '{search_contact}'.")

    # 4. UPDATE CONTACT
    elif choice == 4:
        if not my_contact:
            print("No contacts available to update!")
            continue

        update_name = input("Enter contact name to update: ").strip()
        
        if update_name in my_contact:
            try:
                update_phone = int(input("Enter new phone number: "))
                my_contact[update_name]["phone"] = update_phone
                print(f"Success! {update_name}'s record updated.")
            except ValueError:
                print("Invalid format! Phone updates require numbers only.")
        else:
            print("The contact entry does not exist.")

    # 5. DELETE CONTACT
    elif choice == 5:
        if not my_contact:
            print("The Contact book is already empty!")
            continue

        delete_search = input("Enter contact name to delete: ").strip()
        
        if delete_search in my_contact:
            my_contact.pop(delete_search)
            print(f"'{delete_search}' has been permanently dropped.")
        else:
            print(f"Could not find '{delete_search}' in files.")

    # 6. ANIMATED COUNTDOWN QUIT
    elif choice == 6:
        print("\nEXITING APP in 3 sec...")
        for count in range(3, 0, -1):
            print(f"{count}...")
            sleep(1)
        print("Goodbye!")
        stay = False