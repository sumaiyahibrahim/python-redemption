# Dunder methods (Double underscore methods)

## Object Construction & Initialization
| Method         | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `__new__(cls)` | Creates a new instance (rarely needed unless doing metaprogramming)     |
| `__init__(self, ...)` | Initializes the object (constructor)                              |
| `__del__(self)` | Destructor, called when object is deleted ( usually avoid using it)   |

## String / Representation
| Method              | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `__str__(self)`     | Called by `print()` and `str()` — user-friendly string                  |
| `__repr__(self)`    | Called by `repr()` or typing object in console — debug string           |
| `__format__(self, format_spec)` | Supports custom formatting (e.g. `"{:>10}".format(obj)`)     |
| `__bytes__(self)`   | Defines behavior for `bytes(obj)`                                       |
| `__bool__(self)`    | Called for `bool(obj)` (default is `True` unless `__len__()` returns 0) |

## Math & Arithmetic Operators
| Method               | Triggered By... | Use Case                      |
|----------------------|------------------|-------------------------------|
| `__add__(self, other)`     | `+`              | Add objects                  |
| `__sub__(self, other)`     | `-`              | Subtract                     |
| `__mul__(self, other)`     | `*`              | Multiply                     |
| `__truediv__(self, other)` | `/`              | True division                |
| `__floordiv__(self, other)`| `//`             | Floor division               |
| `__mod__(self, other)`     | `%`              | Modulus                      |
| `__pow__(self, other)`     | `**`             | Power                        |
| `__divmod__(self, other)`  | `divmod()`       | Tuple of `(a//b, a%b)`       |


## Comparison Operators
| Method     | Used For... |
|------------|-------------|
| `__eq__`   | `==`         |
| `__ne__`   | `!=`         |
| `__lt__`   | `<`          |
| `__le__`   | `<=`         |
| `__gt__`   | `>`          |
| `__ge__`   | `>=`         |


## Unary Operators
| Method       | Use Case     |
|--------------|--------------|
| `__neg__`    | `-obj`       |
| `__pos__`    | `+obj`       |
| `__abs__`    | `abs(obj)`   |
| `__invert__` | `~obj`       |

## Container / Sequence Behavior
| Method         | Use Case             |
|----------------|----------------------|
| `__len__`      | `len(obj)`           |
| `__getitem__`  | `obj[key]`           |
| `__setitem__`  | `obj[key] = value`   |
| `__delitem__`  | `del obj[key]`       |
| `__contains__` | `x in obj`           |
| `__iter__`     | Start of a `for` loop|
| `__next__`     | Next value in iteration |
| `__reversed__` | `reversed(obj)`      |


## Examples:
1. `__len__()` – Length of Object
lets your object work with len()
```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(420)
print(len(b))
```

2. `__add__()` – Add Objects with `+`
customize how `+` works for your class
```python
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

w1 = Wallet(100)
w2 = Wallet(50)
w3 = w1 + w2  # Calls __add__()
print(w3.amount)  # 150
```

5. __eq__() - Equality check
how to check == between objects
```python
class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

cat1 = Cat("Luna")
cat2 = Cat("Luna")
print(cat1 == cat2)  # True
```