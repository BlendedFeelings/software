---
b: https://blendedfeelings.com/software/design/sequential-convoy-pattern.md
---

# Sequential Convoy pattern 
is a messaging pattern used in software architecture, particularly in the context of enterprise integration and service-oriented architectures (SOA). The pattern is designed to process a sequence of related messages in a specific order. It is called a "convoy" because the sequence of messages travels together through the system, much like vehicles in a convoy.

Here are some key characteristics of the Sequential Convoy pattern:

1. **Ordering**: The messages must be processed in a particular order. This is critical when the order of operations affects the outcome.

2. **Correlation**: Messages in a convoy are related to each other and must be correlated. This correlation can be based on a common identifier or property within the messages.

3. **Single Process**: Messages are typically processed by a single logical receiver or process to maintain the order. This process is responsible for coordinating the sequence of message processing.

4. **State Management**: The process handling the convoy may need to maintain state information between messages. This state helps to determine what processing should be done as each message arrives.

5. **Atomic Processing**: Each message in the sequence may need to be processed atomically to ensure that the entire sequence is either completed successfully or can be rolled back in case of a failure.

6. **Exception Handling**: Proper exception handling is crucial to deal with any errors that occur during the processing of the convoy. This includes compensating actions if a part of the sequence fails.

The Sequential Convoy pattern is commonly implemented using message queues, where messages are enqueued in the order they must be processed. A processor then dequeots and processes each message in sequence. Workflow engines or orchestration services can also implement convoys by managing the state and order of message processing.

This pattern is useful when dealing with scenarios like processing financial transactions, order processing systems, and any other domain where the sequence of operations is essential.

However, the pattern also introduces complexity, as it requires careful design to ensure that messages are processed in order, that the state is consistently maintained, and that the system can handle failures gracefully. It can also have performance implications, as the need to maintain order can limit concurrency and throughput.