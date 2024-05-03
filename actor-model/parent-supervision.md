---
b: https://blendedfeelings.com/software/actor-model/parent-supervision.md
---

# Supervision 
refers to the strategy of managing actors' lifecycles and their responses to failure. Parent supervision is a pattern where each actor is supervised by its parent actor. This means that when an actor is created, its parent is responsible for handling its failures and deciding what to do next.

Here are the key concepts of parent supervision in the Actor Model:

1. **Hierarchy**: Actors are organized in a hierarchy. When an actor creates another actor, the creator becomes the parent of the new actor. This parent is responsible for supervising its children.

2. **Supervision Strategy**: The parent actor defines a supervision strategy, which is a set of rules that determine what actions to take when a child actor fails. Common strategies include:
   - **Resume**: The child continues to run, maintaining its internal state.
   - **Restart**: The child is stopped and a new instance is started, with its state reset to the initial state.
   - **Stop**: The child is permanently stopped.
   - **Escalate**: The failure is reported to the parent's supervisor, escalating the problem up the hierarchy.

3. **Fault Tolerance**: The supervision strategy is a way to provide fault tolerance. By isolating failures to individual actors and having a strategy to deal with them, the system can recover from errors without affecting the entire application.

4. **Lifecycle Monitoring**: Parent actors can monitor their children's lifecycle events, such as starting, stopping, or crashing. This allows the parent to take appropriate action based on its supervision strategy.

5. **Encapsulation**: Just as actors encapsulate state and behavior, they also encapsulate failure. This means that the failure of an actor does not directly affect other actors. Instead, it is the responsibility of the supervisor to handle the failure according to the defined strategy.

6. **Message Passing**: All interactions between actors, including supervision directives, are done through asynchronous message passing. This decouples the actors and allows for flexible and dynamic supervision structures.

Popular frameworks that implement the Actor Model, such as Akka (for Scala and Java) and Orleans (for .NET), provide built-in support for the supervision of actors. These frameworks allow developers to easily define supervision strategies and manage actor hierarchies, making it simpler to build robust and resilient concurrent systems.