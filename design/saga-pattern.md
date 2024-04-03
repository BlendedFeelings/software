---
b: https://blendedfeelings.com/software/design/saga-pattern.md
---

# Saga pattern 
is a design pattern used to manage distributed transactions, which are transactions that span multiple services, each with its own database and transaction management. In a distributed system, the Saga pattern ensures data consistency across these services without the need for a global transaction manager, which would be a single point of failure and a bottleneck for scalability.

Here's how the Saga pattern typically works:

1. **Definition of Saga**: A Saga is defined as a sequence of local transactions. Each local transaction updates the database and publishes an event or message to trigger the next local transaction in the saga.

2. **Local Transactions**: Each service involved in the Saga performs its own local transaction. If the transaction is successful, it publishes an event indicating success and possibly triggering the next step in the Saga. If the transaction fails, it publishes an event indicating failure.

3. **Compensation Transactions**: If a local transaction fails after some transactions have already been completed, the Saga executes compensating transactions to undo the changes made by the preceding successful transactions. This ensures that the system returns to a consistent state.

4. **Event/Message-Driven**: Sagas rely on an event-driven or message-driven architecture to communicate between services. When a service completes its local transaction, it emits an event or sends a message that the next service listens for to begin its own transaction.

5. **Orchestration or Choreography**: There are two main ways to coordinate the transactions within a Saga:
   - **Orchestration**: A central coordinator (orchestrator) tells the participants what local transactions to execute. The orchestrator keeps track of the state of the Saga and decides what transaction to execute next based on the outcomes of the previous ones.
   - **Choreography**: Each service knows what to do next based on the events it listens to. There is no central coordination, as each service produces and listens to events, deciding on its actions autonomously.

6. **Failure Handling**: The design of Sagas includes strategies for dealing with failures, such as retries, timeouts, and compensating transactions, to ensure that the system can recover from errors and maintain data consistency.

7. **Monitoring and Visibility**: Due to the complexity of distributed transactions, it's important to have good monitoring and visibility into the state of Sagas to troubleshoot issues.

The Saga pattern is particularly useful in microservices architectures where different microservices manage their own data. It allows for loosely coupled services that can operate independently while maintaining data consistency across the system. However, implementing Sagas can be complex and requires careful design to handle failure scenarios properly.