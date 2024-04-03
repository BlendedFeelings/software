---
b: https://blendedfeelings.com/software/refactoring/split-temporary-variable-refactoring.md
---

# Split Temporary Variable 
refactoring technique is used when a temporary variable is reused for multiple purposes within a method. This can lead to confusion and errors, as the purpose of the variable can become unclear. By splitting the variable into separate variables for each distinct purpose, the code becomes cleaner and each variable's role is more explicit.

Here's a step-by-step guide on how to apply the "Split Temporary Variable" refactoring technique:

1. **Identify Reused Variable**: Find a temporary variable that is being reused for different unrelated values.

2. **Create Separate Variables**: For each distinct use of the variable, create a new temporary variable with a descriptive name that reflects its purpose.

3. **Replace Each Assignment**: Replace each assignment to the original variable with an assignment to the corresponding new variable.

4. **Update References**: Update all references to the original variable to refer to the appropriate new variable.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public void Calculate()
{
    double temp = 2 * (height + width);
    Console.WriteLine("Perimeter: " + temp);
    temp = height * width;
    Console.WriteLine("Area: " + temp);
}
```

After applying "Split Temporary Variable" refactoring:

```csharp
public void Calculate()
{
    double perimeter = 2 * (height + width);
    Console.WriteLine("Perimeter: " + perimeter);
    double area = height * width;
    Console.WriteLine("Area: " + area);
}
```

In this example, the `temp` variable was reused first to calculate the perimeter and then to calculate the area. This can be confusing for someone reading the code, as the purpose of `temp` changes halfway through the method. By splitting `temp` into `perimeter` and `area`, each variable now has a single, clear purpose, which improves readability and maintainability.