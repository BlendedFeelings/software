---
b: https://blendedfeelings.com/software/refactoring/extract-method-refactoring.md
---

# Extract Method
refactoring technique involves taking a piece of code that can be grouped together, moving it out of the current method, and putting it into a new method with a name that explains the purpose of the method. This technique is often used to improve readability, reduce complexity, and facilitate code reuse.

Here's a step-by-step guide on how to apply the "Extract Method" refactoring technique:

1. **Identify Code to Extract**: Look for a code fragment that can be grouped together. This could be a block of code that performs a specific task or calculation that's distinct from the rest of the method.

2. **Create New Method**: Create a new method and name it in a way that clearly describes what the code does. The method name should be a verb or a phrase that expresses the method's action or purpose.

3. **Move Code**: Copy the identified code fragment into the new method. If the code fragment uses local variables from the original method, you'll need to pass these as parameters to the new method.

4. **Replace Original Code with Method Call**: Replace the original code fragment with a call to the new method. Pass any necessary arguments.

5. **Test**: Ensure that the behavior of the program hasn't changed by running tests. This step is crucial to confirm that the refactoring hasn't introduced any bugs.

Here's an example in C#:

Before refactoring:

```csharp
public void PrintInvoice()
{
    // Calculate total amount
    double totalAmount = 0;
    foreach (var item in invoiceItems)
    {
        totalAmount += item.Price * item.Quantity;
    }
    totalAmount += totalAmount * taxRate;

    // Print the invoice
    Console.WriteLine("Total Amount: " + totalAmount.ToString("C"));
}
```

After applying "Extract Method" refactoring:

```csharp
public void PrintInvoice()
{
    double totalAmount = CalculateTotalAmount(invoiceItems, taxRate);
    Console.WriteLine("Total Amount: " + totalAmount.ToString("C"));
}

private double CalculateTotalAmount(List<InvoiceItem> items, double taxRate)
{
    double totalAmount = 0;
    foreach (var item in items)
    {
        totalAmount += item.Price * item.Quantity;
    }
    totalAmount += totalAmount * taxRate;
    return totalAmount;
}
```

In this example, the code for calculating the total amount of the invoice has been extracted into its own method called `CalculateTotalAmount`. This makes the `PrintInvoice` method more readable and allows the calculation logic to be reused elsewhere if needed.