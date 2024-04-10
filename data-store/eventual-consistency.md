---
b: https://blendedfeelings.com/software/data-store/eventual-consistency.md
---

# Eventual consistency 
is a consistency model used in distributed computing to provide a guarantee that, given enough time without new updates, all replicas of a data item will converge to the same value. This model is often employed in systems where high availability and scalability are prioritized over immediate data consistency.

Here are some key points about eventual consistency:

1. **Weak Guarantee**: Eventual consistency offers a weak guarantee that, eventually, all accesses to a particular piece of data will return the last updated value. However, it does not specify when the convergence will happen.

2. **High Availability**: This model is particularly useful in systems where availability is critical, even in the presence of network partitions or other failures. It allows the system to continue operating despite inconsistencies among replicas.

3. **Trade-offs**: Eventual consistency is often chosen as a trade-off between consistency and other system properties, such as availability and partition tolerance, as outlined in the CAP theorem.

4. **Consistency Mechanisms**: Various mechanisms can be used to achieve eventual consistency, including conflict resolution strategies like "last writer wins", version vectors, and state reconciliation processes.

5. **Use Cases**: Eventual consistency is suitable for applications where it is acceptable for different users to see different versions of data for some time. Examples include social media feeds, DNS systems, and some e-commerce platforms.

6. **Tunable Consistency**: Some systems allow for tunable or adjustable consistency models, where developers can choose the level of consistency for different operations, ranging from strong consistency to eventual consistency, depending on the requirements.

7. **Eventual vs. Strong Consistency**: Unlike strong consistency models (e.g., linearizability or serializability), eventual consistency does not guarantee that operations will be seen in the same order by all processes. Instead, it ensures that all replicas will eventually be consistent if no new updates are made to the data.

Eventual consistency is an important concept in the design of distributed systems, as it allows for greater scalability and availability at the cost of not always providing the most up-to-date data. It is often used in combination with other consistency models to provide the right balance for a given application's needs.