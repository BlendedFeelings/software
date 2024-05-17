---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/convergent-replicated-data-types.md
---

# State-based CRDTs (Convergent Replicated Data Types, or CvRDTs) 
are a category of CRDTs designed for distributed systems where replicas of the data type must be kept consistent despite concurrent updates and potential network partitions. The core idea behind CvRDTs is that each replica maintains its own state, and these states can be merged using a specific merge operation to ensure that all replicas converge to the same state over time.

Here are some key characteristics and principles of CvRDTs:

- **Commutative Merge Function:** CvRDTs define a merge function that is commutative, associative, and idempotent. This means that the order in which merges are performed does not matter (commutative), merges can be grouped together in any way (associative), and merging a state with itself does not change the state (idempotent).

- **Monotonic State Changes:** The state in a CvRDT must change in a way that is monotonic, meaning that it can only move forward and never regress. This is important because it ensures that once an update is applied, it cannot be undone by the merge operation.

- **State Transmission:** To synchronize, replicas exchange their entire state or a delta of their state with each other. When a replica receives a state from another, it merges this state with its own using the merge function.

- **Idempotence:** Due to the idempotent nature of the merge function, if a replica receives the same state multiple times, the result of merging that state will be the same as if it was merged only once.

- **Eventual Consistency:** CvRDTs guarantee eventual consistency, meaning that if all updates stop and all replicas communicate with each other, all replicas will eventually reach the same state.

Examples of CvRDTs include:

- **G-Counter (Grow-only Counter):** A counter that can only be incremented. Each replica maintains a count for each node in the system, and the merge operation involves taking the maximum count for each node from all replicas.

- **PN-Counter (Positive-Negative Counter):** An extension of the G-Counter that supports both increments and decrements. It maintains two G-Counters internally, one for increments and one for decrements. The total count is the difference between the two G-Counters.

- **OR-Set (Observed-Removed Set):** A set that supports adding and removing elements. Elements are tagged with unique identifiers, and the merge operation involves unioning the added elements and removing the elements that have been observed as removed.

CvRDTs are particularly useful in systems where the communication between replicas can be intermittent or unreliable, and where operations need to be performed without waiting for a global consensus. They provide a robust way to handle the complexities of distributed data synchronization while ensuring that the system can continue to function and that data remains consistent across replicas in the long term.