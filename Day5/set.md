#  Python Sets

Python sets are **unordered collections of unique elements**. They’re great for storing non-duplicate items and performing set operations like union, intersection, etc.

---

## Properties

- Defined using curly braces `{}` or `set()` constructor.
- No duplicates allowed.
- Items are unordered and unindexed.
- Sets are mutable (you can add/remove elements).
- Elements must be **immutable** (no lists/dictionaries inside).

```python
myset = {"apple", "banana", "cherry"}
print(myset)  # Output order is not guaranteed
```

### copy(), Returns a shallow copy of the set
```python
original = {10, 20, 30}
copy_set = original.copy()
print(copy_set)  # {10, 20, 30}
print(original is copy_set)  # False (they are different objects)
```

## To create empty set, use set()
```python
empty_set = set()  # Not {}
```

## Access Set Items
### You cannot access items by index, but you can loop through a set:

```python 
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```

### To check if an item exists:

```python 
print("banana" in fruits)    # True
print("grape" not in fruits) # True
```
## Add Set Items
### add(): Add a single item
```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
```

### update(): Add multiple items (from any iterable)
```python
fruits.update(["orange", "grape"])
print(fruits)
```

## Remove Set Items
### remove(): Removes item (raises error if not found)
```python
fruits.remove("banana")
```

### discard(): Removes item (no error if not found)
```python
fruits.discard("kiwi")  # Safe even if "kiwi" not in set
```

### pop(): Removes a random item
```python
item = fruits.pop()
print("Removed:", item)
```

### clear(): Empties the set
```python
fruits.clear()
```

### del: Deletes the set entirely
```python
del fruits
```

## Loop Sets
```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

## You can also convert a set to a list to use indexing:
```python
color_list = list(colors)
print(color_list[0])
```

## Join Sets
### union(): Combine sets (returns new set)
```python
a = {"a", "b", "c"}
b = {1, 2, 3}
result = a.union(b)
print(result)
```

### update(): Add items from another set (modifies original)
```python
a.update(b)
print(a)
```

## Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}
```
### Union
```python
print(a | b)              # {1, 2, 3, 4, 5}
```
### Intersection
```python
print(a & b)              # {3}
```
### Difference
```python
print(a - b)              # {1, 2}
```
### Symmetric Difference
```python
print(a ^ b)              # {1, 2, 4, 5}
```