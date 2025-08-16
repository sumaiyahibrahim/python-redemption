# `filter()`
- Takes a function + a sequence (like a list)
- Returns only the elements that pass a condition (return True)

## Syntax:
```python
filter(function, iterable)
``` 

### Example: Filter even numbers
```python
def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, nums))
print(result)  # [2, 4, 6]
```

### Example: Filter names that start with 'S'
```python
def starts_with_s(name):
    return name.startswith('S')

names = ["Sam", "Andy", "Sarah", "Bob"]
filtered_names = list(filter(starts_with_s, names))
print(filtered_names)  # Output: ['Sam', 'Sarah']
```

### Example: Filter strings longer than 3 characters
```python
def is_long(word):
    return len(word) > 3

words = ['hi', 'hello', 'yo', 'world']
long_words = list(filter(is_long, words))
print(long_words)  # Output: ['hello', 'world']
```