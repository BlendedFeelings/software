---
b: https://blendedfeelings.com/software/domain-driven-design/domain-event.md
---

# Domain Events 
are a way of capturing significant business moments that domain experts care about. They are discrete events that denote state changes within the domain that are important for business reasons. Domain Events are used to explicitly implement side effects across different parts of the domain in a loosely coupled way.

### Purpose of Domain Events:

1. **Decoupling**: Domain Events enable parts of a system to react to actions occurring in other parts of the system without being tightly coupled to each other.

2. **Side Effect Management**: They help in managing side effects by providing a clear mechanism for triggering behavior in response to state changes.

3. **Intent Expression**: Domain Events express the intent of what happened in the domain, making the model more expressive and aligned with the business language.

4. **Reactivity**: They enable a reactive model where systems can respond to events as they occur.

5. **Audit and History**: Domain Events can be stored and used to create an audit log or history of what has happened in the system.

### Characteristics of Domain Events:

- **Named After Business Activity**: Domain Events are named after the business activity they represent, such as `OrderPlaced`, `InventoryDepleted`, or `CustomerUpgraded`.

- **Immutable**: Once raised, the event's data should not change.

- **Contains Event Data**: Events carry the data relevant to the business activity, such as the time of the event and the entities involved.

- **Can Trigger Workflows**: They can trigger workflows or processes in the same or other bounded contexts.

### Examples of Domain Events:

- `OrderPlacedEvent`: Raised when a customer places an order.
- `ProductShippedEvent`: Raised when a product is shipped to a customer.
- `AccountDebitedEvent`: Raised when an account is debited.

### How to Implement Domain Events:

In code, Domain Events are typically implemented as simple classes with properties that carry the event data. Here is an example in C#:

```csharp
public class OrderPlacedEvent
{
    public Guid OrderId { get; private set; }
    public DateTime OrderDate { get; private set; }
    public Guid CustomerId { get; private set; }

    public OrderPlacedEvent(Guid orderId, DateTime orderDate, Guid customerId)
    {
        OrderId = orderId;
        OrderDate = orderDate;
        CustomerId = customerId;
    }
}
```

### Considerations When Working with Domain Events:

- **Event Handling**: Decide whether events will be handled synchronously or asynchronously. Asynchronous handling can improve system performance and responsiveness but adds complexity.

- **Event Dispatching**: Implement an event dispatcher that can publish events to interested subscribers.

- **Subscriber Registration**: Subscribers need to register with the dispatcher to receive events.

- **Transaction Management**: Ensure that events are raised and handled in a way that respects transaction boundaries.

- **Persistence**: Consider whether and how to persist events for auditing or replay.

Domain Events are a powerful concept in DDD that can help to create a more maintainable, decoupled, and expressive domain model. They facilitate communication between different parts of the system and can be used to implement complex business processes and workflows.