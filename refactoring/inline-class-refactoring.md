---
b: https://blendedfeelings.com/software/refactoring/inline-class-refactoring.md
---

# Inline Class 
refactoring technique is used when a class isn't doing enough to justify its existence. It might have too few responsibilities or its responsibilities might be better placed in another class. By moving all features from the class to another one and deleting the original, the design can be simplified.

Here's a step-by-step guide on how to apply the "Inline Class" refactoring technique:

1. **Identify Class to Inline**: Find a class that has few responsibilities or where its responsibilities are closely related to another class.

2. **Move Fields and Methods**: Move all fields and methods from the class you want to inline to the target class. Adjust the scope and access levels as necessary.

3. **Refactor References**: Refactor all references to the inlined class to the target class.

4. **Delete Inlined Class**: Once all fields and methods have been moved and all references updated, delete the original class.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public class Person
{
    public string Name { get; set; }
    private TelephoneNumber _telephoneNumber;

    public Person(string name, TelephoneNumber telephoneNumber)
    {
        Name = name;
        _telephoneNumber = telephoneNumber;
    }

    public TelephoneNumber GetTelephoneNumber()
    {
        return _telephoneNumber;
    }
}

public class TelephoneNumber
{
    public string AreaCode { get; set; }
    public string Number { get; set; }

    public string GetFullNumber()
    {
        return AreaCode + Number;
    }
}

// Client code
Person person = new Person("John Doe", new TelephoneNumber { AreaCode = "123", Number = "4567890" });
string phoneNumber = person.GetTelephoneNumber().GetFullNumber();
```

After applying "Inline Class" refactoring:

```csharp
public class Person
{
    public string Name { get; set; }
    public string AreaCode { get; set; }
    public string Number { get; set; }

    public Person(string name, string areaCode, string number)
    {
        Name = name;
        AreaCode = areaCode;
        Number = number;
    }

    public string GetFullNumber()
    {
        return AreaCode + Number;
    }
}

// Client code
Person person = new Person("John Doe", "123", "4567890");
string phoneNumber = person.GetFullNumber();
```

In this example, the `TelephoneNumber` class was inlined into the `Person` class. The fields `AreaCode` and `Number`, along with the method `GetFullNumber()`, were moved from `TelephoneNumber` to `Person`. The `TelephoneNumber` class was then removed. The client code was updated to use the `Person` class directly for phone number operations. This simplifies the model by removing an unnecessary class and making the `Person` class the single point of contact for related information.