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
            Object = [Users(user[0], user[1], user[2], user[3]) for user in data]
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
            print(f"{"Username":<20} {"Password":<10} {"Email":<10} {"Group":<10}")
            print("-" * 50)
            for user in self.users:
                print(user)
    
    def delete_user(self, username):
        self.users = [user for user in self.users if user.username != username]
        self.save_users()

    def login(self):
        username = input("Enter Username or Email: ")
        password = input("Enter password: ")
        password = hashlib.md5(password.encode()).hexdigest()

        for user in self.users:
            print(user.username, user.email, username)
            if user.username == username or user.email == username:
                
                if user.password == password:
                    print(f"Welcome {user.username}")
                    return True, user
                else:
                    print("Your identifiant or password is incorrect.")
        
        
        