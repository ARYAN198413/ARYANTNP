import os

# In-memory storage for user data
users = {}

# Function for user registration
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please log in.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful! Please log in to continue.")

# Function for user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# File Management Operations
def create_file():
    file_name = input("Enter the file name: ")
    if os.path.exists(file_name):
        print("File already exists.")
        return
    content = input("Enter content for the file: ")
    with open(file_name, "w") as file:
        file.write(content)
    print(f"File '{file_name}' created successfully.")

def read_file():
    file_name = input("Enter the file name to read: ")
    if not os.path.exists(file_name):
        print("File does not exist.")
        return
    with open(file_name, "r") as file:
        print("\n--- File Content ---")
        print(file.read())
        print("--------------------")

def update_file():
    file_name = input("Enter the file name to update: ")
    if not os.path.exists(file_name):
        print("File does not exist.")
        return
    content = input("Enter content to append: ")
    with open(file_name, "a") as file:
        file.write("\n" + content)
    print(f"File '{file_name}' updated successfully.")

def delete_file():
    file_name = input("Enter the file name to delete: ")
    if not os.path.exists(file_name):
        print("File does not exist.")
        return
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")

def list_files():
    print("\nFiles in current directory:")
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if files:
        for file in files:
            print(file)
    else:
        print("No files found.")

def change_directory():
    path = input("Enter the directory path to navigate to: ")
    try:
        os.chdir(path)
        print(f"Current directory: {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")
    except NotADirectoryError:
        print("Not a directory.")

def create_directory():
    dir_name = input("Enter the directory name to create: ")
    try:
        os.mkdir(dir_name)
       
