---
b: https://blendedfeelings.com/software/python/class.md
---

# Class in Python 
is a blueprint for creating objects. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Here is a basic example of a Python class:

```python
class Dog:
    # Class attribute
    species = 'Canis familiaris'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances of the Dog class
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# Access the instance attributes
print(buddy.name)  # Buddy
print(miles.age)   # 4

# Call our instance methods
print(buddy.description())  # Buddy is 9 years old
print(miles.speak("Woof"))  # Miles says Woof
```

In this example, `Dog` is a class that represents the concept of a dog. It has a class attribute `species`, two instance attributes `name` and `age`, and two methods `description` and `speak`. When you create instances of the `Dog` class, you're creating new "dog" objects that can have different names and ages, and can perform actions defined by their methods.

Key concepts in Python classes:

- `__init__`: A special method that gets called when a new instance of the class is created. It's used for initializing the attributes of the class.
- `self`: Represents the instance of the class. By using the `self` keyword, you can access the attributes and methods of the class in Python.
- Class Attribute: A variable that is shared by all instances of a class.
- Instance Attribute: A variable that is unique to each instance of a class.
- Method: A function that is defined inside a class and can be called on an instance of that class.

### @staticmethod
A static method does not receive an implicit first argument. This means that it can neither modify object instance state nor class state. Static methods are restricted in what data they can access - they can't access the properties associated with class instances without a reference to an instance. They are utility-type methods that take some parameters and work upon those parameters. To define a static method, you use the `@staticmethod` decorator.

Here is an example of a static method:

```python
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # Do something with arg1 and arg2
        return arg1 + arg2
```