---
b: https://blendedfeelings.com/software/refactoring/hide-delegate-refactoring.md
---

# Hide Delegate 
refactoring technique is used when a client object is calling a delegate object through an intermediary object. Instead of the client interacting directly with the delegate, the intermediary provides its own method to hide the delegate. This encapsulates the relationship and reduces the client's dependency on the delegate's interface, making it easier to change the delegate without affecting the client.

Here's a step-by-step guide on how to apply the "Hide Delegate" refactoring technique:

1. **Identify Delegate Calls**: Find places in the client code where the client is calling methods on a delegate object through an intermediary.

2. **Create Wrapper Method**: In the intermediary object, create a method that wraps the delegate method call. The client will call this wrapper method instead of the delegate method directly.

3. **Replace Delegate Calls**: Replace all instances of the client calling the delegate method with calls to the new wrapper method on the intermediary.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Person
{
    public Department Department { get; set; }
    
    // Other properties and methods
}

public class Department
{
    public string ChargeCode { get; set; }
    public Manager Manager { get; set; }
    
    // Other properties and methods
}

public class Manager
{
    // Properties and methods
}

// Client code
var john = new Person();
Manager johnsManager = john.Department.Manager;
```

After applying "Hide Delegate" refactoring:

```csharp
public class Person
{
    public Department Department { get; set; }
    
    public Manager GetManager()
    {
        return Department.Manager;
    }

    // Other properties and methods
}

public class Department
{
    public string ChargeCode { get; set; }
    public Manager Manager { get; set; }
    
    // Other properties and methods
}

public class Manager
{
    // Properties and methods
}

// Client code
var john = new Person();
Manager johnsManager = john.GetManager();
```

In this example, the `Person` class has been refactored to include a `GetManager` method that hides the delegate (`Department`). The client code now calls `john.GetManager()` instead of accessing the `Manager` through the `Department` property, which reduces the client's dependency on the structure of the `Department` class. This means that if the way a `Person` object retrieves its `Manager` changes in the future, only the `Person` class needs to be updated, and the client code remains unaffected.