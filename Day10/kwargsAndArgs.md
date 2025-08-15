# `args`
### Normal Function Arguments (args)
These are fixed parameters—you must pass the exact number of values defined in the function.

Example:
```python
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
```
- You MUST pass 2 values.
- If you pass more or fewer, you'll get an error.

### Arbitrary Positional Arguments (`*args`)
`*args` allows you to pass any number of positional arguments to a function. It packs them into a tuple.

Example:
```python
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40, 60, 100, 100, 3, 4)) 
```
- Use `*args` when you don’t know how many inputs a user might provide.
- Inside the function, `args` is just a tuple → you can loop through it, use `sum()`, etc.
- `*args` is just a convention – you can name it anything you like (e.g., `*numbers`, `*inputs`, `*sumaiyah`) as long as it has the `*` before it.

#### Behind the Scenes:
```python
def show_args(*args):
    print(args)

show_args(10, 20, 30)
# Output: (10, 20, 30)  ← tuple of arguments
```

# `**kwargs`
- `**kwargs` collects named arguments as a dict
- You can use `kwargs['key']` to access specific values
- You can check if a key exists: `'fruit' in kwargs`
- Just like *args, the name kwargs is a convention – you can rename it to anything

Example:
### Basic `**kwargs`
```python
def greet_user(**kwargs):
    print(kwargs)

greet_user(name="Sumaiyah", age=21)
# output: {'name': 'Sumaiyah', 'age': 21}
```

### Accessing Specific Keys
```python
def describe_pet(**kwargs):
    if 'animal' in kwargs:
        print(f"I have a {kwargs['animal']}")
    else:
        print("I don't know what animal you have 😅")

describe_pet(animal='dog', name='Rex')
# output: I have a dog
```

# Looping Through `**kwargs`
```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_details(name='Sumaiyah', skill='AI', mood='🔥')
# output
# name = Sumaiyah
# skill = AI
# mood = 🔥
```

# Combining `*args` and `**kwargs`
```python
def combo_func(*args, **kwargs): 
    print("Positional:", args)
    print("Keyword:", kwargs)

combo_func(1, 2, 3, name='Sumaiyah', goal='ML Engineer')
# output
# Positional: (1, 2, 3)
# Keyword: {'name': 'Sumaiyah', 'goal': 'ML Engineer'}
```
- `*args` must always come before `**kwargs`

Another Example:
```python
def desc_breakfast(*args,**kwargs):
    print("args:",args) # tuple
    print("kwargs:",kwargs) # dict

    if 'drink' in kwargs and 'fruit' in kwargs:
        print(f"I had {'and'.join(args)} for breakfast.") 
        print(f"My drink was {kwargs['drink']} and my fruit was {kwargs['fruit']}.") 
desc_breakfast('pancakes', 'bacon', drink='coffee', fruit='banana') 
```

###  Quick notes:
- always `*args` first then `**kwargs`
- `*args` returns tuple
- `**kwargs` returns dictionary
- Always use f-strings when inserting variables
- must use quotes while accessing kwargs 
- while calling function positional arguments (`*args`) must come BEFORE keyword arguments (`**kwargs`)