---
b: https://blendedfeelings.com/software/design/eventual-consistency.md
---

# Eventual consistency 
is a consistency model used in distributed systems, which allows for temporary inconsistencies between different copies (replicas) of distributed data. The core idea is that, given enough time and assuming no new updates are made to the data, all replicas will eventually become consistent with each other.

Here are some key points about eventual consistency:

1. **Latency Tolerance**: Eventual consistency is often used in systems where low latency is more critical than strong consistency. It allows for quicker response times because operations can proceed without waiting for all replicas to be updated synchronously.

2. **Eventual Convergence**: All replicas will converge to the same state in the absence of new updates, typically through background processes that propagate updates across the system.

3. **Conflict Resolution**: In cases where concurrent updates are made to different replicas, the system must have a mechanism to resolve conflicts. This can be done using versioning, timestamps, or other conflict resolution strategies such as "last writer wins" or application-specific rules.

4. **Trade-offs**: Eventual consistency is often chosen as a trade-off between consistency, availability, and partition tolerance (the CAP theorem). It favours availability and partition tolerance over immediate consistency.

5. **Use Cases**: Systems that are suitable for eventual consistency are those where it's acceptable for different users to see slightly different data for some time. Examples include social media feeds, distributed file systems, and DNS.

6. **Consistency Levels**: There are various levels of eventual consistency, such as causal consistency, read-your-writes consistency, session consistency, and monotonic read consistency, each providing different guarantees.

7. **Monitoring and Metrics**: To manage eventual consistency, it's important to have monitoring in place to track the extent of inconsistencies and the time it takes for the system to converge.

8. **User Experience**: In some cases, the user interface can be designed to mask inconsistencies or inform users that updates are in the process of propagating.

9. **Eventual Consistency vs. Strong Consistency**: Unlike strong consistency, where all replicas are guaranteed to be up-to-date after a transaction, eventual consistency allows for a period during which replicas can diverge.

10. **Design Considerations**: When designing a system with eventual consistency, it's important to consider how inconsistencies will affect the application's behaviour and how to maintain integrity and user trust.

In summary, eventual consistency is a pragmatic approach to data replication in distributed systems that prioritises availability and performance, while accepting that data may not be perfectly synchronised at all times. It requires careful design to ensure that the eventual convergence of data meets the application's requirements and user expectations.