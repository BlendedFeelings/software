---
b: https://blendedfeelings.com/software/refactoring/replace-temp-with-query-refactoring.md
---

# Replace Temp with Query 
refactoring technique involves replacing a temporary variable with a method call. This is particularly useful when the variable is assigned the result of a simple expression and is not modified afterwards. By using a method, the calculation is encapsulated, which can improve maintainability and reduce the complexity of the method where the temporary variable was used.

Here's a step-by-step guide on how to apply the "Replace Temp with Query" refactoring technique:

1. **Identify Temporary Variable**: Find a temporary variable that is assigned the result of a calculation or expression once and isn't modified later.

2. **Create Query Method**: Create a new method that returns the result of the expression you previously assigned to the temporary variable. The method name should clearly describe the value being returned.

3. **Replace Temp with Query**: Replace all references to the temporary variable with calls to the new method.

4. **Remove Temporary Variable**: Once all references to the temporary variable have been replaced, remove the variable's declaration and assignment.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public class Order
{
    private List<OrderItem> orderItems;
    private double taxRate;

    public double CalculateTotal()
    {
        double basePrice = 0;
        foreach (var item in orderItems)
        {
            basePrice += item.Price * item.Quantity;
        }

        double tax = basePrice * taxRate;
        double total = basePrice + tax;
        return total;
    }
}
```

After applying "Replace Temp with Query" refactoring:

```csharp
public class Order
{
    private List<OrderItem> orderItems;
    private double taxRate;

    public double CalculateTotal()
    {
        double total = BasePrice() + TaxAmount();
        return total;
    }

    private double BasePrice()
    {
        double basePrice = 0;
        foreach (var item in orderItems)
        {
            basePrice += item.Price * item.Quantity;
        }
        return basePrice;
    }

    private double TaxAmount()
    {
        return BasePrice() * taxRate;
    }
}
```

In this example, the `basePrice` and `tax` temporary variables have been replaced with the `BasePrice` and `TaxAmount` methods, respectively. This encapsulates the details of how the base price and tax amount are calculated and makes the `CalculateTotal` method more concise. It also allows for the reuse of the `BasePrice` method if needed elsewhere in the class.