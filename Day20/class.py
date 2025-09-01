class User:
    def __init__(self):
        print("User created")

user1 = User() # Instance of User class which is object
user1.name = "John" # Adding attribute to the object
user1.age = 30 # Adding another attribute to the object
print(user1.name)


user2 = User()
user2.name = "Jane"
user2.age = 25
print(user2.name)

user3 = User()
user3.name = "Doe"
user3.age = 40
print(user3.name)

#####################################

class User:
    def __init__(self, user_id, user_name, followers):
        self.id = user_id
        self.name = user_name
        self.followers = followers
        print("User created") # Constructor - called when object is created

user1 = User(1, "John", 100)
user2 = User(2, "Jane", 150)
user3 = User(3, "Doe", 200)
print(user1.name, user1.followers)