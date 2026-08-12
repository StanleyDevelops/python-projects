import hashlib

# Function to convert string to hash
def hash_password(password):

    # Hasing using sha-256 cryptographic hash function
    password_byte = password.encode("utf-8")
    hash_object = hashlib.sha256(password_byte)

    # the password stored in hexadecimal
    password_hash = hash_object.hexdigest()

    return password_hash
    
# Function to store password with Hash
def add_password(password_list):

    while True:
        website = input("Enter the website: ").strip().lower()
        if website:
            break
        print("Website name cannot be empty!")      # validate empty input

    while True:
        username = input("Enter Username: ").strip().lower()
        if username:
            break
        print("Username cannot be vacant!")

    # Check for Duplicate Website and Username
    existing_account = None
    for account in password_list:
        if (account["website"].lower() == website.lower() and 
            account["username"].lower() == username.lower()):
            existing_account = account
            break

    if existing_account:
        print(f"\nAn account for '{website}' with username '{username}' already exists!")
        choice = input("Would you like to update the password for this account? (y/n): ").strip().lower()
        
        if choice == 'y':
            # Update existing entry password
            while True:
                password = input("Enter NEW Password: ").strip()
                if password:
                    existing_account["password"] = hash_password(password)
                    print("✅ Password updated successfully!")
                    return existing_account
                print("Password must be filled!")
        else:
            print("Operation cancelled. Returning to menu.")
            return None

    while True:
            password = input("Enter New Password to store: ")
            if password:
                new_password = hash_password(password)
                break
            print("Password must be filled!")

    new_record = {"website": website,
            "username": username,
            "password": new_password}
    
    return new_password

# search for password by website
def search_password(password_manager):
    search_website = input("Enter website to search password for: ")
    for data in password_manager:
        if data["website"] == search_website:
            print(data["website"])
            print(data["username"])
            print(data["password"])
            break
        else:
            print("Website not Found!")

# delete password by username
def delete_password(password_manager):
    search_website = input("Enter website to delete password for: ")
    for data in password_manager:
        if data["website"] == search_website:
            password_manager.remove(data)
            print(f"⚠️ Password for {data["website"]} deleted.")
            break
        else:
            print("Website not found!")

# edit password 
def edit_password(password_manager):
    search_website = input("Enter website to edit password for: ").strip().lower()
    for data in password_manager:
        if data["website"] == search_website:

           # if website matches, change password
            while True:
                password = input("Enter New Password to store: ")
                if password:
                    new_password = hash_password(password)
                    data["password"] = new_password
                    print(f"New Password Saved successfully✅")
                    break
                print("Password cannot be empty!")

    else:
        print("Website not Found!")




    


        





