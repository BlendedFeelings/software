---
b: https://blendedfeelings.com/software/refactoring/replace-type-code-with-strategy-refactoring.md
---

# Replace Type Code with Strategy 
refactoring technique is used when an object's behavior varies according to a type code, but unlike the State pattern, the Strategy pattern is used when the variation is not due to internal state transitions but rather due to different algorithms or behaviors that need to be selected dynamically. The Strategy pattern encapsulates these algorithms into separate strategy classes.

Here's a step-by-step guide on how to apply the "Replace Type Code with Strategy" refactoring technique:

1. **Identify Type Code**: Find a field in a class that represents a type code and affects the behavior of the class.

2. **Create Strategy Interface**: Create an interface that represents the common strategy interface.

3. **Create Concrete Strategy Classes**: For each value of the type code, create a concrete strategy class that implements the interface.

4. **Move Type-Specific Behavior**: Move the behavior that depends on the type code into the appropriate strategy class. This may involve overriding methods or providing new implementations.

5. **Replace Type Code with Strategy Object**: Replace the type code field in the original class with a reference to the strategy object.

6. **Remove Type Code Field**: Once all type-specific behavior is encapsulated in strategy classes and the type code field is no longer used, remove it from the original class.

7. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Employee
{
    public const int ENGINEER = 0;
    public const int SALESMAN = 1;
    public const int MANAGER = 2;
    
    private int type;

    public Employee(int type)
    {
        this.type = type;
    }

    public int PayAmount()
    {
        switch (type)
        {
            case ENGINEER:
                return 1000;
            case SALESMAN:
                return 1500;
            case MANAGER:
                return 2000;
            default:
                throw new InvalidOperationException();
        }
    }
}
```

After applying "Replace Type Code with Strategy" refactoring:

```csharp
public interface IPayStrategy
{
    int PayAmount();
}

public class EngineerPayStrategy : IPayStrategy
{
    public int PayAmount()
    {
        return 1000;
    }
}

public class SalesmanPayStrategy : IPayStrategy
{
    public int PayAmount()
    {
        return 1500;
    }
}

public class ManagerPayStrategy : IPayStrategy
{
    public int PayAmount()
    {
        return 2000;
    }
}

public class Employee
{
    private IPayStrategy payStrategy;

    public Employee(IPayStrategy payStrategy)
    {
        this.payStrategy = payStrategy;
    }

    public int PayAmount()
    {
        return payStrategy.PayAmount();
    }
}
```

In the refactored example, the `Employee` class no longer uses an integer type code to determine the pay amount. Instead, it has a `payStrategy` field that holds a reference to an `IPayStrategy` object. The `PayAmount` method in the `Employee` class delegates the behavior to the current strategy object. Each strategy class (`EngineerPayStrategy`, `SalesmanPayStrategy`, `ManagerPayStrategy`) encapsulates the pay calculation for that specific type of employee. This approach allows for easy addition of new pay strategies and simplifies the `Employee` class by removing the conditional logic related to pay calculation.