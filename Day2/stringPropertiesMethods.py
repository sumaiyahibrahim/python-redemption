# Text Type: str
# - Strings are sequences of Unicode characters, defined with single (' '), double (" "), or triple quotes (''' ''' or """ """)
# - Strings are immutable (cannot be changed after creation)
# - Can be indexed and sliced: s[0], s[1:4], s[-1], etc.
# - Supports concatenation (+), repetition (*), and membership (in) operations

# Concatenation:
s1: str = "Hello"
s2: str = "World"
result: str = s1 + " " + s2  # 'Hello World'

# Multiplying (repetition):
repeat: str = "ha" * 3       # 'hahaha'

# Membership:
# The 'in' and 'not in' operators check if a substring exists within a string.
# Returns True if the substring is found, otherwise False.
exists: bool = "e" in "hello"    # True, because 'e' is in "hello"
not_exists: bool = "z" not in "hello"  # True, because 'z' is not in "hello"

# Typecasting to string:
num: int = 42
num_str: str = str(num)      # '42'
flt: float = 3.14
flt_str: str = str(flt)      # '3.14'
lst: list = [1, 2, 3]
lst_str: str = str(lst)      # '[1, 2, 3]'

# Typecasting from string (if possible):
s_int: int = int("123")      # 123
s_float: float = float("3.14") # 3.14

# Common string methods with examples and their return types:

# s.lower()      # returns lowercase version (str)
example: str = "Hello".lower()        # 'hello'

# s.upper()      # returns uppercase version (str)
example: str = "Hello".upper()        # 'HELLO'

# s.title()      # capitalizes each word (str)
example: str = "hello world".title()  # 'Hello World'

# s.capitalize() # capitalizes first character (str)
example: str = "hello".capitalize()   # 'Hello'

# s.strip()      # removes leading/trailing whitespace (str)
example: str = "  hello  ".strip()    # 'hello'

# s.replace(old, new) # replaces substring (str)
example: str = "hello world".replace("world", "Python")  # 'hello Python'

# s.split(sep)   # splits string into list (list[str])
example: list = "a,b,c".split(",")     # ['a', 'b', 'c']
example: list = "a b c".split()        # ['a', 'b', 'c']

# s.rsplit(sep)  # splits from the right (list[str])
example: list = "a,b,c".rsplit(",", 1) # ['a,b', 'c']

# s.partition(sep)   # splits into 3 parts: before, sep, after (tuple[str, str, str])
example: tuple = "key:value".partition(":")  # ('key', ':', 'value')

# s.rpartition(sep)  # splits into 3 parts: before, sep, after (tuple[str, str, str])
example: tuple = "key:value:again".rpartition(":")  # ('key:value', ':', 'again')

# s.splitlines()     # splits string at line breaks into a list (list[str])
example: list = "a\nb\nc".splitlines()  # ['a', 'b', 'c']

# s.join(list)   # joins list of strings into one string, using s as separator (str)
example: str = "-".join(['a', 'b', 'c'])  # 'a-b-c'

# More useful string methods with examples and their return types:

# s.isalpha()    # True if all characters are alphabetic (bool)
example: bool = "abc".isalpha()         # True

# s.isdigit()    # True if all characters are digits (bool)
example: bool = "123".isdigit()         # True

# s.isalnum()    # True if all characters are alphanumeric (bool)
example: bool = "abc123".isalnum()      # True

# s.isspace()    # True if all characters are whitespace (bool)
example: bool = "   ".isspace()         # True

# s.islower()    # True if all characters are lowercase (bool)
example: bool = "abc".islower()         # True

# s.isupper()    # True if all characters are uppercase (bool)
example: bool = "ABC".isupper()         # True

# s.zfill(width) # pads string on the left with zeros to fill width (str)
example: str = "42".zfill(5)           # '00042'

# s.center(width, fillchar) # centers string, pads with fillchar (str)
example: str = "hi".center(6, "*")     # '**hi**'

# Escape characters:
# \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote)

# String formatting:
# f"Hello {name}"   # f-strings (recommended, Python 3.6+)
# "Hello {}".format(name) # format method
# "Hello %s" % name      # old-style formatting

# Example:
# s = " Hello, World! "
# print(s.strip().upper())  # Output: HELLO, WORLD!

# Note: The most commonly used string methods and properties are listed above.
# Python's str type has many more methods. Here are additional ones for completeness:

# s.casefold()         # aggressive lowercasing for caseless matching (str)
# s.encode(encoding)   # returns encoded bytes of string (bytes)
# s.endswith(suffix)   # True if string ends with suffix (bool)
# s.expandtabs(tabsize)# replaces tabs with spaces (str)
# s.format(*args, **kwargs) # advanced string formatting (str)
# s.format_map(mapping)     # formatting with a mapping object (str)
# s.index(sub)        # like find(), but raises ValueError if not found (int)
# s.ljust(width, fillchar)  # left-justifies string (str)
# s.rjust(width, fillchar)  # right-justifies string (str)
# s.lstrip()          # removes leading whitespace (str)
# s.rstrip()          # removes trailing whitespace (str)
# s.maketrans(x, y)   # static method for translation tables (dict)
# s.translate(table)  # returns translated string (str)
# s.removeprefix(prefix) # removes prefix if present (str, Python 3.9+)
# s.removesuffix(suffix) # removes suffix if present (str, Python 3.9+)
# s.swapcase()        # swaps case of all letters (str)
# s.rfind(sub)        # highest index of substring, -1 if not found (int)
# s.rindex(sub)       # like rfind(), but raises ValueError if not found (int)

# Properties:
# Strings are immutable sequences of Unicode characters.
# Can be iterated, indexed, and sliced.
# Support for comparison operators (==, !=, <, >, etc.).
# Support for membership test ('a' in s).

# For full reference, see: https://docs.python.org/3/library/stdtypes.html#string-methods
