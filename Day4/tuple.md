# Tuple Properties in Python

- Tuples are ordered collections of items.
- Tuples are immutable (cannot be changed after creation).
- Tuples allow duplicate values.
- Tuples can contain items of different data types (int, str, float, etc.).
- Tuples are defined using parentheses `()` or without any brackets for multiple items separated by commas.
- Tuples support indexing and slicing (like lists).
- Tuples can be nested (contain other tuples, lists, etc.).
- Tuples are iterable (can be used in loops).
- Tuples use less memory and are faster than lists for read-only data.
- Tuples can be used as dictionary keys (if all elements are immutable).

```python
# Creating tuples
t1 = (1, 2, 3)
t2 = 4, 5, 6
t3 = ("apple", 3.14, True)
t4 = (1,)  # Single-element tuple (note the comma)
```

```python
# Accessing elements
print(t1[0])      # 1
print(t1[-1])     # 3
print(t1[1:3])    # (2, 3)
```

```python
# Nested tuple 
nested = (1, (2, 3), [4, 5])
```

```python
# Tuple unpacking
a, b, c = t1  # a=1, b=2, c=3
```


```python
# count(value) 
t = (1, 2, 2, 3, 4, 2)
print(t.count(2))  # 3
print(t.count(5))  # 0
#Returns how many times a value appears in the tuple.
```
```python
# index(value[, start[, end]])
t = (10, 20, 30, 20, 40)

print(t.index(20))        # 1
print(t.index(20, 2))     # 3

# print(t.index(50))      # ValueError: 50 is not in tuple
```
