# Comparators

## 1. Basic Comparison Operators

| Operator | Description           | Example           | Result     |
|----------|-----------------------|-------------------|------------|
| `==`     | Equal to              | `5 == 5`          | `True`     |
| `!=`     | Not equal to          | `5 != 3`          | `True`     |
| `>`      | Greater than          | `7 > 4`           | `True`     |
| `<`      | Less than             | `3 < 8`           | `True`     |
| `>=`     | Greater than or equal | `5 >= 5`          | `True`     |
| `<=`     | Less than or equal    | `4 <= 6`          | `True`     |
 
##  The 3 Logical Operators in Python

| Operator | Description            | Example               |
|----------|------------------------|------------------------|
| `and`    | True if **both** are True | `x > 5 and x < 10`     |
| `or`     | True if **at least one** is True | `x < 0 or x > 100` |
| `not`    | Inverts the result     | `not is_logged_in`     |

##  Comparisons with Strings
```python
"a" < "b"        # True (lexicographical order)
"apple" == "Apple"  # False (case-sensitive)
```

# Comparison Chaining
```python
3 < x < 10   # instead of: 3 < x and x < 10
```
### Syntax: Basic Form
```python
a < b < c
a <= b <= c
a > b > c
a != b != c
a == b == c
```
This works because Python evaluates chained comparisons like:
```python
a < b < c  ≡  (a < b) and (b < c)
```
