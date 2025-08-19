# Polymorphism
polymorphism means same function name behaves differently for different objects.

## Real Life Analogy: "Animals Speak"
Different animals speak, but all of them use the same method: `speak()`.

| Animal | Action |
|--------|--------|
| Dog    | Woof   |
| Cat    | Meow   |
| Cow    | Moo    |

So, same method (`speak()`), but each animal gives a different sound = polymorphism.

```python
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

class Cow(Animal):
    def speak(self):
        print("Cow says: Moo!")
```
## Using Polymorphism:
```python
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()

# Dog says: Woof!
# Cat says: Meow!
# Cow says: Moo!
```
