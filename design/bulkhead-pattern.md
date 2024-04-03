---
b: https://blendedfeelings.com/software/design/bulkhead-pattern.md
---

# Bulkhead pattern 
is a design pattern used in software architecture to prevent failures in one part of a system from cascading to other parts. The term "bulkhead" is borrowed from the maritime industry, where a bulkhead is a partition in a ship that creates watertight compartments. If one compartment is breached, the bulkheads contain the damage and prevent the ship from sinking.

In the context of software, the Bulkhead pattern involves organizing the system into multiple isolated components or services. Each component has its own set of resources, such as threads, memory, and network connections. By isolating these resources, you ensure that if one component becomes overloaded or fails, it does not affect the other components.

Here are some key points about the Bulkhead pattern:

1. **Isolation**: Components are isolated from each other, so that issues in one component (like a service or module) do not impact the others.

2. **Resource Allocation**: Each component has a dedicated set of resources. This prevents a situation where a failing component consumes all the resources, leaving nothing for the healthy ones.

3. **Resilience**: The system becomes more resilient to failures, as the problem is contained within a single component.

4. **Concurrent Processing**: The pattern allows for concurrent processing within the system. If one component is slow or failing, other components can still operate normally.

5. **Scalability**: It can improve the scalability of a system, as each component can be scaled independently based on its own load and performance characteristics.

6. **Fault Tolerance**: The system can continue to operate in a degraded mode even if one or more components fail.

Implementing the Bulkhead pattern typically involves:

- **Limiting Workloads**: Using techniques such as thread pools, connection pools, and rate limiters to restrict the number of concurrent calls to a component.
- **Timeouts**: Implementing timeouts to ensure that calls to a component do not wait indefinitely if the component is not responding.
- **Circuit Breakers**: Combining the Bulkhead pattern with the Circuit Breaker pattern to prevent repeated calls to a failing component.


The Bulkhead pattern is often used in microservices architectures but can be applied to any system where you want to contain failures and improve resilience.