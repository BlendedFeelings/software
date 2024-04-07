---
b: https://blendedfeelings.com/software/object-oriented-programming/inheritance.md
---

# Inheritance 
is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit properties and behaviors (methods) from another class. The class from which properties and methods are inherited is called the parent class, base class, or superclass, while the class that inherits these properties and methods is called the child class, derived class, or subclass.

Here are some key points about inheritance in OOP:

1. **Code Reusability**: Inheritance promotes code reusability by allowing new classes to be created that reuse, extend, and modify the behavior defined in other classes.

2. **Hierarchical Classification**: It provides a natural and logical way to organize classes in a hierarchical manner from the most general to the most specific.

3. **Extensibility**: It makes it easier to extend the functionality of existing classes without modifying them, by creating new classes that add new attributes or methods.

4. **Polymorphism**: Inheritance allows for polymorphism, which is the ability to treat objects of different subclasses that share the same superclass as objects of the superclass type. This enables the same operation to behave differently on different classes.

5. **Override and Extend**: Subclasses can override or extend the functionality of superclass methods. Overriding means providing a new implementation for an inherited method, while extending means adding new methods or properties in addition to the inherited ones.

6. **Access Modifiers**: Inheritance also involves understanding access modifiers (public, protected, private), which control the visibility of superclass members to the subclass.

7. **Constructor Inheritance**: Constructors are not inherited like other methods. However, the subclass constructor can call the superclass constructor to initialize inherited attributes.

8. **Abstract Classes and Interfaces**: Abstract classes and interfaces can be used to define methods that must be implemented by subclasses, thus enforcing a contract for behavior.

9. **Multiple Inheritance**: Some languages like C++ support multiple inheritance, where a class can inherit from more than one class. However, this can lead to complexity and ambiguity (the "diamond problem"), and many languages like Java and C# do not support multiple inheritance of classes but allow multiple inheritance of interfaces.

10. **The "is-a" Relationship**: Inheritance represents an "is-a" relationship between the subclass and the superclass. For example, if `Dog` is a subclass of `Animal`, then a `Dog` "is an" `Animal`.

Here is a simple example in C# to illustrate inheritance:

```csharp
// Base class or Superclass
public class Animal
{
    public string Name { get; set; }

    public void Eat()
    {
        Console.WriteLine("Eating...");
    }
}

// Derived class or Subclass
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Barking...");
    }
}

// Usage
Dog myDog = new Dog();
myDog.Name = "Buddy";
myDog.Eat(); // Inherited method
myDog.Bark(); // Subclass method
```

In this example, `Dog` inherits from `Animal`, meaning it can use the `Eat` method defined in `Animal`, and it also has its own method `Bark`.