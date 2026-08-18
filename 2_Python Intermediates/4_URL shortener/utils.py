import random

def url_storage():

    while True:
        url = input("Type the url: ")
        if url:
            break
        print("URl cannot be empty!")

    short_code = f"abc{random.randrange(1,1000)}"

    return {short_code: url}

def find_url(urls):

    while True:
        search_code = input("Enter URL to search for: ").lower().strip()
        if search_code:
            break
        print("Search cannot be empty")

    for item in urls:
        if search_code in item:
            print(f"URL found succesfully!")
            print(f"{item[search_code]}")
            return
        
    print(f"Searched URL not found!") 

    

