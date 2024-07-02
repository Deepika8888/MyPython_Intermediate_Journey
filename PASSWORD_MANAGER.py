
print("Welcome to the password manager.")


def view():
    try:
        with open ("passWw.txt" , 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No passwords found. Add some first.")


def add():
    website_name = input("Enter the website name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open ("passWw.txt", 'a') as fw:
        fw.write(f"Website name: {website_name} | Username: {username} | Password: {password}\n")
    if website_name and username and password:
        print("Your password has been saved.")
    else:
        print("Please add all of the required information.")

        


while True:
    ask = input ("What would you like to do? press view to view your passwords or add to create one or q to quit: ")
    if ask.lower() == "q":
        break
    
    if ask == "view":
        view()
    elif ask == "add":
        add()
    else:
        print("Invalid prompt")

    

