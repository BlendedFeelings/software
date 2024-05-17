---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/grow-only-counter.md
---

# G-Counter, or Grow-only Counter 
is a type of Conflict-Free Replicated Data Type (CRDT) which is designed to work in a distributed system where multiple nodes need to maintain and merge a shared state without central coordination.

The G-Counter is a simple CRDT that supports two operations:

- **Increment**: Each node can increase the count, but never decrease it.
- **Merge**: Nodes can combine their counts to reconcile the state and ensure consistency across the distributed system.

Each node in the system maintains its own local counter. The overall count is the sum of all local counters. When a node increments its counter, it only updates its local state. To get the global count, a node must merge its state with the states of all other nodes.

Here's a conceptual overview of how a G-Counter might work:

- Each node has an identifier (ID), and the counter is represented as a map or array where each entry corresponds to a node's ID.
- When a node wants to increment the counter, it increments its own entry in the map/array based on its ID.
- To merge counters, each node takes the maximum of the corresponding entries from all the counters it is merging. This is safe because the counts can only grow.

Here is a simple example of how a G-Counter might be implemented in pseudocode:

```pseudocode
// Initialize a G-Counter
function initialize():
    counter = map[nodeID -> 0]
    return counter

// Increment the counter for a specific node
function increment(counter, nodeID):
    counter[nodeID] += 1

// Merge two counters
function merge(counter1, counter2):
    mergedCounter = map[nodeID -> 0]
    for each nodeID in counter1 and counter2:
        mergedCounter[nodeID] = max(counter1[nodeID], counter2[nodeID])
    return mergedCounter

// Get the total count from a counter
function total(counter):
    sum = 0
    for each count in counter.values():
        sum += count
    return sum
```

In practice, G-Counters are often used in systems where it's necessary to count events or collect metrics without relying on a single point of failure or centralised coordination. They are particularly useful in situations where network partitions can occur, and the system still needs to operate correctly and eventually converge to a consistent state.