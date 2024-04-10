---
b: https://blendedfeelings.com/software/design/single-leader-replication.md
---

# Single leader replication 
also known as master-slave replication, is a common method for distributing a database across multiple machines. This replication model involves designating one node as the "leader" (or "master"), which is responsible for handling all write operations. The other nodes in the system are known as "followers" (or "slaves"), and they replicate the data from the leader to ensure consistency and redundancy.

Here's an overview of how single leader replication works:

1. **Write Operations**: All write operations (INSERT, UPDATE, DELETE) are sent to the leader. The leader writes the new data to its local storage.

2. **Log Generation**: After every write operation, the leader logs the changes in a replication log (also called a transaction log or binary log).

3. **Data Replication**: Followers continuously read the replication log from the leader and apply the changes to their local copies of the data. This can be done synchronously or asynchronously.

    - **Synchronous Replication**: The leader waits for at least one follower to confirm that it has received and applied the change before considering the write operation complete. This ensures strong consistency but can impact write performance.
    
    - **Asynchronous Replication**: The leader does not wait for followers to confirm receipt of changes. This allows for higher write throughput but can lead to temporary inconsistencies if the leader fails before followers have replicated the latest changes.

4. **Read Operations**: Read operations can be distributed across the leader and followers to balance the load and improve read performance. However, if asynchronous replication is used, reads from followers might return slightly stale data.

5. **Failover**: In case the leader fails, one of the followers is promoted to be the new leader. This process can be manual or automated, depending on the system's configuration.

6. **Recovery**: The failed leader, once recovered, typically rejoins the system as a follower and resynchronizes its data from the new leader.

Single leader replication has several advantages, including:

- **Simplicity**: The model is straightforward to understand and implement.
- **Strong Consistency**: If synchronous replication is used, the system can ensure that all followers are up-to-date with the leader.
- **Performance**: Write operations are only handled by one node, which can simplify conflict resolution and transaction management.

However, it also has some disadvantages:

- **Write Scalability**: Since all writes go through the leader, the write throughput is limited by the leader's capacity.
- **Failover Complexity**: Automated failover can be complex to implement correctly, and manual failover can lead to downtime.
- **Data Loss Risk**: With asynchronous replication, there is a risk of data loss if the leader fails before followers have replicated the latest changes.

Single leader replication is widely used in many relational database systems such as PostgreSQL, MySQL, and Oracle. It's also a common pattern in distributed systems architecture.