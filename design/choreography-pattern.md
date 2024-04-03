---
b: https://blendedfeelings.com/software/design/choreography-pattern.md
---

# Choreography pattern 
in software architecture is a way of designing distributed systems where services interact with each other through events rather than through a central orchestrator or controller. This pattern is particularly useful in microservices architectures, where it can help to create systems that are more loosely coupled and scalable.

Here's how the choreography pattern works:

1. **Decentralized Decision Making**: Each service in the system is autonomous and makes decisions based on the information it has. There is no central point of control.

2. **Event-based Communication**: Services communicate by publishing events. An event is a record of an action that has taken place. Other services listen for events that they are interested in and react accordingly.

3. **Reactive Services**: Services react to events they are interested in. When an event is detected, a service will carry out a task or series of tasks, which may include publishing more events.

4. **Loose Coupling**: Services do not need to know about the internal workings of other services. They only need to know what events are available to listen to and what those events mean. This reduces the dependencies between services.

5. **Scalability**: Since services are loosely coupled and communicate through events, it is easier to scale the system. Services can be scaled independently of each other.

6. **Flexibility and Agility**: New services can be added to the system by simply allowing them to participate in the event stream. They can publish new events and react to existing ones without needing to change other services.

7. **Complexity Management**: Although the choreography pattern can reduce coupling, it can also lead to complex systems where the flow of events is difficult to track and understand. This can make debugging and maintaining the system more challenging.

8. **Eventual Consistency**: The choreography pattern often leads to a system that is eventually consistent rather than immediately consistent. This means that it may take some time for the system to reach a consistent state after an event occurs.

In summary, the choreography pattern is a way of designing systems where services work together by reacting to events rather than being told what to do by a central authority. This can lead to more flexible, scalable, and resilient systems, but it also introduces challenges in terms of complexity and consistency.