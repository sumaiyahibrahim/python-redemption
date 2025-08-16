# 📝 Day 1 Notes – Python Basics

## 🖨️ 1. Printing in Python

```python
print("Hello World") 
```
- Outputs text to the console
- Use `\n` for new lines
- You can concatenate strings using `+`:

```python
print("Hello" + " World")
```
- You can print multiple items separated by commas (adds spaces automatically):

```python
print("Hello", "World")
```
- Use `end` and `sep` parameters to control output:

```python
print("Hello", end="!")  # No newline, ends with !
print("A", "B", sep="-") # Output: A-B
```

---

## ✍️ 2. String Manipulation

```python
print("Hello\nWorld")     # Line break
print("Hello" + " " + "Python")
```
- Use `+` to join strings manually
- Escape quotes using `\"` inside a string
- Strings are **immutable** (cannot be changed after creation)
- Use `len()` to get string length:

```python
print(len("Python"))  # Output: 6
```
- Use **f-strings** for easier formatting (Python 3.6+):

```python
name = "Alice"
print(f"Hello, {name}!")
```
- Common string methods: `.lower()`, `.upper()`, `.title()`, `.strip()`, `.replace()`

---

## 🐍 3. Variables

```python
name = "Alice"
age = 25
```
- Variables store data
- Python is **dynamically typed** – no need to declare type
- Variable names are **case-sensitive** (`Name` ≠ `name`)
- You can reassign variables to different types:

```python
x = 5
x = "now a string"
```
- Use `type()` to check a variable's type:

```python
print(type(age))  # Output: <class 'int'>
```
- Naming convention: use `snake_case` for variable names

---

## 🔤 4. Input Function

```python
name = input("What is your name? ")
print("Hello, " + name)
```
- `input()` always returns a **string**
- Use `input()` to interact with the user
- Convert input to other types if needed:

```python
age = int(input("Enter your age: "))
```
- Always provide a clear prompt in `input()`
- Be careful with type conversion; invalid input causes errors

---

## 🧠 5. Variable Naming Rules

- Must begin with a letter or `_`
- Cannot start with a number
- Cannot use Python keywords like `input`, `print`, `if`, etc.

✅ Good:
```python
user_name = "Sam"
total_score = 99
```

❌ Bad:
```python
1st_place = "Winner"   # Invalid
print = "something"    # Overwrites built-in
```


---

##  Day Project – Band Name Generator

```python
city = input("Which city did you grow up in?\n")
pet = input("What is your pet's name?\n")
print("Your band name could be " + city + " " + pet)
```