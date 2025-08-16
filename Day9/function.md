# function
A function is a block of code that performs a specific task. You can reuse it whenever you need, instead of writing the same code again.

Syntax :
```python
def function_name(parameters):
    # code block
    return output
```
### Basic Function
```python
def greet():
    print("Welcome to Python ")

greet()  # Calling the function
```

### Function with Parameters
```python
def greet_user(name):
    print(f"Hey {name}, you’re awesome!")

greet_user("Sumaiyah")
```

### Function with Return Value
```python
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum is:", result)
```

### Default Parameters
```python
def welcome(user="Guest"):
    print(f"Welcome back, {user}!")

welcome()         # Uses default
welcome("Zayn")   # Uses given input
```

### Keyword Arguments
```python
def order(food, drink):
    print(f"You ordered {food} and {drink}!")

order(drink="Coke", food="Burger")
```

### Arbitrary Arguments (`*args`)
```python
def total_marks(*marks):
    print("All marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 90, 100)
```
- `*args` lets a function accept any number of positional arguments.
- It collects them into a tuple.
- Great for when you don’t know how many inputs you’ll get.

### Arbitrary Keyword Arguments (`**kwargs`)
```python
def greet_all(**kwargs):
    for name, message in kwargs.items():
        print(f"{name}: {message}")

greet_all(Sara="Hi", Ayan="Hello")
```
 
### Lambda Function (1-line functions)
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

