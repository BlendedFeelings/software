---
b: https://blendedfeelings.com/software/refactoring/extract-class-refactoring.md
---

# Extract Class 
refactoring technique is used when a class has too many responsibilities or too much code, making it difficult to maintain. By identifying a subset of related data and behavior, you can create a new class and move the relevant fields and methods from the old class into the new class. This helps in adhering to the Single Responsibility Principle and makes both classes easier to understand and maintain.

Here's a step-by-step guide on how to apply the "Extract Class" refactoring technique:

1. **Identify Responsibilities**: Determine which fields and methods can be grouped together into a new class based on their related functionality.

2. **Create New Class**: Create a new class to encapsulate the identified fields and methods.

3. **Move Fields and Methods**: Move the relevant fields and methods from the original class to the new class. Update access levels and scope as necessary.

4. **Update References**: Refactor the original class to reference the new class where necessary. Update client code to use the new class as appropriate.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Person
{
    public string Name { get; set; }
    public string HomeAddress { get; set; }
    public string WorkAddress { get; set; }
    // ... Many other fields and methods related to the person's addresses

    // Methods that deal with person's name
    // ...
}
```

After applying "Extract Class" refactoring:

```csharp
public class Person
{
    public string Name { get; set; }
    public Address HomeAddress { get; set; }
    public Address WorkAddress { get; set; }
    // ... Other fields and methods related to the person

    // Methods that deal with person's name
    // ...
}

public class Address
{
    public string Street { get; set; }
    public string City { get; set; }
    public string PostalCode { get; set; }
    // ... Other fields and methods related to the address

    // Methods that deal with address details
    // ...
}

// Client code
Person person = new Person();
person.HomeAddress = new Address { Street = "123 Elm St", City = "Metropolis", PostalCode = "12345" };
person.WorkAddress = new Address { Street = "456 Maple Ave", City = "Metropolis", PostalCode = "67890" };
```

In this example, the `Address`-related fields and methods were extracted from the `Person` class into a new `Address` class. The `Person` class now holds references to `Address` objects for the home and work addresses. This separation of concerns makes both the `Person` and `Address` classes more focused and easier to manage. The client code creates `Address` objects and assigns them to the `Person` object, showing a clear relationship between a person and their addresses.