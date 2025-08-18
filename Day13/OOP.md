# Object Oriented Programming
- OOP is a programming style where we structure code using objects and classes.
- A **class** is a blueprint (like a design plan).
- An **object** is a real instance of that class (like a building from the blueprint).

## Why use OOP?
- OOP allows programmers to create their own objects that have methods and attributes.
- allows to call methods off of them with the .method_name() syntax
- Helps organize complex code
- Promotes reuse with inheritance
- Secures data with Encapsulation
- Gives structure to programs (especially to large codes)

Syntax:
```python
class NameOfClass: 
    # defines new class
    # The name must start with a capital letter by convention.
    def __init__(self,param1,param2): 
        # __init__ is the constructor method for class.
        # It runs automatically when you create an object.
        # self refers to the current object.
        self.param1 = param1
        # creating an instance variable param1
        self.param2 = param2
        # creating an instance variable param2
    
    def some_method(self): # instance method
        # This is a method (a function that belongs to the class).
        # self lets the method access the object’s data (like param1 and param2).
        print(self.param1)
        # This will print the value of param1 for that specific object.

obj = NameOfClass("hello", "world")
obj.some_method() # Output: hello
```



Example :
```python
class Dog():
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='lab',name='Sammy'.spots="No spots")
print(my_dog.breed)
```

Example :
```python
# Define a class named Dog
class Dog:
    # CLASS ATTRIBUTE (shared by all dogs)
    species = 'mammal'

    # Constructor: runs automatically when a new Dog is created
    def __init__(self, breed, name, spots):
        # INSTANCE ATTRIBUTES: unique to each object
        self.breed = breed    # The breed of the dog (e.g., huskie)
        self.name = name      # The name of the dog (e.g., Tommy)
        self.spots = spots    # Boolean: Does the dog have spots? (True/False)

    # METHOD: A function defined inside the class
    def bark(self):
        # Uses the object's name attribute in the string
        print("WOOF! My name is {}.".format(self.name))

# Creating an object (instance) of the Dog class
my_dog = Dog('Huskie', 'Tommy', False)

# Accessing the class attribute (same for all dogs)
print("Species:", my_dog.species)

# Accessing instance attributes
print("Breed:", my_dog.breed)
print("Name:", my_dog.name)
print("Has spots?", my_dog.spots)

# Calling the method
my_dog.bark()
```

Example :
```python
# Define a class named Circle
class Circle():
    
    # CLASS ATTRIBUTE (shared by all instances)
    pi = 3.14

    # Constructor method to initialize the object
    def __init__(self, radius=1):
        # Instance attribute: specific to each object
        self.radius = radius
        
        # Calculate area using the class attribute 'pi'
        # We can use self.pi OR Circle.pi — both work
        self.area = self.radius * self.radius * Circle.pi

    # METHOD: Calculates and returns the circumference
    def get_circumference(self):
        return self.radius * Circle.pi * 2

# Creating an instance of Circle with radius 30
my_circle = Circle(30)

# Access and print the radius
print("Radius:", my_circle.radius)

# Access and print the area
print("Area:", my_circle.area)

# Call the method to get the circumference
print("Circumference:", my_circle.get_circumference())
```