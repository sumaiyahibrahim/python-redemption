# we can format strings using f-strings, format method, or old-style formatting

# f-strings (recommended, Python 3.6+)
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

# String formatting with f-strings
name = "Bob"
height = 1.75
print(f"{name} is {height:.2f} meters tall.")  # .2f formats float to 2 decimal places

# String formatting with format method
print("Hello, my name is {} and I am {} years old.".format(name, age))

# string formatting with format method
print("The value of pi is approximately {:.3f}.".format(3.14159))  # .3f formats float to 3 decimal places


# formating using index
print("Hello, {0}. You are {1} years old.".format(name, age)) # using positional arguments
print("Hello, {name}. You are {age} years old.".format(name=name, age=age))  # using keyword arguments



# --- str.format() method details ---

# Basic usage:
print('This is a string {}'.format('INSERTED'))  # Output: This is a string INSERTED

# Multiple insertions (positional arguments):
print('The {} {} {}'.format('fox', 'brown', 'quick'))  # Output: The fox brown quick

# Repeating values using indexes:
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))  # Output: The fox fox fox

# Using keyword arguments:
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))  # Output: The fox fox fox

# Mixing positional and keyword arguments:
print('The {0} {b} {q}'.format('fox', b='brown', q='quick'))  # Output: The fox brown quick

# Float formatting with width and precision:
result = 100 / 777
print("The result was {}".format(result))           # Output: The result was 0.1287001287001287
print("The result was {r}".format(r=result))        # Output: The result was 0.1287001287001287
print("The result was {r:1.3f}".format(r=result))   # Output: The result was 0.129
# {value:width.precisionf}
# width = minimum width, precision = number of decimals

# Alignment and padding with format():
print("{:<10} is left aligned.".format(name))       # left aligned, width 10
print("{:>10} is right aligned.".format(name))      # right aligned, width 10
print("{:^10} is center aligned.".format(name))     # center aligned, width 10
print("{:*^10} is center aligned with padding.".format(name))  # * is the padding character