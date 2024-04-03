---
b: https://blendedfeelings.com/software/design/linearizability.md
---

# Linearizability 
is a consistency model for distributed systems. It is a strong form of consistency which guarantees that as soon as an operation completes, all subsequent operations will see the effect of that operation. In other words, operations appear to occur instantaneously and atomically at some point between their invocation and their response.

Here are some key points about linearizability:

1. **Sequential Consistency**: Linearizability is a stronger form of sequential consistency. While sequential consistency only requires that operations appear to occur in some sequential order, linearizability also requires that this order respects the real-time ordering of operations.

2. **Non-blocking**: Linearizability allows for concurrent operations and doesn't require locking the entire system to achieve consistency. Operations can be processed in parallel as long as they appear to take effect instantaneously.

3. **Single Copy Equivalence**: Linearizability provides the illusion that all operations are performed on a single copy of the data, even though the data may be replicated across multiple nodes in the system.

4. **Real-time Ordering**: If an operation `A` completes before operation `B` starts, then `A` must appear to occur before `B` in the system's global order.

5. **Client Perspective**: From the perspective of clients, the results of any operation are immediately visible to all other operations. This is akin to having a single, atomic read-modify-write operation.

6. **Failure Handling**: Linearizability must be maintained even in the presence of node failures. This often requires complex algorithms to ensure that once an operation is acknowledged, it is guaranteed to have taken effect.

7. **Implementation Complexity**: Achieving linearizability can be complex and may require sophisticated coordination protocols, such as consensus algorithms (e.g., Paxos, Raft).

8. **Performance Impact**: Ensuring linearizability can have a performance impact due to the coordination overhead. Systems may need to trade off between strong consistency and high availability or low latency.

9. **Testing for Linearizability**: Testing whether a system is linearizable can be challenging. It involves checking all possible interleavings of operations to ensure they can be rearranged into a sequence that respects real-time order and appears atomic.

10. **Use Cases**: Linearizability is often desired in systems where correctness and consistency are critical, such as financial systems, databases, and other transactional systems.

It's worth noting that not all distributed systems require linearizability. Some systems may opt for weaker consistency models (like eventual consistency) to achieve higher availability or lower latency. The choice of consistency model depends on the specific requirements and trade-offs of the application and system architecture.