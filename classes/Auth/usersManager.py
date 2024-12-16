from utils.fileManager import FileManager
from .users import Users
import hashlib


class UsersManager:
    USERS_FILE = "./data/users.csv"

    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            file = FileManager().load_file(self.USERS_FILE)
            data = [line.strip().split(",") for line in file[1:]]
            Object = [Users(user[0], user[1], user[2], user[3], user[4]) for user in data]
            return Object
        except FileNotFoundError:
            return []
    
    def save_users(self):
        data = [
            ['Username', "Password", "Email", "Group"],
            *[[user.username, user.password, user.email, user.group] for user in self.users]
        ]

        FileManager().save_file(self.USERS_FILE, data)

    def view_users(self):
        if not self.users:
            print("No users found.")
        else:
            print(f"{"Username":<20} {"Password":<50} {"Email":<50} {"Group":<10}")
            print("-" * 50)
            for user in self.users:
                print(user)
    
    def delete_user(self):
        username = input("Enter username : ")  

        self.users = [user for user in self.users if user.username != username]
        self.save_users()

    def login(self):
        username = input("Enter Username or Email: ")
        password = input("Enter password: ")
        password = hashlib.md5(password.encode()).hexdigest()

        for user in self.users:
            if user.username == username or user.email == username:

                print(user.password, password)
                
                if user.password == password:
                    print(f"Welcome {user.username}")
                    return user
                else:
                    print("Your identifiant or password is incorrect.")
        
    def register(self):
        username = input("Enter Username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")

        password = hashlib.md5(password.encode()).hexdigest()

        user = Users(username, password, email, "member")
        self.users.append(user)
        self.save_users()
        print(f"User '{username}' added successfully.")

    def modify_user_group(self):
        username = input("Enter username: ")
        group = input("Enter group: ")

        for user in self.users:
            if user.username == username:
                user.group = group
                self.save_users()
                print(f"User '{username}' group modified successfully.")
                break 

    def __str__(self):
        return f"{self.username:<20} {self.email:<20} {self.password:<20} {self.group:<20}"