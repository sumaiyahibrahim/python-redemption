## A list is a collection which is ordered and changeable. Allows duplicate members.
## In Python, lists are defined by having values between square brackets [].
## Lists can contain items of different data types, including other lists.

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]  # List of strings

# List with different data types
mixed = [1, "hello", 3.14, True]  # List with int, str, float, and bool

# List with another list (nested)
nested = [1, 2, [3, 4], 5]  # List containing another list at index 2
```

# Lists are mutable, you can change their content after creation.
```python
fruits[1] = "blueberry"  # Changes the item at index 1 to 'blueberry'
```

# Lists are dynamic, they can grow and shrink in size as needed.
```python
fruits.append("orange")      # Adds 'orange' to the end of the list
fruits.remove("apple")       # Removes the first occurrence of 'apple' from the list
fruits.pop()                 # Removes and returns the last item in the list
fruits.insert(1, "kiwi")     # Inserts 'kiwi' at index 1 (shifts others right)
```

# Lists are iterable, you can loop through them using a for loop.
```python
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list one by one
# Output:
# blueberry
# kiwi
# cherry
```

# Lists can be nested, you can have lists within lists.
```python
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3   # Accesses the first element of the second list (index 1) in matrix
```

# Lists can be sliced, you can access a range of items using slicing syntax.
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]   # Slices from index 1 up to (but not including) index 4
print(numbers[:3])     # [0, 1, 2]   # Slices from the start up to (but not including) index 3
print(numbers[::2])    # [0, 2, 4]   # Slices the whole list, taking every 2nd element (step=2)
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0]   # Reverses the list
print(numbers[1::2])   # [1, 3, 5]   # Starts at index 1, takes every 2nd element
print(numbers[2:5])    # [2, 3, 4]   # From index 2 up to (but not including) index 5
print(numbers[-3:])    # [3, 4, 5]   # Last 3 elements
print(numbers[:-2])    # [0, 1, 2, 3]   # All except the last 2 elements
```

# Lists can be concatenated, you can combine two or more lists using the + operator.
```python
a = [1, 2, 3]
b = [4, 5]
combined = a + b      # [1, 2, 3, 4, 5]   # Concatenates lists a and b
```

# Lists can be repeated, you can repeat a list using the * operator.
```python
repeat = [0, 1] * 3   # [0, 1, 0, 1, 0, 1]   # Repeats the list
```

# Lists can be sorted (in-place) and reversed.

```python
# Sorting a list of strings alphabetically
fruits = ["banana", "apple", "cherry"]
fruits.sort()  # Sorts the list alphabetically: ['apple', 'banana', 'cherry']

# Sorting a list of numbers in ascending order
numbers = [3, 1, 4, 2, 5]
numbers.sort()  # Sorts the list: [1, 2, 3, 4, 5]

# Sorting in descending order
numbers.sort(reverse=True)  # [5, 4, 3, 2, 1]

# Reversing a list (in-place)
fruits.reverse()  # Reverses the order: ['cherry', 'banana', 'apple']

# You can also use sorted() to return a new sorted list without changing the original
new_sorted = sorted(numbers)  # Returns a new sorted list

# Reversing with slicing (creates a new reversed list)
reversed_list = numbers[::-1]  # Returns a new
```


