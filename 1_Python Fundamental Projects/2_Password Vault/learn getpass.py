import getpass

def get_master_password():

    while True:
                 
        password = getpass.getpass("Enter Password: ")
        confirm = getpass.getpass("Confirm Password: ")

        if password == confirm:
            print(f"Both Password Matched!!")
            return password
        else:          # if password and confirm aren't same, deny password
            print("Passwords do not match. Please Try again! ")


set_password = get_master_password()
        


