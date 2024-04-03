---
b: https://blendedfeelings.com/software/clean-architecture/use-case.md
---

# Use Cases
in clean architecture, represent the application-specific business rules. They encapsulate the logic of what the application can do for the user and define the interactions between the external world (such as a user or an external service) and the system's entities. Use cases orchestrate the flow of data to and from the entities, and they direct the entities to use their enterprise-wide business rules to achieve the goals of the application.

### Characteristics of Use Cases:

1. **Application-Specific**: Use cases are tailored to the needs of the application and describe how the user's goals are accomplished using the system.

2. **Encapsulation of Business Logic**: They contain the logic that is specific to the operation being performed, such as creating a new order, updating a customer profile, or generating a report.

3. **Interaction with Entities**: Use cases interact with entities to ensure that business rules are followed and that the correct data is manipulated.

4. **Boundary**: They define a clear boundary around the application, often represented by interfaces (input and output ports) that separate the use case's logic from the external world.

5. **Data Flow**: Use cases control the flow of data into and out of the system, typically involving data transformation between the format most suitable for entities and the format needed for external presentation or storage.

6. **Independence**: They are independent of external concerns such as user interfaces, databases, and other external agencies, which allows them to be tested in isolation.

### Implementation:

Use cases are often implemented as classes or methods that are called by interface adapters, such as controllers in a web application or UI presenters. Here's an example of what a use case might look like in C#:

```csharp
public interface IPlaceOrderUseCase
{
    void Execute(OrderData orderData);
}

public class PlaceOrderUseCase : IPlaceOrderUseCase
{
    private readonly IOrderRepository _orderRepository;

    public PlaceOrderUseCase(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }

    public void Execute(OrderData orderData)
    {
        // Convert OrderData (input data structure) to Order entity
        var order = new Order(orderData.Id, orderData.OrderDate);
        foreach (var item in orderData.Items)
        {
            order.AddItem(new OrderItem(item.ProductId, item.ProductName, item.Price, item.Quantity));
        }

        // Business logic to validate and place the order
        ValidateOrder(order);
        _orderRepository.Save(order);
    }

    private void ValidateOrder(Order order)
    {
        // Perform validation on the order
        if (!order.Items.Any())
        {
            throw new InvalidOperationException("An order must have at least one item.");
        }

        // Additional validation logic...
    }
}

public class OrderData
{
    public int Id { get; set; }
    public DateTime OrderDate { get; set; }
    public List<OrderItemData> Items { get; set; }
}

public class OrderItemData
{
    public int ProductId { get; set; }
    public string ProductName { get; set; }
    public decimal Price { get; set; }
    public int Quantity { get; set; }
}
```

In this example, the `PlaceOrderUseCase` class implements the `IPlaceOrderUseCase` interface, representing the use case for placing an order. It uses an `IOrderRepository` to interact with the persistence layer, thus keeping the use case independent of the database details. The `OrderData` and `OrderItemData` classes are simple data structures that carry data from the outside world into the use case.

Use cases should be designed to focus on what the system needs to do to deliver value to the end-user, encapsulating and directing the application logic while remaining decoupled from external concerns.