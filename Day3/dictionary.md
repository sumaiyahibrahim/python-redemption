# Python Dictionary

## What is a Dictionary?

A **dictionary** in Python is an unordered collection of key-value pairs. Each key is unique and maps to a value.

```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
```

## Key Features

- **Mutable**: Can be changed after creation.
- **Unordered** (Python 3.6+ maintains insertion order).
- **Keys** must be immutable (e.g., strings, numbers, tuples).

---

## Access Items

```python
person = {"name": "Bob", "age": 30}
print(person["name"])      # Bob
print(person.get("age"))   # 30
# The difference:
# - person["name"] uses square brackets to directly access the value for the key "name". 
#   If the key does not exist, it raises a KeyError.
# - person.get("age") uses the get() method (with parentheses) to access the value for the key "age".
#   If the key does not exist, it returns None (or a default value if provided), and does NOT raise an error.
```

---

## Change Items

```python
person["age"] = 31
person["city"] = "London"
```
- Assign a new value to an existing key to change it.
- If the key does not exist, it will be added.

---

## Add Items

```python
person["country"] = "UK"  # Adds a new key-value pair
```
- Assigning a value to a new key adds it to the dictionary.

---

## Remove Items

```python
del person["city"]           # Removes the key 'city'
age = person.pop("age")      # Removes 'age' and returns its value
person.clear()               # Removes all items
```
- Use `del` to remove a key, `pop()` to remove and get the value, `clear()` to empty the dictionary.

---

## Loop Dictionaries

```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```
- Loop through keys or key-value pairs using `.items()`.

---

## Copy Dictionaries

```python
person_copy = person.copy()
# or
person_copy = dict(person)
```
- Use `.copy()` or `dict()` to make a shallow copy of a dictionary.

---

## Nested Dictionaries

```python
students = {
    "Alice": {"age": 25, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
print(students["Alice"]["grade"])  # 'A'
```
- Dictionaries can contain other dictionaries as values.

---

## Dictionary Methods

| Method           | Description                        | Example                                      |
|------------------|------------------------------------|----------------------------------------------|
| `keys()`         | Returns all keys                   | `d.keys()`                                   |
| `values()`       | Returns all values                 | `d.values()`                                 |
| `items()`        | Returns key-value pairs            | `d.items()`                                  |
| `update()`       | Updates dictionary with another    | `d.update({'k4': 400})`                      |
| `get(key, val)`  | Gets value, returns val if missing | `d.get('k1', 'default')`                     |

---

## More Dictionary Methods with Examples

| Method         | Description                                                                 | Example                                                      |
|----------------|-----------------------------------------------------------------------------|--------------------------------------------------------------|
| `clear()`      | Removes all the elements from the dictionary                                | `d.clear()`                                                  |
| `copy()`       | Returns a shallow copy of the dictionary                                    | `d2 = d.copy()`                                              |
| `fromkeys()`   | Returns a new dictionary with specified keys and a single value             | `dict.fromkeys(['a', 'b'], 0)`                              |
| `get()`        | Returns the value of the specified key                                      | `d.get('k1')`                                                |
| `items()`      | Returns a view object with key-value tuple pairs                            | `d.items()`                                                  |
| `keys()`       | Returns a view object with all keys                                         | `d.keys()`                                                   |
| `pop()`        | Removes the element with the specified key and returns its value            | `d.pop('k1')`                                                |
| `popitem()`    | Removes and returns the last inserted key-value pair as a tuple             | `d.popitem()`                                                |
| `setdefault()` | Returns the value of the key. If not present, inserts key with given value  | `d.setdefault('k4', 400)`                                    |
| `update()`     | Updates the dictionary with specified key-value pairs or another dictionary | `d.update({'k4': 400})`                                      |
| `values()`     | Returns a view object with all values                                       | `d.values()`                                                 |

### Examples

```python
d = {'k1': 100, 'k2': 200}

# clear()
d.clear()
print(d)  # {}

# copy()
d1 = {'a': 1, 'b': 2}
d2 = d1.copy()
print(d2)  # {'a': 1, 'b': 2}

# fromkeys()
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'x': 0, 'y': 0, 'z': 0}

# get()
d = {'k1': 123}
print(d.get('k1'))      # 123
print(d.get('missing')) # None

# items()
print(d.items())        # dict_items([('k1', 123)])

# keys()
print(d.keys())         # dict_keys(['k1'])

# pop()
d = {'k1': 1, 'k2': 2}
val = d.pop('k1')
print(val)  # 1
print(d)    # {'k2': 2}

# popitem()
d = {'a': 10, 'b': 20}
item = d.popitem()
print(item) # ('b', 20) (removes last inserted item)
print(d)    # {'a': 10}

# setdefault()
d = {'k1': 1}
val = d.setdefault('k2', 99)
print(val)  # 99
print(d)    # {'k1': 1, 'k2': 99}

# update()
d.update({'k3': 3})
print(d)    # {'k1': 1, 'k2': 99, 'k3': 3}

# values()
print(d.values())       # dict_values([1, 99, 3])
```

---

## Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Example: Dictionary Lookup

```python
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])  # 2.99
```
- You can use square brackets to look up the value for a key in a dictionary.
- If the key does not exist, a `KeyError` will be raised.

---

## Example: Dictionary with Nested Structures

```python
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 1003}}
print(d['k2'])           # [0, 1, 2]   # Accesses the list stored at key 'k2'
print(d['k3']['insideKey'])  # 1003    # Accesses the value inside the nested dictionary
```
- Dictionaries can store lists, other dictionaries, or any data type as values.
- You can access nested data by chaining keys and indexes.

---

## Example: Adding New Key-Value Pairs

```python
d = {'k1': 100, 'k2': 200}
d['k3'] = 300  # Adds a new key 'k3' with value 300
print(d)
# Output: {'k1': 100, 'k2': 200, 'k3': 300}
```
- You can add new key-value pairs to a dictionary by assigning a value to a new key using square brackets.

---

## Example: Updating Values and Viewing Keys/Values

```python
d = {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
print(d)  # {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

# Getting all keys
print(d.keys())    # dict_keys(['k1', 'k2', 'k3'])

# Getting all values
print(d.values())  # dict_values(['NEW VALUE', 200, 300])
```
- `dict.keys()` returns a view of all keys in the dictionary.
- `dict.values()` returns a view of all values in the dictionary.

---

## Example: Using items() to Get Key-Value Pairs

```python
d = {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
print(d.items())  # dict_items([('k1', 'NEW VALUE'), ('k2', 200), ('k3', 300)])
```
- `dict.items()` returns a view object displaying a list of dictionary's key-value tuple pairs.
- Useful for iterating over both keys and values in a loop:
  ```python
  for key, value in d.items():
      print(key, value)
  ```

---

## Useful Tips

- Keys must be unique and immutable.
- Values can be any data type.
- Use `in` to check if a key exists: `"name" in person"`
