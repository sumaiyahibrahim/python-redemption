# Booleans

In Python, **Booleans** represent one of two values:  
- `True`  
- `False`

They are used to perform **logical operations**, control flow (like `if` statements), and evaluate expressions.

---
 
## Boolean Values

```python
x = True
y = False

print(type(x))  # <class 'bool'>
```
---
## Boolean as Result of Comparison
```python
print(10 > 5)      # True
print(3 == 3)      # True
print(4 < 2)       # False
```

## Boolean in Conditions
```python
a = 100
b = 200

if b > a:
    print("b is greater than a")  # This will print
```

## bool() Function, ou can convert values into booleans using bool().
```python
print(bool("Hello"))  # True
print(bool(15))       # True
print(bool([]))       # False (empty list)
print(bool(""))       # False (empty string)
print(bool(0))        # False
```

## Common Values That Are False in Python
-None
-False
-0
-"" (empty string)
-[] (empty list)
-{} (empty dict)
-() (empty tuple)
-set() (empty set)

Everything else is considered True.

## Boolean Operators
### and - True if both True
### or - True if one true
### not - Inverts value
```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```