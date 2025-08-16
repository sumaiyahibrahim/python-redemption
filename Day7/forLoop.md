#  `for` Loop
#### The `for` loop is used to **iterate** over sequences like lists, strings, tuples, sets, and more.
---
## Basic Syntax
```python 
for variable in iterable:
    # do something with variable
```
**variable**: each item from the iterable is assigned to this.

**iterable**: a sequence like a list, string, etc.

## Looping Over a List
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
## `for` Loop Over a List
```python
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print('hello')
```

## Loop Over a String
```python
for char in "hello":
    print(char)
```

## Loop Using `range()`
```python
for i in range(5):
    print(i)
# if you want to loop Horizontally : print(i,end=' ')
```

## Custom Range
```python
for i in range(1, 10, 2):  # start, stop, step
    print(i)
```

## Loop with `else`
```python
for i in range(3):
    print(i)
else:
    print("Loop finished")
```
- Python allows an else block after a for loop
- The else runs only if the loop isn't broken by break.
- return False inside the loop causes the function to exit too early — it doesn't check all elements.

## Breaking a Loop Early
```python
for x in range(10):
    if x == 5:
        break
    print(x)
```
- `break` → exits the loop completely.

## Skipping Iterations with continue
```python
for x in range(5):
    if x == 2:
        continue
    print(x)
```
- `continue` → skips just one iteration and moves to the next.

## Nested `for` Loops
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

## Indexing Loop using `range(len(list))`
```python
fruits = ['apple', 'banana', 'cherry']

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

## Loop Over `dict.items()` → Keys + Values
```python
person = {'name': 'Sumaiyah', 'age': 20, 'role': 'Developer'}

for key, value in person.items():
    print(f"{key} → {value}")
```

## another looping for dictionary
```python
d={'k1':1,'k2':2,'k3':3}
for key,val in d.values():
    print(val)
```

## using tuple
```python
mylist=[(1,2)(3,4)(5,6)(7,8)]
for item in mylist:
    print(item)
```

## another tuple 
```python
mylist = [(1,2), (3,4), (5,6), (7,8)]
for a, b in mylist:
    print(a)
```

## Use `enumerate()` → Index + Item in One Go
```python
fruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
```