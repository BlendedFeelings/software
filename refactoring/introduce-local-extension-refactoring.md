---
b: https://blendedfeelings.com/software/refactoring/introduce-local-extension-refactoring.md
---

# Introduce Local Extension 
refactoring technique is used when you need to add functionality to a third-party class or a class that you cannot or should not alter. Instead of modifying the class directly, you create a new class that extends the original class (subclass) or wraps it (wrapper class), and you add the new methods to this local extension.

Here's a step-by-step guide on how to apply the "Introduce Local Extension" refactoring technique:

1. **Identify the Need**: Determine the additional functionality that you need from the class.

2. **Create Local Extension**: Decide whether to use subclassing or wrapping:
    - **Subclassing**: Create a subclass of the original class and add the new methods there.
    - **Wrapping**: Create a wrapper class that contains an instance of the original class and delegate to it, adding new methods as needed.

3. **Use Local Extension**: Replace instances of the original class with the local extension where the additional functionality is needed.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C# using both subclassing and wrapping:

Suppose you are using a `DateTime` class from the .NET Framework, and you need methods to check if a date is a weekend and to add workdays to a date.

### Subclassing:

```csharp
public class ExtendedDateTime : DateTime
{
    public ExtendedDateTime(int year, int month, int day) : base(year, month, day) { }

    public bool IsWeekend()
    {
        return this.DayOfWeek == DayOfWeek.Saturday || this.DayOfWeek == DayOfWeek.Sunday;
    }

    // Add other methods as needed
}

// Client code
ExtendedDateTime date = new ExtendedDateTime(2023, 4, 30);
bool isWeekend = date.IsWeekend();
```

### Wrapping:

```csharp
public class DateTimeWrapper
{
    private DateTime _dateTime;

    public DateTimeWrapper(DateTime dateTime)
    {
        _dateTime = dateTime;
    }

    public bool IsWeekend()
    {
        return _dateTime.DayOfWeek == DayOfWeek.Saturday || _dateTime.DayOfWeek == DayOfWeek.Sunday;
    }

    public DateTimeWrapper AddWorkdays(int days)
    {
        // Implementation to add workdays, skipping weekends
        // ...
        return new DateTimeWrapper(_dateTime); // Return the modified date
    }

    // Delegate other DateTime methods as needed
    public int Year => _dateTime.Year;
    // ... and so on for other properties and methods
}

// Client code
DateTimeWrapper date = new DateTimeWrapper(new DateTime(2023, 4, 30));
bool isWeekend = date.IsWeekend();
DateTimeWrapper newDate = date.AddWorkdays(5);
```

In the subclassing example, `ExtendedDateTime` inherits from `DateTime` and adds the `IsWeekend` method. In the wrapping example, `DateTimeWrapper` contains a `DateTime` instance and adds both `IsWeekend` and `AddWorkdays` methods.

The choice between subclassing and wrapping depends on various factors, including whether the original class is sealed (cannot be subclassed), personal or team preference, and whether you need to add state to the extended functionality. Wrapping is more flexible and is often preferred when working with classes that you do not control.