# Functions and Tuple Unpacking
```python
stockPrice=[('APPL',200),('GOOG',200),('MSFT',200)]
for item in stockPrice:
    print(item)

# output:
# ('APPL', 200)
# ('GOOG', 200)
# ('MSFT', 200)
```

### Unpacking Tuples
```python
stockPrice=[('APPL',200),('GOOG',200),('MSFT',200)]
for ticker,price in stockPrice:
    print(ticker)

# output:
# APPL
# GOOG
# MSFT
```

### Printing Both Values
```python
for ticker, price in stockPrice:
    print(f"{ticker} stock is priced at ${price}")

# output:
# APPL stock is priced at $200
# GOOG stock is priced at $200
# MSFT stock is priced at $200
```

# Unpacking the result in Function
```python
def get_student_info():
    name = "Sumaiyah"
    age = 20
    return name, age  # returns a tuple ('Sumaiyah', 20)
# Unpacking the result
student_name, student_age = get_student_info()

print(student_name)  # Sumaiyah
print(student_age)   # 20
```
- return name, age → returns a tuple
- student_name, student_age = get_student_info() → unpacks the tuple