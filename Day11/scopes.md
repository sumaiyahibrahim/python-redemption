 # Scopes
 What is LEGB?

## LEGB stands for:
- L: Local
- E: Enclosing
- G: Global
- B: Built-in
It defines the order in which Python searches for variables when executing code. This order determines which value a variable name refers to.

## Local (L)
- The innermost scope.
- The innermost scope.
```python
x = 10

def my_func():
    x = 5  # Local to my_func
    print(x) 

my_func()  # Output: 5
```

## Enclosing (E)
- The scope of any enclosing function (functions inside functions).
```python
def outer():
    x = 'enclosing'

    def inner():
        print(x)  # Looks in enclosing scope

    inner()

outer()  # Output: enclosing
```

## Global (G)
- Variables defined at the top-level of the script or notebook.
```python
x = 'global'

def func():
    print(x)  # Found in global scope

func()  # Output: global
```

## Built-in (B)
- Python's built-in names like `len`, `range`, `print`, etc.
```python
print(len("Hello"))  # Uses built-in len() function
```

### Example Demonstrating LEGB
```python
x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)

    inner()

outer()  # Output: local
```