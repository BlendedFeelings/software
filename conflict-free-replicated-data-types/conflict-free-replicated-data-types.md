---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/conflict-free-replicated-data-types.md
---

# Conflict-free replicated data types (CRDTs) 
are data structures that can be replicated across multiple computers in a network, where each replica can be updated independently and concurrently without coordination between the replicas, and where it is always mathematically possible to resolve inconsistencies that might result.

CRDTs are designed to be used in distributed systems to achieve strong eventual consistency and are particularly useful in environments where low latency is required and where it is not always possible to achieve immediate consistency due to network partitions or other communication issues.

There are two main types of CRDTs:

1. **State-based CRDTs (CvRDTs):**
   - Each replica of a CvRDT maintains its own state, which is merged with the states of other replicas to achieve consistency.
   - The merge operation is commutative, associative, and idempotent, ensuring that replicas can be merged in any order, and that re-merging states does not change the result.
   - State-based CRDTs require transmitting the entire state or a delta state when updates occur, which may be inefficient if the state is large.

2. **Operation-based CRDTs (CmRDTs):**
   - With CmRDTs, instead of sharing states, replicas propagate operations to each other.
   - Operations need to be designed so that they commute, meaning that applying them in any order will result in the same state.
   - CmRDTs generally require a reliable broadcast mechanism to ensure that all operations are eventually received and applied by all replicas.

CRDTs support various data types such as counters, sets, maps, and lists, each with specific rules for resolving conflicts. For example, a CRDT counter would converge towards the correct total count as replicas communicate and merge their states, even if increments and decrements are made concurrently on different replicas.

CRDTs are useful in scenarios such as collaborative applications (like Google Docs), distributed databases, and caching systems, where the system must continue to function correctly even when some replicas are temporarily unable to communicate.