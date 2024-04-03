---
b: https://blendedfeelings.com/software/refactoring/replace-method-with-method-object-refactoring.md
---

# Replace Method with Method Object 
refactoring technique is used when you have a long method that cannot be easily refactored by extracting methods because it uses many local variables that interact with each other. By turning the method into its own class, you can turn the local variables into fields of the new class, making it easier to decompose the method into several smaller methods within the same class.

Here's a step-by-step guide on how to apply the "Replace Method with Method Object" refactoring technique:

1. **Identify Long Method**: Find a long method that is difficult to refactor due to its use of many local variables.

2. **Create Method Object Class**: Create a new class that will represent the method object. The name of the class should reflect the original method's purpose.

3. **Copy Method to Method Object**: Copy the entire method into the new class as a public method, typically named `Compute` or `Calculate`.

4. **Convert Local Variables to Fields**: Turn all of the original method's local variables into fields of the new class.

5. **Add Constructor**: Create a constructor for the new class that takes the original method's parameters as arguments and assigns them to the fields of the class.

6. **Replace Original Method with Call to Method Object**: In the original class, replace the body of the long method with an instantiation of the method object and a call to the new method.

7. **Refactor Method Object**: Now that you have a method object, you can start breaking down the method into smaller, more manageable methods.

8. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public class OrderCalculator
{
    // A complex method that's hard to refactor
    public double CalculateOrder(Order order, Customer customer)
    {
        double total = 0;
        // Many lines of code and local variables
        // ...
        return total;
    }
}
```

After applying "Replace Method with Method Object" refactoring:

```csharp
public class OrderCalculator
{
    public double CalculateOrder(Order order, Customer customer)
    {
        return new OrderCalculation(order, customer).Compute();
    }
}

public class OrderCalculation
{
    private Order order;
    private Customer customer;
    private double total;

    public OrderCalculation(Order order, Customer customer)
    {
        this.order = order;
        this.customer = customer;
        this.total = 0;
    }

    public double Compute()
    {
        // Original method's code, now able to be refactored further
        // ...
        return total;
    }
}
```

In this example, the `CalculateOrder` method has been replaced with a `OrderCalculation` class, which takes `Order` and `Customer` as arguments to its constructor. The `total` variable, along with any other local variables, becomes fields of the `OrderCalculation` class. The `OrderCalculator` class now delegates the calculation to the `OrderCalculation` object. This setup allows for further refactoring within the `OrderCalculation` class, breaking down the `Compute` method into smaller, more focused methods.