# Conditional Statements (`if`, `elif`, `else`)

## `if` Statement
```python
if condition:
    # do something
```
Example :
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## `if-else` Statement
```python
if condition:
    # do something
else:
    # do something else
```
Example :
```python
hungry = True

if hungry:
    print("FEED ME!")
else:
    print("I'm not hungry")
```

---

## `if-elif-else` Statement
```python
if condition1:
    # do something
elif condition2:
    # do something else
else:
    # fallback if none match
```
Example :
```python
temperature = 30

if temperature > 35:
    print("It's too hot!")
elif temperature > 20:
    print("Nice weather")
else:
    print("It's cold")
```