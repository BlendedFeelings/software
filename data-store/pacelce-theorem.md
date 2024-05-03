---
b: https://blendedfeelings.com/software/data-store/pacelce-theorem.md
---

# PACELC theorem 
is an extension of the CAP theorem, which addresses the trade-offs in distributed computer systems regarding Consistency (C), Availability (A), and Partition Tolerance (P). The CAP theorem states that a distributed system can only satisfy two out of the three guarantees at any given time.

The PACELC theorem adds another dimension to this by stating that in case of network partitioning (P), a system must choose between Availability (A) and Consistency (C), but else (E), when the system is running normally in the absence of partitions, it must choose between Latency (L) and Consistency (C).

Here's a breakdown of the PACELC theorem:

- **P (Partition Tolerance)**: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.
- **A (Availability)**: Every request receives a response, without guarantee that it contains the most recent write.
- **C (Consistency)**: Every read receives the most recent write or an error.
- **E (Else)**: When the system is not experiencing a partition.
- **L (Latency)**: The time taken to respond to a request.

The PACELC theorem thus provides a more nuanced approach to understanding the trade-offs in distributed systems, particularly in how they behave under normal operation versus under network partitioning. It emphasizes that even when there are no partitions, there are still trade-offs to be made between consistency and latency.