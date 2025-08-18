# Validating user input

## Why Validate?
users can enter:
- wrong data types
- blank fields
- unexpected characters

## Tools for validation:
- `.isdigit()`, `.isalpha()`, `.isalnum()`
- `try/except` blocks
- `while` loops for retrying
- Logical conditions (`if`, `and`, `or`)

Examples :
1. Check for number input:
```python
num = input("Enter a number: ")
if num.isdigit():
    print("Valid number")
else:
    print("Not a number")
```

2. Retry until valid input:
```python
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    print("Invalid input! Try again.")
```

3. Try-except for type-safe conversion:
```python
try:
    marks = int(input("Enter marks: "))
except ValueError:
    print("Only numbers allowed!")
```

4. Validate names (no numbers/symbols):
```python
name = input("Enter your name: ")
if name.replace(" ", "").isalpha():
    print("Valid name")
else:
    print("Invalid name. Only letters allowed.")
```

5. Range checking:
```python
age = int(input("Enter age (1-120): "))
if 1 <= age <= 120:
    print("Valid age")
else:
    print("Age out of range")
```