import os

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