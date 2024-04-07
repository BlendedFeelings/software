---
b: https://blendedfeelings.com/software/object-oriented-programming/polymorphism.md
---

# Polymorphism 
is a core concept in object-oriented programming (OOP) that refers to the ability of different objects to be treated as instances of the same class through a common interface. It allows objects to be accessed through references of their superclass type rather than their actual class type. The specific form of polymorphism in OOP is often referred to as subtype polymorphism or dynamic polymorphism.

There are two main types of polymorphism in OOP:

1. **Compile-time Polymorphism (Static binding or Method Overloading)**: This type of polymorphism is resolved during compile time. It occurs when there are multiple methods with the same name but different parameters within the same class (method overloading) or when a method is overridden in a subclass (method overriding).

2. **Runtime Polymorphism (Dynamic binding or Method Overriding)**: This type of polymorphism is resolved during runtime. It happens when a call to an overridden method is resolved at runtime rather than compile time. This is achieved through method overriding where a subclass provides a specific implementation of a method that is already defined in its superclass.

Here's an example in C# that demonstrates runtime polymorphism through method overriding:

```csharp
public class Animal
{
    public virtual void Speak()
    {
        Console.WriteLine("The animal makes a sound.");
    }
}

public class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The dog barks.");
    }
}

public class Cat : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The cat meows.");
    }
}

class Program
{
    static void Main()
    {
        Animal myAnimal = new Animal();  // Create an Animal object
        Animal myDog = new Dog();        // Create a Dog object, referenced as Animal
        Animal myCat = new Cat();        // Create a Cat object, referenced as Animal

        myAnimal.Speak();  // Output: The animal makes a sound.
        myDog.Speak();     // Output: The dog barks.
        myCat.Speak();     // Output: The cat meows.
    }
}
```

In this example, the `Animal` class defines a virtual method `Speak`, which is then overridden by both the `Dog` and `Cat` classes. When `Speak` is called on `myDog` and `myCat`, which are referenced as `Animal` objects, the runtime system looks at the actual objects and invokes the correct method, demonstrating polymorphism.

Polymorphism allows for flexibility and the ability to extend systems with new types that can be treated as existing types but behave differently. It is a powerful feature that enables the writing of more generic and reusable code.