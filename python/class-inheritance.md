---
b: https://blendedfeelings.com/software/python/class-inheritance.md
---

# Inheritance in Python
is a mechanism that allows you to define a new class that takes on the attributes and methods of an existing class. The new class is called a derived (or child) class, and the class from which it inherits is called the base (or parent) class.

Here's a basic example of how inheritance works in Python:

```python
# Define the base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define the derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the method defined in the derived class
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
```

In this example, `Animal` is the base class with a constructor `__init__` that initializes the `name` attribute and a method `speak` that is intended to be overridden by subclasses. The `Dog` and `Cat` classes are derived from `Animal` and provide their own implementations of the `speak` method.

Key concepts in Python inheritance include:

- **Inheritance**: The process by which one class takes on the attributes and methods of another.
- **Subclass**: A class that inherits from another class (also called a derived or child class).
- **Superclass**: The class from which attributes and methods are inherited (also called a base or parent class).
- **Method Overriding**: Providing a new implementation for a method inherited from the parent class.
- **`super()` Function**: A built-in function that allows you to call methods from the superclass in the subclass, often used to extend the functionality of the inherited method.

### Multiclass inheritance

Here's a basic example of how multiple inheritance works in Python:

```python
# Define two parent classes
class ParentClass1:
    def method1(self):
        print("Method 1 from ParentClass1")

class ParentClass2:
    def method2(self):
        print("Method 2 from ParentClass2")

# Define a child class that inherits from both ParentClass1 and ParentClass2
class ChildClass(ParentClass1, ParentClass2):
    def method3(self):
        print("Method 3 from ChildClass")

# Create an instance of the child class
child = ChildClass()

# Call methods from the child class and parent classes
child.method1()  # Inherited from ParentClass1
child.method2()  # Inherited from ParentClass2
child.method3()  # Defined in ChildClass
```

In this example, `ChildClass` inherits from both `ParentClass1` and `ParentClass2`. Therefore, an object of `ChildClass` can access methods from both parent classes as well as its own methods.

When using multiple inheritance, it's important to consider the method resolution order (MRO), which is the order in which Python looks for a method in a hierarchy of classes. Python uses a depth-first, left-to-right search algorithm, which means it searches the first parent class and its ancestors before moving on to the next parent class.

You can view the MRO of a class using the `.__mro__` attribute or the built-in `mro()` method:

```python
print(ChildClass.__mro__)
# or
print(ChildClass.mro())
```

This will show you the order in which Python will search for methods.

Multiple inheritance can lead to complexities, especially when the same method is defined in multiple parent classes. This is known as the "diamond problem." Python's MRO is designed to ensure that each class in the inheritance hierarchy is only visited once, thus preventing some of the issues that can arise from multiple inheritance. However, it's still important to design your class hierarchies carefully to avoid confusion and maintain readability.