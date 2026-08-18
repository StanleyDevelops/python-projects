# URL shortener

from storage import load_data, save_data
from utils import url_storage, find_url

urls = load_data()

while True:
    print("---------------------MENU----------------------")
    print("1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Save and Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(f"Please enter valid input!")
        continue

    if choice == 1:
        url = url_storage()
        urls.append(url)
        print(f"New URL succesfully saved.")

    elif choice == 2:
        if not urls:
            print(f"No URL record found!")
        else:
            find_url(urls)
            
    if choice == 3:
        save_data(urls)
        print(f"Exiting...")
        print(f"Good Bye!")
        break

    
