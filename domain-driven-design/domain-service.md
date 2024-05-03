---
b: https://blendedfeelings.com/software/domain-driven-design/domain-service.md
---

# Domain services 
are a core concept used to encapsulate complex business logic that doesn't naturally fit within an entity or a value object. Domain services are part of the domain layer, which is one of the layers in the typical DDD architecture. Here's a breakdown of what domain services are and how they are used:

1. **Definition**: Domain services are stateless operations or activities that express domain concepts and business rules that are not the responsibility of a single entity or value object. They often represent actions or transactions in the domain that involve multiple domain objects.

2. **Characteristics**:
   - **Stateless**: Unlike entities, domain services do not have a persistent state. They encapsulate logic and can use entities and value objects to perform their tasks.
   - **Domain Logic**: Domain services contain business logic that doesn't belong to any single entity or value object.
   - **Reusable**: They can be reused across different parts of the application where the same domain logic is required.

3. **When to Use**:
   - When an operation or business rule involves multiple entities or value objects.
   - When an operation is part of the ubiquitous language but does not naturally fit within an entity or value object.
   - To prevent bloating entities with too much logic or behavior that is not core to the entity itself.

4. **Examples**:
   - A `TransferService` in a banking application that handles the logic for transferring funds between accounts.
   - An `OrderCalculationService` that calculates the total price of an order, applying discounts, taxes, and other business rules.

5. **Implementation**:
   - Domain services are implemented as classes in the domain layer.
   - They should have clear, intention-revealing names that reflect the domain language.
   - They should have well-defined interfaces that other parts of the application can interact with.
   - They can depend on repositories to retrieve and persist entities, but they should not contain data access logic themselves.

6. **Interaction with Other DDD Elements**:
   - Domain services can be used by application services to perform tasks that involve domain logic.
   - They can orchestrate the interaction between entities and value objects to carry out complex business operations.

7. **Design Considerations**:
   - Keep domain services focused on domain logic and avoid mixing in application or infrastructure concerns.
   - Avoid creating large, monolithic services; instead, focus on small, cohesive services that handle one aspect of the domain well.
   - Use dependency injection to provide domain services with any resources they need to perform their tasks.

In summary, domain services in DDD are a design pattern used to encapsulate business logic that spans multiple domain objects and doesn't naturally fit within an entity or value object. They help keep the domain model clean and focused while allowing complex business processes to be modeled and implemented effectively.