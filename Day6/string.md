# String
```python
print("Hello world")  # printing in single line
print("Hello \nWorld") # printing in next line
print("Hello \tWorld") # Hello 	 World
```
### len() - to find length of the String
```python
a = "Hello"
print(len(a))
```
## String Indexing & Slicing

###  1. Basic Indexing
```python
s = "Python"
s[0]      # 'P' (first character)
s[5]      # 'n' (last character)
```
### 2. Negative Indexing
```python
s[-1]     # 'n' (last character)
s[-2]     # 'o' (second last)
```

### 3. Basic Slicing
```python
s[0:4]    # 'Pyth' (from index 0 to 3)
s[2:]     # 'thon' (from index 2 to end)
s[:3]     # 'Pyt' (from start to index 2)
```

### 4. Negative Slicing
```python
s[-4:-1]  # 'tho' (from -4 to -2)
s[:-3]    # 'Pyt' (up to third last)
```

### 5. Step Slicing
```python
s[::2]    # 'Pto' (every second character)
s[1::2]   # 'yhn' (start at index 1, step 2)
```

### 6. Reverse String
```python
s[::-1]   # 'nohtyP' (reverse the string)
```

### 7. Slice with Start, Stop, Step
```python
s[1:5:2]  # 'yh' (from index 1 to 4, step 2)
```

### 8. Edge Cases
```python
s[100:]   # '' (out-of-range returns empty string)
s[:100]   # 'Python' (safe slicing)
```

### 9. String Immutability
```python
s[0] = 'J'  # ❌ Error
s = 'J' + s[1:]  # 'Jython'
```