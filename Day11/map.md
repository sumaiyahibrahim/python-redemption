# `map()`
`map()` is a built-in function that lets you apply a function to every item in a list (or any iterable)

### Syntax:
```python
map(function, iterable)
```
### Example: Squaring Numbers
```python
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
list=list((map(square,my_nums)))
print(list)
```
### Example: Converting Strings to Integers
```python
str_nums = ['1', '2', '3']
int_nums = list(map(int, str_nums))
print(int_nums)  # [1, 2, 3]
```

### Example: Uppercase All Strings
```python
words = ['sumaiyah', 'loves', 'ai']
uppercased = list(map(str.upper, words))
print(uppercased)  # ['SUMAIYAH', 'LOVES', 'AI']
```

### Example: With Your Own Function
```python
def double(n):
    return n * 2

nums = [5, 10, 15]
doubled = list(map(double, nums))
print(doubled)  # [10, 20, 30]
```

### Example: Find Length of Each String
```python
words = ['hi', 'hello']
lengths = list(map(len, words))
print(lengths)  # Output: [2, 5]
```

### Example:
```python
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]
result = list(map(splicer, names))
print(result)  # Output: ['EVEN', 'E', 'S']
```