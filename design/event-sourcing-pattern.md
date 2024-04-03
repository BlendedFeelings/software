---
b: https://blendedfeelings.com/software/design/event-sourcing-pattern.md
---

# Event Sourcing pattern
is a software architecture pattern that revolves around capturing all changes to an application state as a sequence of events. Instead of storing just the current state of the data in a domain, Event Sourcing involves storing the sequence of state-changing events. Whenever the state of a business entity changes, a new event is appended to the list of events. Since events are immutable, they cannot be changed once they have been added.

Here's how it works and some of its characteristics:

1. **Event Representation**: Each event represents a fact that occurred in the system at a point in time. An event typically contains the event type, the data that changed, and a timestamp.

2. **Event Storage**: Events are stored in an append-only store, which acts as the system's authoritative source of history. This store is often referred to as the "event store" or "event log".

3. **State Reconstruction**: The current state of the system can be reconstructed by replaying the events from the event store. This process is known as "event playback" or "event projection".

4. **Immutability**: Once events are stored, they should not be changed. This immutability guarantees the complete history of changes for each entity.

5. **Decoupling**: Event Sourcing can help in decoupling the state of the system from the code that changes it, which can simplify complex business logic.

6. **Querying State**: To query the current state, the system can maintain one or more projections of the event store. These projections are read-models that are kept up to date by listening to the stream of events.

7. **Event Handlers/Processors**: These components handle incoming events and update the projections accordingly.

8. **CQRS**: Event Sourcing is often used in conjunction with Command Query Responsibility Segregation (CQRS), which separates the read and write models of an application.

Benefits of Event Sourcing:
- **Audit Trail**: Since all changes are stored as events, it provides a complete audit trail that can be useful for debugging, auditing, and regulatory compliance.
- **Complex Event Processing**: It facilitates complex event processing and analysis, which can be useful for triggering workflows, analytics, or business intelligence.
- **Temporal Queries**: It allows for temporal queries, meaning you can determine the state of the system at any point in time.
- **Resilience**: It can increase system resilience, as events can be replayed to recover from crashes or to migrate to new systems.

Challenges of Event Sourcing:
- **Event Schema Evolution**: As the system evolves, you may need to deal with changes to the event schema, which can be complex.
- **Performance**: Replaying a large number of events to reconstruct state can be performance-intensive, although snapshotting can mitigate this.
- **Complexity**: Introducing Event Sourcing can add complexity to the system, especially if the team is not familiar with the pattern.
- **Upfront Design**: It requires careful upfront design to identify domain events and ensure they are meaningful and correctly capture business requirements.

Event Sourcing is particularly well-suited to systems where the audit trail and history of operations are important, such as financial systems, e-commerce, and systems that deal with complex business rules and processes.