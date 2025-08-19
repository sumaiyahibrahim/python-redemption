# Inheritance
Inheritance in Python is like a child getting traits from their parents. If your mom can cook and your dad can sing, you might learn both! In coding, a class (like a blueprint) can pass its features to another class.

# Why us Inheritance useful?
- Reusability
- Easy to manage
- Clear structure

# Step-by-Step Code Example:

## Step 1: Create a Parent Class
```python
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name+" is eating.")
    def sleep(self):
        print(self.name+" is sleeping.")
```
## Step 2: Create a child Class (inheriting Animal)
```python
class Dog(Animal):
    def bark(self):
        print(self.name + " says WOOF!")
```
## Step 3: Use the Child Class
```python
mydog = Dog("Tommy")
mydog.eat()
mydog.sleep()
mydog.bark()
```

# Types of Inheritance

1. Single inheritance
- One parent, one child.
```python
class Parent:
    pass

class Child(Parent):
    pass
```

2. Multiple Inheritance
- One child, multiple parents
```python
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def cooking(self):
        print("Cooking")

class Child(Father, Mother):
    pass

kid = Child()
kid.skills()
kid.cooking()
```

3. Multilevel Inheritance
```python
class Grandparent:
    def story(self):
        print("Old stories")

class Parent(Grandparent):
    def advice(self):
        print("Good advice")

class Child(Parent):
    def fun(self):
        print("Plays games")

kid = Child()
kid.story()
kid.advice()
kid.fun()
```

4. Hierarchical Inheritance
- One parent, many children
```python
class Animal:
    def move(self):
        print("Moving...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

d = Dog()
d.move()
d.bark()

c = Cat()
c.move()
c.meow()
```

5. Hybrid Inheritance
Hybrid inheritance in Python is when multiple types of inheritance are combined in a single program. It’s like mixing and matching family trees—some classes inherit from one parent, some from two, and some form a chain. It’s a blend of:
- Single inheritance (one parent → one child)
- Multiple inheritance (one child → multiple parents)
- Multilevel inheritance (grandparent → parent → child)
- Hierarchical inheritance (one parent → many children)


# Method Overriding
If the child class wants to change a method from the parent, it can override it.
```python
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self): # Overrides parent's speak
        print("Dog says WOOF!")

pet = Dog()
pet.speak()
```

# Using `super()`
`super()` gives you access to methods from the parent class without using the class name directly.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent's constructor
        self.breed = breed
```