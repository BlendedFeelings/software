---
b: https://blendedfeelings.com/software/refactoring/consolidate-duplicate-conditional-fragments-refactoring.md
---

# Consolidate Duplicate Conditional Fragments 
refactoring technique is used when the same piece of code is duplicated across multiple branches of a conditional statement. By consolidating the duplicated code and moving it outside of the conditional, you can reduce redundancy and make the code more concise and easier to maintain.

Here's a step-by-step guide on how to apply the "Consolidate Duplicate Conditional Fragments" refactoring technique:

1. **Identify Duplicate Fragments**: Look for code fragments that are duplicated in two or more branches of a conditional statement.

2. **Move Code Outside Conditional**: Relocate the duplicated code to just before or just after the conditional statement, depending on whether the code needs to execute before or after the decision is made.

3. **Remove Duplicates**: Remove the duplicate code fragments from within the conditional branches.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public void UpdatePrice(Order order)
{
    if (order.IsSpecialDeal)
    {
        order.Price = order.Price * 0.95;
        SaveOrder(order);
    }
    else
    {
        order.Price = order.Price * 0.98;
        SaveOrder(order);
    }
}
```

After applying "Consolidate Duplicate Conditional Fragments" refactoring:

```csharp
public void UpdatePrice(Order order)
{
    if (order.IsSpecialDeal)
    {
        order.Price = order.Price * 0.95;
    }
    else
    {
        order.Price = order.Price * 0.98;
    }
    SaveOrder(order); // Consolidated code moved outside the conditional
}
```

In this example, the `SaveOrder(order)` method call was duplicated in both branches of the `if` statement. By moving it outside the conditional, the duplication is eliminated. This makes the `UpdatePrice` method shorter and clearer, as it now explicitly shows that `SaveOrder` is called regardless of the condition. It also reduces the risk of errors, such as updating one branch of the conditional without updating the other.