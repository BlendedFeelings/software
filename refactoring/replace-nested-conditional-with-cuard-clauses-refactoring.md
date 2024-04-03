---
b: https://blendedfeelings.com/software/refactoring/replace-nested-conditional-with-cuard-clauses-refactoring.md
---

# Replace Nested Conditional with Guard Clauses 
refactoring technique is used to make code clearer by replacing nested conditional structures with early returns, which are also known as guard clauses. This technique is particularly useful in methods where certain conditions lead to early exits because they represent special cases or errors that need to be handled first before the main logic of the method can proceed.

Here's a step-by-step guide on how to apply the "Replace Nested Conditional with Guard Clauses" refactoring technique:

1. **Identify Nested Conditionals**: Look for methods with nested conditional structures, especially those that handle special cases or errors.

2. **Introduce Guard Clauses**: For each special case or error condition, add a guard clause that checks the condition and returns early if it is met.

3. **Flatten Main Logic**: Once all special cases have early returns, the main logic of the method can be flattened, no longer needing to be nested within an `else` block.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged after refactoring.

Here's an example in C#:

Before refactoring:

```csharp
public double CalculatePay(Employee employee)
{
    double result;
    if (employee.IsRetired)
    {
        result = 0;
    }
    else
    {
        if (employee.IsOnVacation)
        {
            if (employee.LengthOfService > 10)
            {
                result = employee.BasePay * 1.5;
            }
            else
            {
                result = employee.BasePay * 1.2;
            }
        }
        else
        {
            result = employee.BasePay;
        }
    }
    return result;
}
```

After applying "Replace Nested Conditional with Guard Clauses" refactoring:

```csharp
public double CalculatePay(Employee employee)
{
    if (employee.IsRetired)
    {
        return 0;
    }

    if (employee.IsOnVacation)
    {
        if (employee.LengthOfService > 10)
        {
            return employee.BasePay * 1.5;
        }
        else
        {
            return employee.BasePay * 1.2;
        }
    }

    return employee.BasePay;
}
```

In this example, the guard clause for `employee.IsRetired` allows us to return early, simplifying the logic that follows. The nested conditional for `employee.IsOnVacation` is still present, but now it's at the top level of the method, making it easier to read and understand. If desired, further refactoring could be applied to handle the vacation logic, potentially with additional guard clauses or method extraction. The flattened structure makes the primary path through the code clearer and reduces the cognitive load required to understand the method's behavior.