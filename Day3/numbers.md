# Math Operators in Python

## Basic Arithmetic Operators

```python
# Addition
a + b

# Subtraction
a - b

# Multiplication
a * b

# Division (always returns float)
a / b

# Floor Division (returns integer result, discards remainder)
a // b

# Modulus (remainder)
a % b

# Exponentiation (power)
a ** b
```

## Examples

```python
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000
```

## Operator Precedence

- `**` (Exponentiation)
- `*`, `/`, `//`, `%` (Multiplication, Division, Floor Division, Modulus)
- `+`, `-` (Addition, Subtraction)
- Parentheses `()` can be used to change precedence.

## Assignment Operators

```python
x += 2   # x = x + 2
x -= 2   # x = x - 2
x *= 2   # x = x * 2
x /= 2   # x = x / 2
x //= 2  # x = x // 2
x %= 2   # x = x % 2
x **= 2  # x = x ** 2
```

## Useful Math Functions

```python
import math

math.sqrt(16)      # 4.0, square root
math.pow(2, 3)     # 8.0, 2 raised to the power 3
math.ceil(2.3)     # 3, smallest integer >= 2.3 (ceiling)
math.floor(2.7)    # 2, largest integer <= 2.7 (floor)
abs(-5)            # 5, absolute value (removes sign)
round(3.14159, 2)  # 3.14
```

## Notes

- Division `/` always returns a float, even if the result is a whole number.
- Use `//` for integer division.
- Use `math` module for advanced mathematical functions.