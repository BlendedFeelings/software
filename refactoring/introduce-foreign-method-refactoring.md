---
b: https://blendedfeelings.com/software/refactoring/introduce-foreign-method-refactoring.md
---

# Introduce Foreign Method 
refactoring technique is used when you need to perform an operation on an instance of a class that you cannot or should not modify. Instead of adding a method to the class itself, you create a method in your own class that takes an instance of the foreign class as an argument. This allows you to extend the functionality of the foreign class without altering its code.

Here's a step-by-step guide on how to apply the "Introduce Foreign Method" refactoring technique:

1. **Identify the Need**: Determine the operation that you need to perform on the foreign class.

2. **Create Foreign Method**: In your own class, create a method that performs this operation. The method should take an instance of the foreign class as a parameter.

3. **Use Foreign Method**: Replace the code that needed the operation with calls to your new foreign method.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Suppose you are using a `DateTime` class from a third-party library, and you need a method to check if a `DateTime` instance represents the last day of the month, but you cannot modify the `DateTime` class.

Before refactoring:

```csharp
// Client code
DateTime date = new DateTime(2023, 4, 30); // Assume this is the date you're working with

// You want to check if 'date' is the last day of the month
bool isLastDayOfMonth = date.AddDays(1).Month != date.Month;
```

After applying "Introduce Foreign Method" refactoring:

```csharp
public class DateUtils
{
    // Introduced foreign method
    public static bool IsLastDayOfMonth(DateTime date)
    {
        return date.AddDays(1).Month != date.Month;
    }
}

// Client code
DateTime date = new DateTime(2023, 4, 30); // Assume this is the date you're working with

// Use the introduced foreign method
bool isLastDayOfMonth = DateUtils.IsLastDayOfMonth(date);
```

In this example, the `DateUtils` class contains the introduced foreign method `IsLastDayOfMonth`, which takes a `DateTime` instance as an argument and checks if it's the last day of the month. This refactoring allows you to encapsulate the logic in a method without modifying the `DateTime` class, making the client code cleaner and more expressive.