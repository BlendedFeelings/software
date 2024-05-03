---
b: https://blendedfeelings.com/software/domain-driven-design/transactional-outbox-pattern.md
---

# Transactional Outbox Pattern 
is a strategy used in domain-driven design (DDD) to ensure reliable messaging when dealing with operations that update a database and send messages or events. It's particularly useful in microservices architectures where you want to maintain atomicity across local database transactions and message publishing, without resorting to distributed transactions, which are complex and often not performant.

The pattern works by introducing an "outbox" table within the same database transaction where the business logic is executed. Here's how it typically works:

1. **Local Transaction Execution**: When an operation occurs that requires changes to the database and also needs to send a message or event, the changes to the database and the message/event are saved within a local database transaction. The message/event is not sent directly to the message broker but is instead inserted into the outbox table as part of the same transaction.

2. **Committing the Transaction**: If the transaction is successful, both the business data and the outbox message are committed together. This ensures that either both the business change and the message are saved, or neither is, which maintains consistency.

3. **Reliable Messaging**: A separate process (which can be a background service, scheduled job, etc.) regularly polls the outbox table for unsent messages. When it finds them, it publishes these messages to the message broker.

4. **Message Deletion or Flagging**: Once the message has been successfully published, the outbox entry can be safely removed or marked as sent to prevent it from being reprocessed.

5. **Idempotence Handling**: The system should handle idempotence to ensure that if a message is inadvertently sent more than once, consumers can recognize and discard duplicate messages.

Benefits of the Transactional Outbox Pattern include:

- **Atomicity**: Ensures that the business operation and message publishing are atomic without the need for distributed transactions.
- **Reliability**: If the application crashes after committing the transaction but before the message can be published, the separate process will ensure the message eventually gets sent.
- **Consistency**: The database and the messages/events remain consistent with each other.
- **Scalability**: The pattern can help the system scale by decoupling the message publishing from the main business logic.

Challenges to consider:

- **Complexity**: Implementing the pattern adds complexity to the system, as you need additional infrastructure to manage the outbox and message publishing.
- **Polling Overhead**: The process that polls the outbox table can add load to the database, especially if polling is done frequently.
- **Eventual Consistency**: The system is eventually consistent, which may not be suitable for all use cases.

When applying the Transactional Outbox Pattern in a DDD context, it's essential to align the outbox messages with the domain events that arise from the domain model. This way, the domain model remains the source of truth for the business logic, while the outbox ensures reliable communication with other parts of the system.