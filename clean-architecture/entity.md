---
b: https://blendedfeelings.com/software/clean-architecture/entity.md
---

# Entities
in the context of clean architecture, represent the business objects of the application. They encapsulate the most fundamental business rules and are the least likely to change when something external changes, such as the database or user interface. Entities are at the heart of the business logic and are typically independent of any specific technical implementation.

### Characteristics of Entities:

1. **Business Rules**: Entities embody the enterprise-wide business rules. These are the critical rules that define what it means to be a particular thing in the business context.

2. **High-Level**: They are high-level constructs that are often closely aligned with the real-world concepts relevant to the business domain.

3. **Stability**: Entities are stable in that they do not frequently change. When they do change, it's often due to a change in business rules rather than technical factors.

4. **Independence**: They are independent of the user interface, database structures, frameworks, and external agencies. This means that changes in these areas should not require changes to the entities.

5. **Self-Validation**: Entities can enforce integrity through self-validation by ensuring they are always in a valid state with respect to the business rules.

6. **Rich Model**: Entities can have both data and behavior, which means that they can contain methods that operate on their internal state.

### Implementation:

Entities are typically implemented as classes in object-oriented programming languages. Here's an example of what an entity might look like in C#:

```csharp
public class Order
{
    public int Id { get; private set; }
    public DateTime OrderDate { get; private set; }
    public List<OrderItem> Items { get; private set; }
    public decimal TotalAmount => Items.Sum(item => item.Price * item.Quantity);

    public Order(int id, DateTime orderDate)
    {
        Id = id;
        OrderDate = orderDate;
        Items = new List<OrderItem>();
    }

    public void AddItem(OrderItem item)
    {
        // Business rule: Item must not be null
        if (item == null)
        {
            throw new ArgumentNullException(nameof(item));
        }

        // Business rule: Duplicate items are not allowed
        if (Items.Any(existingItem => existingItem.ProductId == item.ProductId))
        {
            throw new InvalidOperationException("Item already added.");
        }

        Items.Add(item);
    }

    // Additional methods to manipulate the order...
}

public class OrderItem
{
    public int ProductId { get; private set; }
    public string ProductName { get; private set; }
    public decimal Price { get; private set; }
    public int Quantity { get; private set; }

    public OrderItem(int productId, string productName, decimal price, int quantity)
    {
        ProductId = productId;
        ProductName = productName;
        Price = price;
        Quantity = quantity;
    }
}
```

In this example, the `Order` class is an entity with business rules enforced through its methods, such as not allowing null items to be added and preventing duplicate items. The `OrderItem` class could also be considered an entity or a value object, depending on its role and behavior in the application.

Entities should be designed to be easily testable and maintainable, with clear and explicit boundaries defining their responsibilities. They should not be concerned with how they are stored or presented, focusing solely on representing concepts and rules within the business domain.