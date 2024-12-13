class Users:
    def __init__(self, username, password, email, group):
        self.username = username
        self.password = password
        self.email = email
        self.group = group

    def __str__(self):
        return f"{self.username:<20} {self.email:<20} {self.password:<20} {self.group:<20}"