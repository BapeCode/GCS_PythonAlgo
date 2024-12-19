from ..tools.fileManager import FileManager
from .users import Users
import hashlib
import requests 
from ..tools.console import console


class UsersManager:
    USERS_FILE = "./data/users.csv"

    def __init__(self):
        self.users = self.load_users()
        console.debug("Users Manager Loaded")

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
            print(f"{"Username":<20} {"Password":<50} {"Email":<50} {"Group":<10}")
            print("-" * 50)
            for user in self.users:
                print(user)
    
    def delete_user(self):
        username = input("Enter username : ")  

        self.users = [user for user in self.users if user.username != username]
        self.save_users()

    def login(self, username, password):
        password = hashlib.md5(password.encode()).hexdigest()

        for user in self.users:
            if user.username == username or user.email == username:

                if user.password == password:
                    print(f"Welcome {user.username}")
                    return user
                else:
                    print("Your username or password is incorrect.")

    def verify_password_hibp(self, password):
        
        sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=20, headers={'User-Agent': 'Gestionix/1.0'})
        response.raise_for_status()

        
        for line in response.text.splitlines():
            leaked_suffix, _ = line.split(':')
            if leaked_suffix == suffix:
                return True

        return False

    def verify_password_local(self, password):
        
        with open('./data/rockyou_md5.txt', mode='r', encoding='UTF-8') as file:
            common_passwords = [line.strip() for line in file]
            
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            return hashed_password in common_passwords

    def register(self):
        username = input("Enter Username: ")
        email = input("Enter Email: ")

        
        while True:
            password = input("Enter password: ")

            
            if self.verify_password_hibp(password):
                print("Password found in public breaches (HIBP). Try a different one.")
                continue

            if self.verify_password_local(password):
                print("Password is too common (rockyou). Try a different one.")
                continue

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        user = Users(username, hashed_password, email, "member")
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

    def reload_data(self):
        users = [user for user in self.users]
        FileManager().clean_folder(users)

