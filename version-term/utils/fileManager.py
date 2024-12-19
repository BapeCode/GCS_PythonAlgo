import os
from typing import List, Tuple
import hashlib

class FileManager:

    def load_file(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            return file.readlines()
        
    def save_file(self, file_path, data):
       with open(file_path, mode="w", encoding="utf-8") as file:
            for row in data:
                file.write(",".join(map(str, row)) + "\n")

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist")

    def clean_folder(self, users: List[str]) -> Tuple[List[str], List[str]]:
        files = [hashlib.md5(user.username.encode()).hexdigest() + "_products.csv" for user in users]

        files.append("users.csv")

        for file in os.listdir("./data"):
            if (file not in files):
                os.remove("./data/" + file)
                print(f"File {file} deleted successfully. Because it is not used anymore.")
            
        print("All files are cleaned successfully.")
        