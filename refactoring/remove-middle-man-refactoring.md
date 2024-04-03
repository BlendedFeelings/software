---
b: https://blendedfeelings.com/software/refactoring/remove-middle-man-refactoring.md
---

# Remove Middle Man 
refactoring technique is used when an object is doing little more than delegating to another object. If an intermediary object mostly consists of simple delegating methods, it may be better to remove these methods and let the client call the end object directly. This can simplify the design by reducing unnecessary indirection.

Here's a step-by-step guide on how to apply the "Remove Middle Man" refactoring technique:

1. **Identify Delegating Methods**: Find methods in the intermediary class that simply delegate calls to another object.

2. **Expose Delegate**: If the delegate object is not already accessible to the client, modify the intermediary class to provide access to the delegate.

3. **Replace Delegation with Direct Calls**: In the client code, replace calls to the intermediary's delegating methods with direct calls to the delegate object.

4. **Remove Delegating Methods**: Once all references to the delegating methods have been replaced, remove these methods from the intermediary class.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Person
{
    private Department _department;
    
    public Person(Department department)
    {
        _department = department;
    }

    public Manager GetManager()
    {
        return _department.Manager;
    }

    // Other properties and methods
}

public class Department
{
    public Manager Manager { get; set; }
    
    // Other properties and methods
}

public class Manager
{
    // Properties and methods
}

// Client code
var john = new Person(department);
Manager johnsManager = john.GetManager();
```

After applying "Remove Middle Man" refactoring:

```csharp
public class Person
{
    public Department Department { get; private set; }
    
    public Person(Department department)
    {
        Department = department;
    }

    // Other properties and methods
}

public class Department
{
    public Manager Manager { get; set; }
    
    // Other properties and methods
}

public class Manager
{
    // Properties and methods
}

// Client code
var john = new Person(department);
Manager johnsManager = john.Department.Manager;
```

In this example, the `GetManager` method in the `Person` class was simply delegating to the `Department` object. By removing this method and exposing the `Department` property, the client code can now directly access the `Manager` through the `Department`. This reduces the number of methods in the `Person` class and eliminates the unnecessary indirection of the `GetManager` method. The client code is slightly more verbose but is more direct in its intention.