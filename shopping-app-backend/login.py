from utils.db_mock import users_db, admins_db

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        """Validates user login using mock user database."""
        if self.username in users_db and users_db[self.username] == self.password:
            print(f"Welcome, {self.username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """Validates admin login using mock admin database."""
        if self.username in admins_db and admins_db[self.username] == self.password:
            print(f"Welcome, Admin {self.username}!")
            return True
        else:
            print("Invalid admin username or password.")
            return False
