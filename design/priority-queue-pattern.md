---
b: https://blendedfeelings.com/software/design/priority-queue-pattern.md
---

# Priority queue 
is an abstract data type similar to a regular queue or stack data structure in which each element additionally has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority. If two elements have the same priority, they are served according to their order in the queue.

Here's a basic overview of the priority queue pattern:

1. **Elements**: Each element in a priority queue must have some form of data and a priority level. The priority level is usually a numeric value, with either a higher or lower value indicating higher priority, depending on the implementation.

2. **Insertion**: When a new element is added to the priority queue, it is inserted into the queue based on its priority. This means that the queue must reorder its elements to accommodate the new entry according to the priority rules.

3. **Retrieval**: When an element is retrieved from the queue (often called a 'pop' operation), the element with the highest priority is removed from the queue and returned. If multiple elements have the same priority, the queue may decide which one to return based on other criteria, such as insertion order.

4. **Implementation**: Internally, priority queues can be implemented using various data structures, such as binary heaps, binary search trees, or even unordered arrays or linked lists (though the latter two have less efficient operations).

5. **Complexity**: The efficiency of a priority queue depends on its implementation. Binary heaps, for example, can insert and retrieve elements in O(log n) time, where n is the number of elements in the queue.

6. **Usage**: Priority queues are used in many areas of computer science, including scheduling processes in operating systems, implementing Dijkstra's algorithm for shortest path finding, and in handling events in discrete event simulation.

Here's a simple example of a priority queue using a binary heap in Python:

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Usage:
pq = PriorityQueue()
pq.push('task1', priority=3)
pq.push('task2', priority=1)
pq.push('task3', priority=2)

print(pq.pop()) # Outputs 'task1' (highest priority)
print(pq.pop()) # Outputs 'task3'
print(pq.pop()) # Outputs 'task2' (lowest priority)
```