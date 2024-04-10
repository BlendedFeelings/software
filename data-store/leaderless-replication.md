---
b: https://blendedfeelings.com/software/design/leaderless-replication.md
---

# Leaderless replication 
is a distributed data replication strategy used in distributed databases and storage systems. Unlike traditional leader-based replication models, which rely on a single designated leader to coordinate updates and replication, leaderless replication allows any node to accept writes and updates. This model is designed to increase availability and fault tolerance, as there is no single point of failure.

Here's a brief overview of how leaderless replication typically works:

1. **Write Requests**: A client can send a write request to any node in the cluster. The node then replicates the data to other nodes in the system, often to a predefined number of nodes to ensure durability (this is sometimes referred to as the "replication factor").

2. **Read Requests**: When a client issues a read request, it can query any node or multiple nodes in the cluster. To ensure consistency, the system may use techniques like read repair or hinted handoff. In read repair, the system checks the versions of the requested data on different nodes and updates them if discrepancies are found. Hinted handoff is used to handle scenarios where a node is temporarily down; the system stores hints about writes that occurred during the downtime, which are used to update the node when it comes back online.

3. **Consistency Levels**: Leaderless replication systems often allow clients to specify consistency levels for both read and write operations. For example, a client might require that a write is confirmed by a majority of nodes before considering it successful or might accept eventual consistency for reads to reduce latency.

4. **Conflict Resolution**: Since writes can occur concurrently on different nodes, the system must handle conflicts. Techniques like version vectors, vector clocks, or CRDTs (Conflict-Free Replicated Data Types) are used to track updates and resolve conflicts in a deterministic manner.

5. **Membership and Failure Detection**: The system must be able to detect node failures and adjust accordingly. This often involves a membership protocol and a failure detection mechanism to keep the list of nodes up-to-date and to re-replicate data to maintain the desired replication factor.

Some well-known distributed databases that use or can be configured to use leaderless replication include Apache Cassandra, Riak, and DynamoDB. These systems are designed to provide high availability and scalability, making them suitable for applications that require continuous operation and can tolerate eventual consistency.