---
b: https://blendedfeelings.com/software/domain-driven-design/aggregate.md
---

# Aggregate 
is a cluster of domain objects that can be treated as a single unit for the purpose of data changes. Each Aggregate has a root and a boundary. The boundary defines what is inside the Aggregate. The root is a single, specific Entity contained in the Aggregate, and it is the only member of the Aggregate that outside objects are allowed to hold references to.

### Purpose of Aggregates:

1. **Enforce Invariants**: Aggregates enforce business rules (invariants) that must be consistent within the Aggregate boundary after each transaction.

2. **Manage Transactions**: Changes within the Aggregate are applied together in a single transaction. You can't change just part of an Aggregate without considering the whole.

3. **Reduce Complexity**: By treating the Aggregate as a single unit, you reduce the complexity of the model and the interactions between objects.

4. **Simplify Design**: Aggregates provide a simpler model for dealing with concurrency and transactional consistency.

### Characteristics of Aggregates:

- **Root Entity**: Each Aggregate has a root Entity, known as the Aggregate Root, which is the only object that outside objects are allowed to hold references to.
- **Boundary**: The Aggregate boundary is defined by the Aggregate Root, which encapsulates the other Entities and Value Objects within the Aggregate.
- **Consistency Boundaries**: The Aggregate Root ensures the consistency of changes being made within the Aggregate by controlling all access to the contained objects.
- **Size**: Aggregates should be designed to be as small as possible while still protecting business invariants.

### Examples of Aggregates:

- An `Order` Aggregate in an e-commerce system, with the `Order` Entity as the Aggregate Root and `LineItem` Entities and `Address` Value Objects as part of the Aggregate.
- A `Customer` Aggregate in a CRM system, with the `Customer` Entity as the Aggregate Root and `Address` and `PaymentMethod` Value Objects as part of the Aggregate.

### How to Implement Aggregates:

In code, an Aggregate is typically implemented as a class hierarchy with the Aggregate Root being the parent class. Here is an example in C#:

```csharp
public class Order // Aggregate Root
{
    public Guid Id { get; private set; }
    private List<LineItem> lineItems = new List<LineItem>(); // Encapsulated within the Aggregate
    public Address ShippingAddress { get; private set; }

    public Order(Address shippingAddress)
    {
        Id = Guid.NewGuid();
        ShippingAddress = shippingAddress;
    }

    public void AddLineItem(Product product, int quantity)
    {
        // Business rules and invariants are enforced here
        if (quantity <= 0)
            throw new InvalidOperationException("Quantity must be greater than zero.");

        lineItems.Add(new LineItem(product, quantity));
    }

    // Additional methods that operate on the Aggregate go here
}

public class LineItem // Part of the Aggregate
{
    public Product Product { get; }
    public int Quantity { get; }

    public LineItem(Product product, int quantity)
    {
        Product = product;
        Quantity = quantity;
    }
}
```

### Considerations When Working with Aggregates:

- **Designing Boundaries**: Carefully design Aggregate boundaries to ensure they make sense from a business perspective and protect invariants.
- **Reference by Identity**: Outside the Aggregate boundary, refer to other Aggregates only by their identity (usually through the Aggregate Root's ID).
- **Loading and Persistence**: Design repositories to handle the retrieval and persistence of Aggregates as whole units.
- **Concurrency**: Consider using optimistic concurrency control to handle concurrent updates to Aggregates, as locks can become a bottleneck.

Aggregates are a key concept in DDD that help maintain consistency and enforce business rules within a specific context of the domain. They simplify the design of the domain model and make it easier to reason about changes and transactions.