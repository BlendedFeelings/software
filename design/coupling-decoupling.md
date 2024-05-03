---
b: https://blendedfeelings.com/software/design/coupling-decoupling.md
---

# Coupling and decoupling 
refer to the degree of direct knowledge that one component has about another. This concept is crucial when it comes to the maintainability and scalability of a system.

### Tight Coupling:
- **Tight coupling** is a scenario where two or more components are highly dependent on each other.
- Changes in one component often require changes in the other, leading to a "domino effect" where a single modification can necessitate a series of subsequent changes.
- This is often seen as a disadvantage because it makes the system more complex and harder to maintain.

### Loose Coupling:
- **Loose coupling** is the opposite: components are mostly independent, and changes in one component have little or no effect on others.
- This is generally preferred because it makes the system more modular, easier to manage, and more adaptable to change.

### Upstream -> Downstream:
- **Upstream** refers to the direction toward the source of a process or data flow.
- **Downstream** refers to the direction toward the end point or consumer of a process or data flow.
- In an upstream-downstream relationship, if an upstream component changes, it can affect the downstream components (they are "tightly coupled" to the upstream component). However, changes in a downstream component do not typically affect the upstream component (the upstream component is "loosely coupled" with regard to downstream changes).

### Customer - Supplier
In a customer-supplier relationship, the supplier provides a product or service, and the customer consumes it. The customer may request changes or improvements, and the supplier is responsible for implementing these changes to meet the customer's needs.
- This relationship can be seen in software where a service (supplier) provides an API that client applications (customers) consume.
- In a business context, a department that requires data from another department to complete its reports is the customer, and the department providing the data is the supplier.


To illustrate these concepts, consider a software application with two modules, A and B:

- In a tightly coupled system, changes to module A might require changes to module B and vice versa. This can create a brittle architecture that is difficult to maintain and evolve.
- In a loosely coupled system, module A can operate independently of module B. Changes to one module do not necessitate changes to the other, which encourages a more flexible and maintainable design.
- If module A is upstream of module B, changes in module A (like altering its output format) could force changes in module B, which relies on that output. However, changes in module B (downstream) would not typically require changes in module A.

In summary, tight coupling is generally something to avoid in system design, while loose coupling is encouraged. Upstream components can affect downstream components, but not necessarily the other way around.