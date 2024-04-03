---
b: https://blendedfeelings.com/software/refactoring/consolidate-conditional-expression-refactoring.md
---

# Consolidate Conditional Expression 
refactoring technique involves combining multiple conditional expressions that result in the same action into a single conditional expression. This can make the code more concise and easier to understand, especially when the same outcome is the result of several different conditions.

Here's a step-by-step guide on how to apply the "Consolidate Conditional Expression" refactoring technique:

1. **Identify Similar Conditional Expressions**: Look for multiple `if` statements or conditional expressions that lead to the same action or result.

2. **Combine Conditions**: Use logical operators (such as `&&` for AND, `||` for OR) to combine these conditions into a single conditional expression.

3. **Extract Combined Condition**: Optionally, if the combined condition is still complex, you can extract it into a separate method with a descriptive name.

4. **Replace Original Conditionals**: Replace the original multiple conditionals with the new combined conditional or method call.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public double CalculateShippingCost(Order order)
{
    if (order.IsInternational)
    {
        return internationalShippingRate;
    }
    if (order.TotalWeight > 20)
    {
        return heavyParcelRate;
    }
    if (order.IsExpress)
    {
        return expressDeliveryRate;
    }
    return standardShippingRate;
}
```

After applying "Consolidate Conditional Expression" refactoring:

```csharp
public double CalculateShippingCost(Order order)
{
    if (IsEligibleForSpecialShippingRate(order))
    {
        return GetSpecialShippingRate(order);
    }
    return standardShippingRate;
}

private bool IsEligibleForSpecialShippingRate(Order order)
{
    return order.IsInternational || order.TotalWeight > 20 || order.IsExpress;
}

private double GetSpecialShippingRate(Order order)
{
    if (order.IsInternational)
    {
        return internationalShippingRate;
    }
    if (order.TotalWeight > 20)
    {
        return heavyParcelRate;
    }
    if (order.IsExpress)
    {
        return expressDeliveryRate;
    }
    throw new InvalidOperationException("Order is not eligible for any special shipping rates.");
}
```

In this example, the `CalculateShippingCost` method originally had multiple conditions that could result in a special shipping rate being applied. These have been consolidated into a single method, `IsEligibleForSpecialShippingRate`, which checks all the conditions at once. The action of applying the special rate is handled by `GetSpecialShippingRate`. This refactoring makes it clear that there is a single decision point for determining whether special shipping rates apply, and it separates the logic for determining eligibility from the logic for determining the actual rate.