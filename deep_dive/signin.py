class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
        
user = User('Denzel Oluoch', 'Okothdenz@gmail.com','(#5fq3$5%)')
print(f"User details: ({user.username}, {user.email})")
        