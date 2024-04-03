---
b: https://blendedfeelings.com/software/domain-driven-design/factory.md
---

# Factories 
in Domain-Driven Design (DDD), are design patterns that handle the creation of complex domain objects and Aggregates. They encapsulate the logic for creating instances, ensuring that these objects are created in a valid and consistent state. Factories are particularly useful when the creation process is complex, involves validation, or requires setting up relationships between objects.

### Purpose of Factories:

1. **Encapsulating Creation Logic**: Factories encapsulate the logic and details involved in creating instances of domain objects, which can include setting initial state, validation, and applying business rules.

2. **Ensuring Validity**: They ensure that newly created objects are in a valid state and adhere to invariants required by the domain.

3. **Complex Construction**: For complex domain objects that require intricate setup, factories can manage these details, keeping the client code simple.

4. **Consistency**: By centralizing the creation logic, factories help maintain consistency in how instances of domain objects are created throughout the application.

### Characteristics of Factories:

- **Separation of Concerns**: Factories separate the responsibility of creating objects from the objects themselves, which can help keep the domain model clean.

- **Clear Intent**: The methods in a factory make it clear what kinds of objects are being created and for what purpose.

- **Immutable Objects**: Factories are particularly useful for creating immutable objects, as they can ensure that all necessary data is provided at the time of creation.

### Examples of Factory Usage:

- A `CustomerFactory` that creates a `Customer` Aggregate with default settings and validates the provided information.
- An `OrderFactory` that creates an `Order` Aggregate and automatically generates an order number and sets the order date.

### How to Implement Factories:

Factories are typically implemented as classes or static methods that provide a way to create domain objects. Here is a simple example in C#:

```csharp
public class OrderFactory
{
    public Order CreateOrder(Customer customer, IEnumerable<OrderLine> orderLines)
    {
        if (customer == null)
            throw new ArgumentNullException(nameof(customer));

        if (orderLines == null || !orderLines.Any())
            throw new ArgumentException("Order must have at least one order line.");

        // Apply any additional business rules or validations
        // ...

        var order = new Order(customer.Id, DateTime.UtcNow);
        foreach (var line in orderLines)
        {
            order.AddOrderLine(line.Product, line.Quantity);
        }

        return order;
    }
}

public class Order
{
    public Guid Id { get; private set; }
    public Guid CustomerId { get; private set; }
    public DateTime OrderDate { get; private set; }
    private List<OrderLine> orderLines = new List<OrderLine>();

    public Order(Guid customerId, DateTime orderDate)
    {
        Id = Guid.NewGuid();
        CustomerId = customerId;
        OrderDate = orderDate;
    }

    public void AddOrderLine(Product product, int quantity)
    {
        // Business rules and validations for adding order lines
        // ...
        orderLines.Add(new OrderLine(product, quantity));
    }

    // Other methods and properties
}

public class OrderLine
{
    public Product Product { get; private set; }
    public int Quantity { get; private set; }

    public OrderLine(Product product, int quantity)
    {
        Product = product;
        Quantity = quantity;
    }

    // Other methods and properties
}
```

### Considerations When Working with Factories:

- **Choosing Factory Location**: Decide whether to use a dedicated factory class, factory methods within the domain object class, or a static factory method.

- **Complexity**: Use factories for objects whose creation is complex enough to justify the abstraction. Simple objects may not need a factory.

- **Parameters**: Ensure that factory methods require all necessary parameters to create a valid object.

- **Dependency Injection**: If a factory has dependencies (e.g., services needed to create an object), consider using dependency injection to provide these dependencies.

Factories play a crucial role in DDD by ensuring that complex domain objects are created properly and remain consistent with the domain's rules and constraints. They help to keep the domain model focused on expressing the domain while handling object creation complexities behind the scenes.