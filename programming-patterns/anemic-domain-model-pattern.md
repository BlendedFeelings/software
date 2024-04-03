---
b: https://blendedfeelings.com/software/programming-patterns/anemic-domain-model-pattern.md
---

# Anemic Domain Model
is a term used in software development, particularly when discussing design patterns in the context of domain-driven design (DDD). It's a pejorative term that refers to a software domain model where the domain objects contain little or no business logic; they are merely data structures (collections of getters and setters) without the business rules that govern the data.

In an Anemic Domain Model, the business logic is typically implemented in separate service classes, which leads to a design where the logic is separated from the data it manipulates. This approach goes against the principles of object-oriented design, where data and the operations that manipulate that data are supposed to be encapsulated together in objects.

Here are some characteristics of an Anemic Domain Model:

**Lack of Encapsulation**: The domain entities (models) do not encapsulate any behavior. They are used purely for data transfer between layers or components.

**Service-Layer Heavy**: Most of the business logic resides in service layers, which operate on the domain entities to perform operations.

**Violation of OOP Principles**: It violates the object-oriented programming principle of combining data and behavior in classes.

**Focus on Data Structure**: The focus is on the structure of the data rather than on the behaviors and responsibilities of the domain entities.

**Increased Complexity**: It can lead to a proliferation of service classes and can make the system more complex and harder to maintain.

**Procedural Style**: The separation of data and behavior often leads to a more procedural style of programming rather than an object-oriented one.

An Anemic Domain Model is often the result of a design that has not considered the full benefits of object-oriented design, or it may be a deliberate choice due to certain architectural constraints or preferences. However, it's generally considered an anti-pattern in domain-driven design because it does not take full advantage of the capabilities of object-oriented programming to model complex business scenarios.

```java
// Anemic Domain Model
class Order {
    private long id;
    private List<OrderItem> items;

    void setId(long id) {
        this.id = id;
    }

    long getId() {
        return id;
    }

    void setItems(List<OrderItem> items) {
        this.items = items;
    }

    List<OrderItem> getItems() {
        return items;
    }
}

class OrderItem {
    private long id;
    private String name;
    private int quantity;
    private double price;

    void setId(long id) {
        this.id = id;
    }

    long getId() {
        return id;
    }

    void setName(String name) {
        this.name = name;
    }

    String getName() {
        return name;
    }

    void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    int getQuantity() {
        return quantity;
    }

    void setPrice(double price) {
        this.price = price;
    }

    double getPrice() {
        return price;
    }
}

// Service class
class OrderService {
    void placeOrder(Order order) {
        // Calculate total price
        double totalPrice = 0;
        for (OrderItem item : order.getItems()) {
            totalPrice += item.getPrice() * item.getQuantity();
        }

        // Save order to database
        OrderDAO orderDAO = new OrderDAO();
        orderDAO.saveOrder(order.getId(), totalPrice);
    }
}

// Usage
Order order = new Order();
OrderItem item1 = new OrderItem();
item1.setName("Item 1");
item1.setQuantity(2);
item1.setPrice(10.0);
OrderItem item2 = new OrderItem();
item2.setName("Item 2");
item2.setQuantity(1);
item2.setPrice(5.0);
List<OrderItem> items = new ArrayList<>();
items.add(item1);
items.add(item2);
order.setItems(items);
OrderService orderService = new OrderService();
orderService.placeOrder(order);
```