---
b: https://blendedfeelings.com/software/design/decomposition-patterns.md
---

# Decomposition patterns 
are fundamental to [microservices architecture](microservices-architecture-pattern.md) because they guide how to break down a complex system into smaller, manageable, and independently deployable services. The goal is to create a system that is easier to understand, develop, test, and maintain. Here's a more detailed look at each of the decomposition patterns mentioned:

### Decompose by Business Capability
In this approach, the system is decomposed into microservices based on business capabilities. A business capability is a particular function or a set of related functions that the business performs to meet its objectives. Each microservice is responsible for all the data processing and business logic related to that capability. For example:

- **Inventory Service**: Manages stock levels, product information, and inventory transactions.
- **Billing Service**: Handles invoicing, payment processing, and financial records.
- **Ordering Service**: Manages customer orders, order fulfillment, and shipping.

This pattern aligns the service boundaries with the business domain, which often results in services that reflect the organization's structure and the way it does business. It also promotes a high level of cohesion within each service and loose coupling between services.

### Decompose by Subdomain
Following Domain-Driven Design (DDD), this pattern involves dividing the system into various subdomains, each of which represents a segment of the business domain. Subdomains are typically identified during the domain modeling phase and can be categorized as core, supporting, or generic:

- **Core Subdomains**: The key areas of the business that provide competitive advantage and are central to the business's success.
- **Supporting Subdomains**: Important to the business but do not offer a competitive advantage; they support the core subdomains.
- **Generic Subdomains**: Common functionalities that can be used across different businesses, such as user authentication or payment processing.

Each microservice in this pattern corresponds to a subdomain and encapsulates the domain logic, data, and user interfaces related to that subdomain. This pattern helps maintain a clear focus on the domain model and ensures that the microservices' boundaries align with natural business boundaries.

### Self-contained Service (SCS)
Self-contained Services are designed to be as autonomous as possible. Each SCS is an independent application that includes its user interface, business logic, and data storage. Services communicate with each other through well-defined APIs, and they should not share databases to avoid tight coupling.

The SCS pattern emphasizes the following principles:

- **Autonomy**: An SCS can be developed, deployed, scaled, and retired independently of other services.
- **Self-sufficiency**: Each SCS contains all the necessary components to fulfill its business capability, including its own UI and database.
- **Isolation**: SCSs are isolated from each other, which reduces the risk of cascading failures and simplifies the understanding of each service.

This pattern is particularly useful when you want to scale different parts of the system independently or when different teams are responsible for different services. It also simplifies deployment and allows for different technology stacks to be used in different services if needed.

When using decomposition patterns, it's important to carefully consider the size and scope of each microservice. Services should be large enough to perform meaningful business functions but small enough to be managed by a small development team. Striking the right balance is key to achieving the benefits of a microservices architecture.