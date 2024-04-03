---
b: https://blendedfeelings.com/software/concepts/composition-over-inheritance.md
---

# Composition Over Inheritance
is a principle that suggests using composition to achieve code reuse and flexibility rather than inheritance. The principle is a guideline that encourages developers to design their software in such a way that functionality is provided or extended by composing objects with desired behaviors, rather than inheriting from a base or parent class.

### Understanding Composition Over Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit properties and methods from another class. While inheritance provides a simple way to achieve polymorphic behavior and code reuse, it can also lead to a rigid class structure that is difficult to modify and understand, especially as the system evolves. This is often referred to as the "inheritance hierarchy problem."

Composition, on the other hand, involves building more complex objects by combining simpler, more focused objects. This is typically achieved by including instances of other classes as fields in your class, rather than inheriting from those classes.

### Benefits of Composition Over Inheritance

- **Flexibility**: Composition provides greater flexibility by enabling dynamic behavior change at runtime through object composition.
- **Loose Coupling**: Objects remain more loosely coupled, which means that changes in one part of the system are less likely to affect others.
- **Better Encapsulation**: Composition allows for better encapsulation since internal details of composed objects can be hidden from the containing object.
- **Avoidance of Deep Inheritance Hierarchies**: Composition avoids the complexity and brittleness that can arise from deep class hierarchies.

### Examples of Composition Over Inheritance

Consider a game with different types of characters, each with different abilities. Instead of creating a complex inheritance hierarchy of character types, you could define a `Character` class and separate classes for abilities, such as `Flying`, `Swimming`, or `Walking`. A `Character` object would have fields for these abilities and use them as needed.

```csharp
public class Character
{
    private IFlying flyingBehavior;
    private ISwimming swimmingBehavior;
    // Other behaviors...

    public Character(IFlying flyingBehavior, ISwimming swimmingBehavior)
    {
        this.flyingBehavior = flyingBehavior;
        this.swimmingBehavior = swimmingBehavior;
    }

    public void Fly()
    {
        flyingBehavior.Fly();
    }

    public void Swim()
    {
        swimmingBehavior.Swim();
    }
    // Other methods...
}

public interface IFlying
{
    void Fly();
}

public class CanFly : IFlying
{
    public void Fly()
    {
        // Implementation for flying
    }
}

public interface ISwimming
{
    void Swim();
}

public class CanSwim : ISwimming
{
    public void Swim()
    {
        // Implementation for swimming
    }
}
```

In this example, `Character` objects are composed of different behaviors that can be mixed and matched as needed, rather than inheriting from a base class with fixed behavior.

### Applying Composition Over Inheritance

To apply this principle effectively, developers should:

- Prefer defining classes based on what they do (behaviors) rather than what they are (inheritance).
- Use interfaces to define contracts for behaviors and compose objects to fulfill those contracts.
- Consider using design patterns that promote composition, such as Strategy, Decorator, or Composite patterns.

While composition is often favored over inheritance, inheritance is still a valuable tool in certain situations, particularly when there is a clear "is-a" relationship and no significant risk of creating overly complex class hierarchies. The choice between composition and inheritance should be based on the specific needs of the application and the problem domain.