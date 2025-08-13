# List Comprehensions
List comprehensions are a shorter, cleaner way to create lists in Python.

Instead of writing a loop like this:
```python
numbers = []
for i in range(5):
    numbers.append(i)
```
You can write it like this:
```python
numbers = [i for i in range(5)]
```

## Basic Syntax
```python
[expression for item in iterable]
```
- **expression** → What you want to do with each item
- **item** → Variable that takes each value
- **iterable** → A list, range, string, etc.

Examples :

### 1️⃣ Make a list of numbers 0–9
```python
nums = [i for i in range(10)]
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 2️⃣ Square of each number in a list
```python
squares = [x**2 for x in range(6)]
# Output: [0, 1, 4, 9, 16, 25]
```

### 3️⃣ Convert a string to a list of characters
```python
chars = [ch for ch in "hello"]
# Output: ['h', 'e', 'l', 'l', 'o']
```

## With Conditionals (Filter Items)
### 4️⃣ Only even numbers from a list
```python
evens = [i for i in range(10) if i % 2 == 0]
# Output: [0, 2, 4, 6, 8]
```

### 5️⃣ Square only if number is odd
```python
odd_squares = [x**2 for x in range(10) if x % 2 != 0]
# Output: [1, 9, 25, 49, 81]
```

## With If-Else (Ternary Style)
### 6️⃣ Even → "Even", Odd → "Odd"
```python
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']
```