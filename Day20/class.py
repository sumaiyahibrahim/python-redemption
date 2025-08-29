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
