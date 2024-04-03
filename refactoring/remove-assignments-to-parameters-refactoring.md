---
b: https://blendedfeelings.com/software/refactoring/remove-assignments-to-parameters-refactoring.md
---

# Remove Assignments to Parameters 
refactoring technique is about ensuring that function parameters act as read-only references to the data passed into a function. Assigning new values to parameters within the function can lead to unexpected behavior, especially if the original arguments are passed by reference (as in some programming languages), or if the function is complex and the parameter is reassigned multiple times, making it hard to track its value.

Here's a step-by-step guide on how to apply the "Remove Assignments to Parameters" refactoring technique:

1. **Identify Parameter Assignments**: Look for parameters that have their values reassigned within the method.

2. **Use Local Variables**: Instead of reassigning a parameter, create a new local variable and assign the parameter's value to it. Then use this local variable for any subsequent modifications.

3. **Replace Parameter Assignments**: Replace all assignments to the parameter with assignments to the new local variable.

4. **Update References**: Update all references to the parameter (after the initial reassignment) to refer to the new local variable.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public int Discount(int inputVal, int quantity, int yearToDate)
{
    if (inputVal > 50) inputVal -= 2;
    if (quantity > 100) inputVal -= 1;
    if (yearToDate > 10000) inputVal -= 4;
    return inputVal;
}
```

After applying "Remove Assignments to Parameters" refactoring:

```csharp
public int Discount(int inputVal, int quantity, int yearToDate)
{
    int result = inputVal;
    if (inputVal > 50) result -= 2;
    if (quantity > 100) result -= 1;
    if (yearToDate > 10000) result -= 4;
    return result;
}
```

In this example, the `inputVal` parameter is reassigned multiple times based on various conditions. By introducing a new local variable `result` and using it for modifications, the original parameter `inputVal` remains unchanged throughout the method. This makes the method's logic clearer and avoids any side effects that might occur if the parameter were passed by reference. It also makes the function easier to understand, as the `result` variable clearly represents the value that will be returned.