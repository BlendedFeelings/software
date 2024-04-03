---
b: https://blendedfeelings.com/software/design/causality.md
---

# Causality
refers to the relationship between events that happen across different nodes in a system where there is no global clock to synchronize time. Establishing causality is crucial for understanding the order of events and for ensuring consistency in the system. It's a fundamental concept that helps to address various challenges in distributed computing, such as concurrency control, fault tolerance, and event ordering.

In a distributed system, events can occur concurrently, and without a way to establish causality, it can be difficult to determine the order in which these events occurred. To tackle this, distributed systems often use logical clocks and ordering mechanisms. Here are some key concepts related to causality in distributed systems:

1. **Lamport Timestamps**: Leslie Lamport introduced the concept of logical clocks to order events. A Lamport timestamp is a counter that is incremented every time a process performs an action. When a message is sent, the sender includes its current counter value. Upon receiving a message, the receiver updates its counter to be at least as large as the one received plus one.

2. **Vector Clocks**: An extension of Lamport timestamps, vector clocks allow for partial ordering of events and can determine if two events are causally related or concurrent. Each process maintains a vector of counters, one for each process in the system. The vector is updated similarly to Lamport timestamps, but it provides more detailed information about causality.

3. **Happened-before Relation**: Defined by Lamport, the happened-before relation is a way to establish causality between events. If event A happened before event B, then A causally affects B. The rules are:
   - If events A and B are in the same process, and A comes before B, then A happened-before B.
   - If event A is the sending of a message and event B is the receipt of that message, then A happened-before B.
   - If A happened-before B and B happened-before C, then A happened-before C (transitivity).

4. **Causal Ordering**: Ensuring that messages are delivered in the order that respects the happened-before relation. This is crucial for maintaining consistency in the state of different processes.

5. **Consistency Models**: Different models define the level of consistency required in a distributed system. For example, causal consistency ensures that causally related updates are seen by all processes in the same order, while other models like eventual consistency are more lenient.

6. **Distributed Transactions**: Mechanisms like two-phase commit (2PC) and Paxos use concepts of causality to ensure that transactions are correctly committed or aborted across distributed nodes.

Causality is a complex issue in distributed systems due to the lack of a shared global state and the potential for network delays and partitions. By using logical clocks and other ordering mechanisms, distributed systems can establish causality and ensure that the system behaves in a predictable and reliable manner, despite the inherent challenges of distributed computing.