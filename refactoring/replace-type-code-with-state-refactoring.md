---
b: https://blendedfeelings.com/software/refactoring/replace-type-code-with-state-refactoring.md
---

# Replace Type Code with State 
refactoring technique is used when an object's behavior changes based on its state, which is represented by a type code. Instead of using a type code, you encapsulate the state-specific behavior in separate state classes. This approach allows for a cleaner design where the state transitions and behaviors are managed by state objects, making use of the State design pattern.

Here's a step-by-step guide on how to apply the "Replace Type Code with State" refactoring technique:

1. **Identify Type Code**: Find a field in a class that represents the state of the object through a type code.

2. **Create State Base Class or Interface**: Create a base class or interface that represents the common state interface.

3. **Create Concrete State Classes**: For each value of the type code, create a concrete state class that extends the base class or implements the interface.

4. **Move State-Specific Behavior**: Move the behavior that depends on the type code into the appropriate state class. This may involve overriding methods or providing new implementations.

5. **Replace Type Code with State Object**: Replace the type code field in the original class with a reference to the state object.

6. **Implement State Transitions**: Implement the logic for transitioning between states within the state classes or the context class.

7. **Remove Type Code Field**: Once all state-specific behavior is encapsulated in state classes and the type code field is no longer used, remove it from the original class.

8. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Fan
{
    public const int OFF = 0;
    public const int LOW = 1;
    public const int HIGH = 2;
    
    private int state = OFF;

    public void PullChain()
    {
        if (state == OFF)
        {
            state = LOW;
            Console.WriteLine("Fan is on low.");
        }
        else if (state == LOW)
        {
            state = HIGH;
            Console.WriteLine("Fan is on high.");
        }
        else if (state == HIGH)
        {
            state = OFF;
            Console.WriteLine("Fan is off.");
        }
    }

    // Other methods
}
```

After applying "Replace Type Code with State" refactoring:

```csharp
public abstract class FanState
{
    public abstract void PullChain(Fan fan);
}

public class OffState : FanState
{
    public override void PullChain(Fan fan)
    {
        fan.SetState(new LowState());
        Console.WriteLine("Fan is on low.");
    }
}

public class LowState : FanState
{
    public override void PullChain(Fan fan)
    {
        fan.SetState(new HighState());
        Console.WriteLine("Fan is on high.");
    }
}

public class HighState : FanState
{
    public override void PullChain(Fan fan)
    {
        fan.SetState(new OffState());
        Console.WriteLine("Fan is off.");
    }
}

public class Fan
{
    private FanState state;

    public Fan()
    {
        state = new OffState();
    }

    public void SetState(FanState state)
    {
        this.state = state;
    }

    public void PullChain()
    {
        state.PullChain(this);
    }

    // Other methods
}
```

In the refactored example, the `Fan` class no longer uses an integer type code to represent its state. Instead, it has a `state` field that holds a reference to a `FanState` object. The `PullChain` method in the `Fan` class delegates the behavior to the current state object, which then changes the state of the fan as needed. Each state class (`OffState`, `LowState`, `HighState`) encapsulates the behavior for that specific state. This approach allows for easy addition of new states and simplifies the `Fan` class by removing the conditional logic related to state changes.