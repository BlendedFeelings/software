---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/positive-negative-counter.md
---

# PN-Counter, or Positive-Negative Counter, 
is a type of data structure used in distributed systems to achieve a form of conflict-free replicated data type (CRDT). CRDTs are designed to be replicated across multiple nodes in a network, allowing for concurrent updates that can be merged in a way that ensures eventual consistency without the need for locking or other synchronization primitives.

The PN-Counter is specifically used for implementing a distributed counter that can be incremented and decremented. Here's how it works:

- The PN-Counter consists of two separate counters: one for tracking the increments (the positive counter) and one for tracking the decrements (the negative counter).
- Each node in the distributed system maintains its own copy of the PN-Counter. When a node wants to increment the counter, it increments its own positive counter. Similarly, when a node wants to decrement the counter, it increments its own negative counter.
- When nodes communicate with each other, they share their positive and negative counter values. Upon receiving the values from another node, a node will merge the values by taking the maximum of each counter from all nodes. This is based on the assumption that each node's counters only increase.
- The actual value of the PN-Counter is calculated by subtracting the value of the negative counter from the positive counter.

The PN-Counter allows for a reliable distributed counter that can handle concurrent increments and decrements in a system where nodes might not always be able to communicate with each other. The merging process ensures that all nodes eventually reach the same value, as long as all increments and decrements are eventually propagated to all nodes.

Here is a simplified example of how a PN-Counter might be implemented in pseudocode:

```pseudocode
class PNCounter:
    def __init__(self):
        self.positive = 0
        self.negative = 0

    def increment(self):
        self.positive += 1

    def decrement(self):
        self.negative += 1

    def value(self):
        return self.positive - self.negative

    def merge(self, other_counter):
        self.positive = max(self.positive, other_counter.positive)
        self.negative = max(self.negative, other_counter.negative)
```

In a real-world distributed system, the `merge` method would be more complex to handle the merging of state from multiple nodes, and additional mechanisms would be needed to handle communication and conflict resolution. However, this example gives a basic idea of the PN-Counter's functionality.