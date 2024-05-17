---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/commutative-replicated-data-types.md
---

# Operation-based CRDTs (Commutative Replicated Data Types, or CmRDTs), 
also known as op-based CRDTs, are a type of CRDT designed to handle the replication of data across multiple nodes in a distributed system. In contrast to state-based CRDTs (CvRDTs) that synchronize by sharing their entire state or a part of it, CmRDTs synchronize by propagating operations (or updates) that have been applied to the data.

Here are some key characteristics and principles of CmRDTs:

- **Commutative Operations:** The operations in a CmRDT must be designed so that they commute, meaning that they can be applied in any order and still produce the same final state. This is crucial for consistency, as operations may arrive at different replicas in different orders.

- **Reliable Broadcast:** CmRDTs typically rely on a reliable broadcast mechanism to ensure that all operations are eventually delivered to all replicas. This mechanism should guarantee that operations are delivered without loss, duplication, or creation, and often in causal order (though not necessarily in the order they were issued).

- **Idempotence:** Operations should be idempotent, meaning that applying the same operation multiple times has the same effect as applying it once. This characteristic is important to handle message retransmissions or duplication.

- **Eventual Consistency:** Just like CvRDTs, CmRDTs provide eventual consistency. As long as all operations are eventually delivered to all replicas, and there are no new updates, the replicas will converge to the same state.

Examples of CmRDTs include:

- **Counter:** An operation-based counter where increments and decrements are represented as operations that are propagated to all replicas. Each operation includes a unique identifier to ensure idempotence.

- **Set:** An operation-based set can have add and remove operations. To ensure idempotence and commutativity, each element might be tagged with a unique identifier, and the operations are designed to handle out-of-order delivery.

- **List:** An operation-based list (or sequence) where insert and delete operations include context information to ensure that concurrent operations can be correctly integrated into the list, preserving the intended order of elements.

CmRDTs are particularly useful in scenarios where operation-based updates are more efficient or practical than exchanging the entire state. For example, in a collaborative text editor, it would be more efficient to propagate the operations of inserting or deleting characters rather than the entire text state after each change.

In summary, CmRDTs provide a framework for ensuring data consistency across distributed systems where operations can be applied out of order. They are well-suited for environments with unreliable communication or where operation-based updates are preferred over state-based synchronization.