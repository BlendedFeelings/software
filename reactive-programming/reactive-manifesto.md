---
b: https://blendedfeelings.com/software/reactive-programming/reactive-manifesto.md
---

# Reactive Manifesto 
is a document that defines a set of principles for building systems that are robust, resilient, flexible, and message-driven. It was first introduced in 2013 by Jonas Bonér, Dave Farley, Roland Kuhn, and Martin Thompson. The manifesto advocates for systems that are more responsive to users and more resilient to failure, which is particularly important in modern distributed systems where components can fail independently.

The Reactive Manifesto outlines four key traits of reactive systems:

1. **Responsive**: The system should respond in a timely manner if at all possible. Responsiveness is the cornerstone of usability and utility, but more importantly, it means that problems may be detected quickly and dealt with effectively.

2. **Resilient**: The system should stay responsive in the face of failure. This applies not only to high-availability, mission-critical systems but also to systems that can gracefully handle and recover from errors.

3. **Elastic**: The system should stay responsive under varying workloads. Reactive systems can react to changes in the input rate by increasing or decreasing the resources allocated to service inputs. This implies designs that have no contention points or central bottlenecks, allowing for scaling out within and across nodes.

4. **Message Driven**: Reactive systems rely on asynchronous message-passing to establish a boundary between components that ensures loose coupling, isolation, and location transparency. This boundary also provides the means to delegate errors as messages.

Building systems that adhere to these principles often involves using certain architectural patterns such as Event Sourcing, Command Query Responsibility Segregation (CQRS), and implementing microservices using frameworks that facilitate asynchronous message handling, like Akka or Vert.x.

The Reactive Manifesto has influenced the design of many systems and frameworks, especially in the realm of distributed computing and microservices architecture. It's also closely related to the principles behind the development of reactive programming and reactive streams, which are about dealing with data streams asynchronously and with non-blocking back pressure.

For more information, you can visit the official website of the Reactive Manifesto: [https://www.reactivemanifesto.org/](https://www.reactivemanifesto.org/)