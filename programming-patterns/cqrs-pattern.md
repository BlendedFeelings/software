---
b: https://blendedfeelings.com/software/programming-patterns/cqrs-pattern.md
---

# Command Query Responsibility (CQRS) pattern
separates the read and write operations into two different parts. The idea is to use separate models for reading and writing data, which allows for more flexibility and scalability in the application.
Write operations are handled by a command model, which is responsible for updating the application state. Read operations are handled by a separate query model, which is optimized for querying and returning data to the user.

Here's an overview of the key concepts:

**Commands**: These are operations that modify the state of the system. They could be actions like "Create an Order", "Update Customer Details", or "Delete a Product". Commands are executed by the command side of the system, often referred to as the write side. They typically do not return data and are intended to change the state of the application.

**Queries**: These are operations that retrieve data from the system without changing its state. Examples include "Get User Details", "List All Orders", or "Find Products by Category". Queries are executed by the query side, also known as the read side, and are designed to be read-optimized.

**Separation of Models**: In a typical CQRS implementation, there are separate models for reads and writes. The write model is optimized for transactional integrity and the read model is optimized for query performance. This can lead to a situation where the read model is a denormalized version of the write model, which can be updated asynchronously using events.

**Event Sourcing**: CQRS is often associated with Event Sourcing, although they can be used independently. Event Sourcing involves storing changes to the system's state as a sequence of events. These events can then be replayed to reconstruct the current state or to build up the read model.

**Benefits**: The main advantages of CQRS include improved scalability (by scaling reads and writes independently), increased flexibility (by allowing different data storage technologies for reads and writes), and better separation of concerns.

**Drawbacks**: CQRS can introduce complexity to the system, especially when combined with Event Sourcing. It may also result in eventual consistency between the read and write models, which can be challenging to handle in some business scenarios.

**Use Cases**: CQRS is particularly useful in systems where the read and write workloads are highly disparate, where performance for reads or writes needs to be optimized, or where the system needs to scale horizontally.

```java
// Command interface
interface Command {
    void execute();
}

// Concrete command
class CreateOrderCommand implements Command {
    private OrderRepository repository;
    private OrderDTO orderDTO;

    CreateOrderCommand(OrderRepository repository, OrderDTO orderDTO) {
        this.repository = repository;
        this.orderDTO = orderDTO;
    }

    void execute() {
        Order order = new Order(orderDTO);
        repository.save(order);
    }
}

// Query interface
interface Query<T> {
    T execute();
}

// Concrete query
class GetOrderQuery implements Query<Order> {
    private OrderRepository repository;
    private long orderId;

    GetOrderQuery(OrderRepository repository, long orderId) {
        this.repository = repository;
        this.orderId = orderId;
    }

    Order execute() {
        return repository.findById(orderId);
    }
}

// Repository interface
interface OrderRepository {
    void save(Order order);
    Order findById(long orderId);
}

// Data Transfer Object (DTO)
class OrderDTO {
    private String customerName;
    private List<OrderItemDTO> items;
}

class OrderItemDTO {
    private String name;
    private int quantity;
}

// Domain model
class Order {
    private long id;
    private String customerName;
    private List<OrderItem> items;

    Order(OrderDTO orderDTO) {
        this.customerName = orderDTO.getCustomerName();
        for (OrderItemDTO itemDTO : orderDTO.getItems())
            this.items.add(new OrderItem(itemDTO));
    }
}

class OrderItem {
    private String name;
    private int quantity;

    OrderItem(OrderItemDTO itemDTO) {
        this.name = itemDTO.getName();
        this.quantity = itemDTO.getQuantity();
    }
}

// Usage
OrderRepository repository = new OrderRepositoryImpl();
Command createOrderCommand = new CreateOrderCommand(repository, orderDTO);
createOrderCommand.execute();
Query<Order> getOrderQuery = new GetOrderQuery(repository, 1);
Order order = getOrderQuery.execute();
```