# lambda expression
- A lambda function is a **small, anonymous function** (i.e., it doesn't have a name).
- It's used when you need a short function for a short period — especially useful inside functions like map(), filter(), reduce(), etc.

## Syntax:
```python
lambda arguments: expression
```

### Example:
```python
square = lambda x: x**2
print(square(4))  # Output: 16
```
Its equivalent to:
```python
def square_fn(x):
    return x**2
```

### Use Case 1: Using lambda with map()
```python
# map(func, iterable) applies the function to all items
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16]
```

### Use Case 2: Using lambda with filter()
```python
# filter(func, iterable) returns items where function returns True
names = ['Sam', 'Andy', 'Sally']
s_only = list(filter(lambda x: x.startswith('S'), names))
print(s_only)  # Output: ['Sam', 'Sally']
```

### Use Case 3: Using lambda with reduce()
```python
# reduce(func, iterable) applies rolling computation to items
from functools import reduce
sum_all = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sum_all)  # Output: 10
```

### Use Case 4: Sorting with custom keys using lambda
```python
people = [('Sam', 25), ('Alice', 30), ('Bob', 22)]
people_sorted = sorted(people, key=lambda x: x[1])
print(people_sorted)  # Output: [('Bob', 22), ('Sam', 25), ('Alice', 30)]
```

### Use Case 5: Nested lambdas
```python
# When one lambda returns another (advanced use)
add = lambda x: lambda y: x + y
add5 = add(5)
print(add5(3))  # Output: 8
```
