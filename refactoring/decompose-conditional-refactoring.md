---
b: https://blendedfeelings.com/software/refactoring/decompose-conditional-refactoring.md
---

# Decompose Conditional 
refactoring technique involves taking a complex conditional statement (such as an `if` statement) and breaking it down into more manageable parts to improve readability and maintainability. This often involves extracting the condition into a method and possibly doing the same for the then and else blocks.

Here's a step-by-step guide on how to apply the "Decompose Conditional" refactoring technique:

1. **Identify Complex Conditional**: Find a conditional statement in your code that is complicated or not immediately clear.

2. **Extract Condition**: Create a method that returns the result of the conditional expression. The method name should clearly describe the condition being checked.

3. **Extract Then and Else Blocks**: If the then and/or else blocks of the conditional are complex, consider extracting them into their own methods as well.

4. **Replace Conditional with Method Calls**: Replace the original conditional expression with a call to the new method, and replace the then and/or else blocks with calls to their respective methods if they were extracted.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public void UpdateCustomerStatus(Customer customer)
{
    if (customer.LastOrderDate < DateTime.Now.AddDays(-30) && customer.IsPremium)
    {
        // Code to downgrade customer status
    }
    else
    {
        // Code to send customer a reminder
    }
}
```

After applying "Decompose Conditional" refactoring:

```csharp
public void UpdateCustomerStatus(Customer customer)
{
    if (ShouldDowngradeCustomer(customer))
    {
        DowngradeCustomerStatus(customer);
    }
    else
    {
        SendCustomerReminder(customer);
    }
}

private bool ShouldDowngradeCustomer(Customer customer)
{
    return customer.LastOrderDate < DateTime.Now.AddDays(-30) && customer.IsPremium;
}

private void DowngradeCustomerStatus(Customer customer)
{
    // Code to downgrade customer status
}

private void SendCustomerReminder(Customer customer)
{
    // Code to send customer a reminder
}
```

In this example, the complex condition in the `if` statement has been extracted to a method called `ShouldDowngradeCustomer`. The then and else blocks have been extracted to `DowngradeCustomerStatus` and `SendCustomerReminder` methods, respectively. This makes the `UpdateCustomerStatus` method much clearer and easier to understand at a glance. It also allows for the individual parts of the conditional logic to be tested separately.