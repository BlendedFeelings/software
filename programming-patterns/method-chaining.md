---
b: https://blendedfeelings.com/software/programming-patterns/method-chaining.md
---

# Method chaining
also known as named parameter idiom, is a common programming technique where multiple methods are called on the same object in a single statement. This is done by having each method return the object itself (`this` in many object-oriented languages), which allows the calls to be chained together in a linear fashion. This pattern is particularly common in object-oriented programming and can lead to more readable and expressive code.

Here's an example of method chaining in C#:

```csharp
public class Car
{
    public int Speed { get; private set; }
    public string Color { get; private set; }

    public Car SetSpeed(int speed)
    {
        Speed = speed;
        return this;
    }

    public Car Paint(string color)
    {
        Color = color;
        return this;
    }
}

// Using method chaining to set properties
Car myCar = new Car()
    .SetSpeed(100)
    .Paint("Red");
```

In the above example, both `SetSpeed` and `Paint` methods return the `Car` object, allowing the calls to be chained. This style of coding can make the code look cleaner and more intuitive, as it resembles natural language.

Method chaining is a key feature in many libraries and frameworks, particularly those that implement a fluent interface. Fluent interfaces are designed specifically to enable method chaining by providing an API that encourages the writing of code in a more readable and flowing manner.

One of the most well-known examples of method chaining is in the jQuery library for JavaScript, where you can often see code like this:

```javascript
$('#myElement')
    .addClass('highlight')
    .show()
    .html('Hello, world!');
```

Each method call manipulates the element and then returns the jQuery object, allowing the next method in the chain to be called immediately.

However, method chaining isn't without its critics. Some argue that it can make debugging harder since it's less clear where an error occurred in a chain of method calls. It can also potentially lead to less optimized code if the object being returned is not managed efficiently. Despite these concerns, method chaining remains a popular and widely used technique in many programming languages.