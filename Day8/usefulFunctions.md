### List Constructor – `list()`
Converts iterables like strings, tuples, or ranges into a list.
```python
my_str = "hello"
print(list(my_str))  # ['h', 'e', 'l', 'l', 'o']

my_tuple = (1, 2, 3)
print(list(my_tuple))  # [1, 2, 3]

print(list(range(5)))  # [0, 1, 2, 3, 4]
```

### `enumerate()` – Track Index + Item
Use `enumerate()` when you need both the index and value in a loop.
```python
fruits = ['apple', 'banana', 'mango']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
enumerate() returns (index, value) pairs

### `zip()` – Combine Multiple Iterables
Pairs up elements from two or more iterables (lists, tuples, etc.)
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [90, 80, 85]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

### `in` Keyword – Check Existence
Use `in` to check if an item exists in a list, string, tuple, etc.
```python
nums = [1, 2, 3, 4]

print(3 in nums)     # True  
print(10 in nums)    # False  
print('a' in 'apple')  # True
```

### `random.shuffle()` – Shuffle a List In-Place
```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print(my_list)  # Order will be randomized
```
It shuffles the list in-place, doesn't return a new one

### `random.randint(a, b)` – Random Integer
Returns a random integer between `a` and `b` (both inclusive)
```python
import random

num = random.randint(1, 100)
print(f"Random number: {num}")
```