---
b: https://blendedfeelings.com/software/design/transactional-outbox-pattern.md
---

# Transactional Outbox Pattern 
is a strategy used in software architecture to ensure that changes to a database and messages/events to be sent to a message broker or event bus are handled atomically. This pattern is particularly useful in scenarios where you have a service that needs to update a database and publish an event, and you must ensure that both actions succeed or fail together. It helps to maintain data consistency across different services in a distributed system.

Here's how the pattern typically works:

1. **Local Transaction**: When an application performs an operation that requires changes to the database and also needs to send a message/event, it starts a local transaction.

2. **Database Update**: Within this transaction, the application first performs the necessary updates to the database.

3. **Outbox Table**: Instead of sending the message/event directly to the message broker, the application inserts a record into an "outbox" table within the same database. This record contains all the information needed to construct the message/event later on.

4. **Commit Transaction**: The transaction is then committed. At this point, the database changes are saved, and the outbox record is also stored atomically.

5. **Message Relay Process**: A separate process (sometimes called a "Relay" or "Publisher") periodically checks the outbox table for new records. When it finds them, it constructs and sends the corresponding messages/events to the message broker.

6. **Delete or Mark Record**: Once the message/event has been successfully published, the relay process either deletes the outbox record or marks it as sent, to avoid resending it.

7. **Handling Failures**: If the process of sending the message/event fails, the relay process can retry it. Since the outbox record is still present, no data is lost, and the system can ensure that the message/event is eventually delivered.

The benefits of the Transactional Outbox Pattern include:

- **Atomicity**: Ensures that the database updates and message/event publishing are treated as a single unit of work.

- **Reliability**: If a service crashes or fails before it can send the message/event, the outbox ensures that no messages/events are lost.

- **Consistency**: Helps maintain consistency across different parts of a distributed system by ensuring that messages/events are only published after the database transaction commits.

- **Simplicity**: Simplifies the transaction management in the service code because it only needs to handle a local database transaction.

Implementing the Transactional Outbox Pattern typically requires additional infrastructure to poll the outbox table and publish the messages/events, as well as additional logic to handle retries and deduplication of messages/events. It's important to consider the performance implications of polling the outbox table and to design the relay process to be scalable and resilient.