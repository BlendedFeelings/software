---
b: https://blendedfeelings.com/software/design/reliable-causal-broadcast.md
---

# Reliable causal broadcast 
is a communication primitive that ensures messages are reliably delivered and that the delivery respects the causal order of messages. This means that if a message m1 causally precedes another message m2, then m2 will not be delivered before m1.

Here's a summary of the properties a reliable causal broadcast system typically guarantees:

- **Reliability**: Every message that is sent is eventually delivered to all non-faulty processes.
- **Causality**: If a message m1 causally precedes another message m2, then every process delivers m1 before m2.

To implement reliable causal broadcast, systems often use vector clocks or similar mechanisms to track the causal dependencies between messages. Here's a high-level overview of how a simple reliable causal broadcast protocol might work:

1. Each process maintains a vector clock, which is an array of integers that track the number of messages sent by each process.
2. When a process sends a message, it increments its own entry in its vector clock and attaches the updated vector clock to the message.
3. Upon receiving a message, a process checks if the message can be delivered by comparing the attached vector clock with its own. If the message's vector clock is causally consistent with the receiver's vector clock, the message is delivered; otherwise, it is buffered until it can be delivered causally.
4. After delivering a message, the process updates its vector clock by taking the element-wise maximum of its own vector clock and the vector clock from the message.

This is a simplified description, and actual implementations may vary in complexity to handle various edge cases and optimisations. Reliable causal broadcast is a foundational concept in distributed systems, especially in scenarios where the order of events is crucial, such as collaborative applications, state machine replication, and consistency protocols.