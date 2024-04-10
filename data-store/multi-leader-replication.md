---
b: https://blendedfeelings.com/software/data-store/multi-leader-replication.md
---

# Multi-leader replication 
also known as master-master replication, is a method of database replication in which multiple database servers host the same data and can independently accept writes and updates. This is in contrast to single-leader replication, where a single designated master server handles all write operations and then replicates those changes to one or more read-only replica servers.

Here are some key characteristics of multi-leader replication:

1. **Multiple Write Points**: Each leader can accept write operations, which makes the system more resilient to failure. If one leader fails, other leaders can continue to process writes without interruption.

2. **Conflict Resolution**: Since multiple leaders can accept writes, there is a potential for write conflicts when the same data is modified in different leaders at the same time. Multi-leader replication systems must have a conflict resolution mechanism to handle such cases. This could be as simple as "last write wins" or more complex application-specific logic.

3. **Asynchronous Replication**: Leaders typically replicate changes to each other asynchronously. This means that there could be a brief period where the leaders are out of sync. Eventually, all changes propagate to all leaders, ensuring consistency.

4. **Topology**: The replication topology can be configured in various ways, such as a ring where each leader replicates to the next, or a star where each leader replicates to all others.

5. **Performance**: Multi-leader replication can offer improved write performance and lower latency, especially in geographically distributed systems, because write operations can be processed by the nearest leader.

6. **Complexity**: The complexity of managing multiple write points and resolving conflicts can make multi-leader replication more difficult to implement and maintain than single-leader replication.

7. **Use Cases**: Multi-leader replication is particularly useful in scenarios where high availability, low latency, and resilience to network partitions are crucial. It is often used in distributed systems, multi-datacenter deployments, and global applications.

It's important to carefully consider the trade-offs of using multi-leader replication, as the increased complexity and potential for conflicts may not be suitable for all applications. Proper design, conflict resolution strategies, and thorough testing are essential for successful implementation.