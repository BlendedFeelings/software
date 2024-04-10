---
b: https://blendedfeelings.com/software/design/cap-theorem.md
---

# CAP theorem 
also known as Brewer's theorem, is a fundamental principle in the field of distributed computing systems that addresses the trade-offs between three key properties: Consistency, Availability, and Partition Tolerance. It was formulated by Eric Brewer in 2000.

Here's what each of these properties means:

- **Consistency**: Every read operation from the system returns the most recent write or an error. In other words, if a write operation occurs, any subsequent read operation should reflect that change. This is the "C" in CAP.

- **Availability**: Every request (whether read or write) receives a (non-error) response, without the guarantee that it contains the most recent write. This ensures that the system is always operational and does not have any downtime. This is the "A" in CAP.

- **Partition Tolerance**: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes. If communication between nodes is unreliable, the system can still function. This is the "P" in CAP.

The CAP theorem asserts that a distributed system can only provide two of the three guarantees at the same time, but not all three simultaneously. This means that in the presence of a network partition (P), one must choose between consistency (C) and availability (A). For example:

- A system can be consistent and partition-tolerant (CP), but it might not be available in the sense that if a partition occurs, some nodes might not be able to respond to requests.

- A system can be available and partition-tolerant (AP), but it might not be consistent across all nodes at all times. In the event of a partition, the system will continue to operate, but some nodes might return an outdated or stale response.

- It's not possible to have a system that is consistent and available (CA) across a partition, because if there is a partition, you can't maintain both consistency and availability; you must sacrifice one for the other.

The CAP theorem has been widely influential in the design of distributed systems and has led to the development of various databases and systems that prioritize different aspects of the theorem based on the needs of their applications.