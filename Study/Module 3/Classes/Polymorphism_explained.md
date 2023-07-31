## Polymorphism in Python

Polymorphism in Python is a powerful feature of object-oriented programming that allows objects of different classes to be treated as objects of a common base class. It provides flexibility and extensibility to your programs, allowing code to be written that can work with objects of multiple types.

### 1. Method Overriding

Method overriding occurs when a subclass defines a method with the same name as a method in its superclass. The method in the subclass overrides the implementation of the method in the superclass. This allows the subclass to provide its own implementation while still adhering to the common interface defined by the superclass. Here's an example:

```python
class Shape:
    def draw(self):
        print("Drawing a generic shape.")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")

class Square(Shape):
    def draw(self):
        print("Drawing a square.")

shape = Shape()
circle = Circle()
square = Square()

shape.draw()    # Output: Drawing a generic shape.
circle.draw()   # Output: Drawing a circle.
square.draw()   # Output: Drawing a square.
```

### 2. Polymorphic Functions

Polymorphism is not limited to method overriding. It can also be achieved through polymorphic functions. A polymorphic function can operate on objects of different classes as long as those objects adhere to a common interface or have compatible behavior. Here's an example:

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_speak(dog)     # Output: Woof!
make_speak(cat)     # Output: Meow!
```

### 3. Polymorphism with Inheritance
Polymorphism is particularly powerful when used with inheritance hierarchies. It allows different subclasses to be treated as objects of their common base class, enabling code to work uniformly with objects of different types. Here's an example:

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

```

Polymorphism in Python allows objects of different classes to be treated interchangeably based on their shared interface or behavior. It provides a flexible and extensible way of writing code that can work with objects of different types, promoting code reuse and modular design.
