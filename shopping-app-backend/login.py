class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.users_db = {"user1": "password1"} 
        
    def login(self):
        if self.username in self.users_db and self.users_db[self.username] == self.password:
            return True
        else:
            return False
