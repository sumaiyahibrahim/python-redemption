# when a function is attached to a class, it is called a method
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        print("User created")