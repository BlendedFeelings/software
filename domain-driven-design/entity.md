---
b: https://blendedfeelings.com/software/domain-driven-design/entity.md
---

# Entity 
is one of the two primary building blocks of the domain model (the other being Value Objects). Entities are objects that have a distinct identity that runs through time and different states. They are defined not just by their attributes, but by a thread of continuity and identity.

### Characteristics of Entities:

1. **Identity**: Entities have a unique identifier that distinguishes them from other entities. This identity usually persists for the entire life cycle of the entity, even if other attributes change.

2. **Mutability**: Unlike Value Objects, Entities can change over time. Their attributes might change, but their identity remains constant.

3. **Life Cycle**: Entities can go through a complex life cycle, being created, updated, and eventually possibly deleted, while still maintaining their identity.

4. **Equality**: Equality of entities is based on identity, not on attribute values. Two entities are considered equal if their identities are equal, regardless of differences in other attributes.

5. **Encapsulation**: Entities encapsulate both state (data) and behavior (methods or functions that operate on the data). The behavior typically includes business logic that applies to the entity.

### Examples of Entities:

- A `Customer` in an e-commerce system, identified by a customer ID.
- An `Order` in an order processing system, identified by an order number.
- An `Account` in a banking application, identified by an account number.

### How to Implement Entities:

In code, an entity is typically implemented as a class (or equivalent in non-object-oriented languages) with a unique identifier and methods that encapsulate the entity's behavior. Here is a simple example in C#:

```csharp
public class Customer
{
    public Guid Id { get; private set; }
    public string Name { get; set; }
    public string Email { get; set; }

    public Customer(string name, string email)
    {
        Id = Guid.NewGuid(); // Assign a unique identifier
        Name = name;
        Email = email;
    }

    // Additional methods to encapsulate behavior would go here
}
```

### Considerations When Working with Entities:

- **Identity Generation**: Decide how identities are generated. They can be created by the system (e.g., GUIDs, auto-incrementing IDs) or provided by external sources (e.g., user-provided account numbers).
- **Consistency**: Ensure that the entity's state is always consistent. Changes to the state should be validated against business rules.
- **Persistence**: Entities are often persisted to a database. The persistence mechanism should respect the entity's identity and ensure it is maintained across transactions.
- **Concurrency**: When entities are accessed concurrently, you need to handle conflicts that may arise from concurrent modifications.

Entities are a crucial part of any DDD-based system, allowing the representation of real-world objects that have a distinct identity and are subject to change over time. Properly identifying and implementing entities is essential for creating a model that accurately reflects the business domain and its rules.