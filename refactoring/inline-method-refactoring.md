---
b: https://blendedfeelings.com/software/refactoring/inline-method-refactoring.md
---

# Inline Method 
refactoring technique involves replacing a method call with the actual content of the method. This is done when the method's body is just as clear as its name, or when the method is overly simplistic and used only in one place. By inlining the method, you can eliminate the indirection that a method call introduces, which can sometimes make the code simpler and more direct.

Here's a step-by-step guide on how to apply the "Inline Method" refactoring technique:

1. **Identify Method to Inline**: Find a method that is simple enough to be inlined without losing clarity. It should generally be short, not be overloaded, and not be used in multiple places.

2. **Replace Method Calls**: Replace all calls to the method with the method's body. If the method has parameters, you'll need to replace the parameters with the actual arguments used in each call.

3. **Remove Method**: Once all calls to the method have been replaced, remove the method definition.

4. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public void ProcessOrder(Order order)
{
    if (IsOrderValid(order))
    {
        // Process the order
    }
}

private bool IsOrderValid(Order order)
{
    return order.Items.Count > 0 && order.TotalAmount > 0;
}
```

After applying "Inline Method" refactoring:

```csharp
public void ProcessOrder(Order order)
{
    if (order.Items.Count > 0 && order.TotalAmount > 0)
    {
        // Process the order
    }
}
```

In this example, the `IsOrderValid` method is short and only used once in the `ProcessOrder` method. By inlining the method, we've removed the indirection and made the condition directly visible in the `ProcessOrder` method, which can help readers of the code understand the processing logic without having to jump to a separate method.