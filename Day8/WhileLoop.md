# `while` Loops

A while loop is used to repeat a block of code as long as a given condition is True.
It keeps checking the condition before each iteration.

Syntax : 
```python
while condition:
    # code block to run
```
Example :
```python
x = 1
while x <= 5:
    print(f"x is: {x}")
    x += 1
```

### Infinite Loop (be careful!)
```python
x = 1
while x <= 5:
    print("Oops! This never ends...")
```
This will keep printing forever, because x never changes.
To stop such loops, you must update the condition inside the loop — like x += 1.

### Using `break` in a `while` Loop
`break` lets you **exit** a loop **early**, even if the condition is still `True`.

```python
x = 1
while x <= 10:
    print(x)
    if x == 5:
        break
    x += 1
```
Loop stopped before reaching 10, because break was triggered when x was 5.

### Skipping with `continue`
`continue` lets you **skip the rest** of the loop body and jump to the next iteration.
```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(f"x is: {x}")
```
When x == 3, the print() is skipped.

### `while...else` Loop
The `else` block runs only if the `while` loop completes without a `break`.
```python
x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print("Loop finished normally!")
```