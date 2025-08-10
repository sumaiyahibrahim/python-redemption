# File handling
## Creating an Empty File
```python
with open('myfile.txt', 'w') as f:
    pass
```
or
```python
open('myfile.txt', 'w').close()
```

## Writing to a file
```python
with open('myfile.txt', 'w') as f:
    f.write("Hello this is a text file\n")
    f.write("this is the second line\n")
    f.write("this is the third line\n")
# Overwrites everything if file already exists
# Creates the file if it doesn’t exist
```

## Reading from a file
```python
with open('myfile.txt', 'r') as f:
    content = f.read()
    print("File content:")
    print(content)
# Read the whole file as one big string
```
## Reading Line by Line
```python
with open("myfile.txt", "r") as f:
    for line in f:
        print(line.strip())
# Read file line by line (good for loops!)
```

## Appending to Files
```python
with open("myfile.txt", "a") as f:
    f.write("This is an extra line\n")
# 'a' mode = append
# Adds content to the end of file
# Doesn’t delete previous content
```

```python
'r' - Read
'w' - Write
'a' - Append
'r+' - Read + Write
'w+' - Write + Read (overwrites)
'a+' - Append + Read
'x' - Exclusive creation (error if exists)
'b' - Binary mode (e.g. images, videos)
```