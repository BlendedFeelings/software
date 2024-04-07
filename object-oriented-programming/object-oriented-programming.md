---
b: https://blendedfeelings.com/software/object-oriented-programming/object-oriented-programming.md
---

# Object-Oriented Programming (OOP) 
is a programming paradigm based on the concept of "objects," which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). OOP languages are diverse, but the most popular ones include Java, C++, C#, Python, and Ruby.

Here are the core concepts of OOP:

1. **Class**: A blueprint for creating objects. A class defines a type's data and behavior.

2. **Object**: An instance of a class. An object has state (data) and behavior (methods).

3. **Inheritance**: A way to form new classes using classes that have already been defined. It helps in reusing the code and establishing a relationship between different classes.

4. **Encapsulation**: The bundling of data with the methods that operate on that data. It restricts direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the data.

5. **Abstraction**: The concept of hiding the complex reality while exposing only the necessary parts. It helps in reducing programming complexity and effort.

6. **Polymorphism**: The ability to present the same interface for differing underlying data types. A polymorphic type can be used in multiple forms as if it were a type from which it inherits.

Here's a simple example in C# that demonstrates some of these concepts:

```csharp
// Example of a Class
public class Animal
{
    // Example of Encapsulation
    private string name;  // Private field

    // Constructor
    public Animal(string name)
    {
        this.name = name;
    }

    // Example of Abstraction
    public void Eat()  // Public method
    {
        Console.WriteLine(name + " eats");
    }
}

// Example of Inheritance
public class Dog : Animal
{
    public Dog(string name) : base(name)
    {
    }

    // Example of Polymorphism
    public new void Eat()
    {
        Console.WriteLine(GetName() + " eats dog food");
    }

    // Example of Encapsulation
    public string GetName()
    {
        return name;  // Access to the private field through a method
    }
}

class Program
{
    static void Main()
    {
        Animal myAnimal = new Animal("Generic Animal");
        Dog myDog = new Dog("Rex");

        myAnimal.Eat();  // Output: Generic Animal eats
        myDog.Eat();     // Output: Rex eats dog food
    }
}
```

In this example, `Animal` is a base class with a private field `name` and a method `Eat()`. The `Dog` class inherits from `Animal` and overrides the `Eat()` method to demonstrate polymorphism. The `GetName()` method in `Dog` is an example of encapsulation, providing controlled access to the private field `name`.