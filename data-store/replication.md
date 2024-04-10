---
b: https://blendedfeelings.com/software/data-store/replication.md
---

# Replication in distributed systems 
refers to the process of sharing information across multiple nodes (computers, servers, etc.) to ensure consistency and reliability. The goal of replication is to improve the availability of data and services by keeping multiple copies of data across different locations.

Here are some key concepts associated with replication in distributed systems:

1. **Consistency Models**: Different replication strategies provide different guarantees about how data is replicated and when it becomes visible to other nodes. Some common consistency models include:
   - **Strong Consistency**: Every read receives the most recent write for a data item.
   - **Eventual Consistency**: Updates will eventually propagate to all replicas, but readers might see old data.
   - **Causal Consistency**: Writes that are causally related must be seen by all processes in the same order. Concurrent writes may be seen in a different order on different nodes.

2. **Replication Strategies**:
   - **Master-Slave Replication**: One node is designated as the master (primary), and others are slaves (secondaries). The master handles all write operations, and slaves replicate the data from the master.
   - **Multi-Master Replication**: Multiple nodes can accept write operations. Conflicts are resolved using various algorithms.
   - **Peer-to-Peer Replication**: Nodes function as equals, without any designated master. Data is replicated among peers.

3. **Fault Tolerance**: Replication helps systems to be fault-tolerant, meaning they can continue to operate even if some nodes fail.

4. **Load Balancing**: Replication allows systems to balance the load by directing read operations to different replicas.

5. **Data Partitioning**: Sometimes, data is partitioned across different nodes to improve performance and scalability. Each node is responsible for a subset of the data.

6. **Synchronization**: Replicated data needs to be synchronized to maintain consistency. This can be done synchronously, where writes are not considered successful until all replicas acknowledge the write, or asynchronously, where writes proceed without waiting for all replicas.

7. **Conflict Resolution**: When multiple replicas can accept writes, conflicts can occur. Systems use various conflict resolution strategies like version vectors, vector clocks, or last-write-wins.

8. **State Machine Replication**: A replication method where replicas start in the same state and execute the same sequence of commands to stay in sync.

9. **Quorum**: A strategy to ensure that a certain minimum number of nodes agree on a write operation before it is committed, to maintain consistency.

10. **CAP Theorem**: It states that a distributed system can only simultaneously provide two out of the following three guarantees: Consistency (C), Availability (A), and Partition Tolerance (P).

Replication is a complex topic with many nuances, and the right approach depends on the specific requirements of the system being designed, such as its need for consistency, availability, latency, and fault tolerance.