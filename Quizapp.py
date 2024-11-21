# In-memory storage for user data
users = {}

# Questions for each subject
quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": 0},
        {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Heap", "Tree"], "answer": 1},
        {"question": "What is the worst-case time complexity of quicksort?", "options": ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], "answer": 1},
        {"question": "Which data structure uses FIFO?", "options": ["Queue", "Stack", "Heap", "Graph"], "answer": 0},
        {"question": "What is a full binary tree?", "options": ["Every node has 0 or 2 children", "All leaves are at the same level", "All nodes have 2 children", "All levels are filled"], "answer": 0},
        {"question": "Which of these is a self-balancing binary search tree?", "options": ["AVL Tree", "Binary Tree", "Heap", "B Tree"], "answer": 0},
        {"question": "What is the height of a red-black tree?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": 0},
        {"question": "Which algorithm is used to find the shortest path in a graph?", "options": ["Dijkstra", "DFS", "Kruskal", "BFS"], "answer": 0},
        {"question": "Which data structure is used in breadth-first search?", "options": ["Stack", "Queue", "Heap", "Graph"], "answer": 1},
        {"question": "What is the time complexity to insert an element in a binary heap?", "options": ["O(log n)", "O(1)", "O(n)", "O(n log n)"], "answer": 0},
    ],
    "DBMS": [
        {"question": "Which command is used to retrieve data from a database?", "options": ["SELECT", "DELETE", "INSERT", "UPDATE"], "answer": 0},
        {"question": "Which key uniquely identifies a record in a table?", "options": ["Primary Key", "Foreign Key", "Candidate Key", "Super Key"], "answer": 0},
        {"question": "What does ACID stand for in DBMS?", "options": ["Atomicity, Consistency, Isolation, Durability", "Addition, Consistency, Integrity, Data", "Atomicity, Change, Isolation, Durability", "Atomicity, Consistency, Integrity, Durability"], "answer": 0},
        {"question": "Which normal form removes partial dependency?", "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": 1},
        {"question": "What is a foreign key?", "options": ["A primary key in another table", "A unique key", "A key in the same table", "A composite key"], "answer": 0},
        {"question": "Which SQL clause is used to group data?", "options": ["GROUP BY", "ORDER BY", "HAVING", "WHERE"], "answer": 0},
        {"question": "What is the purpose of an index in a database?", "options": ["To improve query performance", "To store data", "To create a backup", "To enforce constraints"], "answer": 0},
        {"question": "Which type of join returns matching rows from both tables?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "answer": 0},
        {"question": "What does DDL stand for?", "options": ["Data Definition Language", "Data Description Language", "Data Development Language", "Data Design Language"], "answer": 0},
        {"question": "Which constraint ensures unique values in a column?", "options": ["UNIQUE", "PRIMARY KEY", "FOREIGN KEY", "NOT NULL"], "answer": 0},
    ],
    "Python": [
        {"question": "What is the output of `print(2 ** 3)`?", "options": ["6", "8", "9", "16"], "answer": 1},
        {"question": "Which of the following is immutable?", "options": ["List", "Set", "Dictionary", "Tuple"], "answer": 3},
        {"question": "How do you define a function in Python?", "options": ["def", "function", "define", "func"], "answer": 0},
        {"question": "What does the `len()` function do?", "options": ["Find length of an object", "Find type of an object", "Find maximum value", "Find minimum value"], "answer": 0},
        {"question": "What is the output of `bool([])`?", "options": ["True", "False", "Error", "None"], "answer": 1},
        {"question": "Which keyword is used for exception handling?", "options": ["try", "except", "finally", "All of the above"], "answer": 3},
        {"question": "Which module is used for regular expressions?", "options": ["re", "regex", "regexp", "os"], "answer": 0},
        {"question": "How do you import a module?", "options": ["import module_name", "include module_name", "require module_name", "load module_name"], "answer": 0},
        {"question": "What is a lambda function?", "options": ["Anonymous function", "Recursive function", "Named function", "Generator"], "answer": 0},
        {"question": "What does `is` compare?", "options": ["Identity", "Value", "Type", "Length"], "answer": 0},
    ],
}

# Function for user registration
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please log in.")
        return
    password = input("Enter a password: ")  # Replace getpass with input
    users[username] = password
    print("Registration successful! Please log in to continue.")

# Function for user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")  # Replace getpass with input
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to conduct a quiz
def conduct_quiz(subject):
    print(f"\nStarting the {subject} quiz...")
    score = 0
    questions = quizzes[subject]
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")
        answer = int(input("Your answer (1-4): ")) - 1
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

# Main application
def main():
    while True:
        print("\nQuiz Application")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\nSubjects:")
                    print("1. DSA")
                    print("2. DBMS")
                    print("3. Python")
                    print("4. Logout")
                    subject_choice = input("Choose a subject (1-4): ")
                    if subject_choice == "1":
                        conduct_quiz("DSA")
                    elif subject_choice == "2":
                        conduct_quiz("DBMS")
                    elif subject_choice == "3":
                        conduct_quiz("Python")
                    elif subject_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
