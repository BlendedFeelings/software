---
b: https://blendedfeelings.com/software/refactoring/replace-type-code-with-subclasses-refactoring.md
---

# Replace Type Code with Subclasses 
refactoring technique is used when an object's behavior is determined by a type code (usually represented by a number or string). Instead of using a type code, you create subclasses for each type and move the type-specific behavior into these subclasses. This leverages polymorphism to choose the correct behavior at runtime.

Here's a step-by-step guide on how to apply the "Replace Type Code with Subclasses" refactoring technique:

1. **Identify Type Code**: Find a field in a class that represents a type code and determines the behavior of the class.

2. **Create Base Class or Interface**: If not already present, create a base class or interface that represents the common interface for all types.

3. **Create Subclasses**: For each type code value, create a subclass that extends the base class or implements the interface.

4. **Move Type-Specific Behavior**: Move the behavior that depends on the type code into the appropriate subclass. Override methods or provide new implementations as needed.

5. **Replace Type Code with Subclass Instances**: Modify the client code to instantiate the appropriate subclass based on the type code, instead of using the type code field.

6. **Remove Type Code Field**: Once all type-specific behavior is moved to subclasses and the type code field is no longer used, remove it from the base class.

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

    public int GetTypeCode()
    {
        return type;
    }

    // Other methods that use 'type' to determine behavior
}
```

After applying "Replace Type Code with Subclasses" refactoring:

```csharp
// Base class or interface
public abstract class Employee
{
    public abstract int GetTypeCode();

    // Other methods now use polymorphism instead of 'type' checks
}

public class Engineer : Employee
{
    public override int GetTypeCode()
    {
        return Employee.ENGINEER;
    }

    // Engineer-specific behavior
}

public class Salesman : Employee
{
    public override int GetTypeCode()
    {
        return Employee.SALESMAN;
    }

    // Salesman-specific behavior
}

public class Manager : Employee
{
    public override int GetTypeCode()
    {
        return Employee.MANAGER;
    }

    // Manager-specific behavior
}
```

In the refactored example, the `Employee` class becomes an abstract class. The `type` field is removed, and three new subclasses (`Engineer`, `Salesman`, `Manager`) are created to represent the specific types of employees. Each subclass overrides the `GetTypeCode` method to return the appropriate type code. Client code that previously created an `Employee` object with a type code would now directly instantiate the specific subclass.

This refactoring improves the design by removing the need for conditional logic based on type codes and by using inheritance to handle variations in behavior.