---
b: https://blendedfeelings.com/software/concurrency/lock-free-queue-data-structure.md
---

# Lock-free queue 
is a concurrent data structure that allows multiple threads to enqueue (add) and dequeue (remove) elements without the need for mutual exclusion locks. This is achieved through the use of atomic operations that ensure the consistency of the queue's state even when multiple threads are accessing it simultaneously.

Lock-free data structures are designed to avoid the drawbacks of locking, such as deadlocks, priority inversion, and convoying, while also providing better scalability and potentially reducing the overhead associated with context switching.

Here is a conceptual overview of how a lock-free queue might be implemented:

1. **Atomic Operations**: The implementation relies on atomic operations provided by the hardware, such as Compare-And-Swap (CAS), Load-Linked/Store-Conditional (LL/SC), or other atomic read-modify-write operations.

2. **Node-Based Design**: The queue is typically implemented as a linked list of nodes, where each node contains the value and a pointer to the next node.

3. **Head and Tail Pointers**: Two pointers, `head` and `tail`, are maintained to point to the first and last nodes in the queue, respectively.

4. **Enqueue Operation**: To add an element to the queue, a new node is created, and the `tail` pointer is atomically swapped with the new node's address if the `tail` still points to the last node. This may involve a loop to retry the operation if other threads are also enqueuing simultaneously.

5. **Dequeue Operation**: To remove an element from the queue, the `head` pointer is advanced to the next node atomically. If the queue is empty or another thread is also dequeuing, the operation may need to retry.

6. **Memory Reclamation**: Since nodes can be removed from the queue by concurrent dequeue operations, a mechanism for safe memory reclamation is necessary, such as hazard pointers, reference counting, or epoch-based reclamation.

Here is a simplified pseudo-code example of a lock-free queue:

```pseudo
class Node {
    value: data
    next: atomic<Node>
}

class LockFreeQueue {
    head: atomic<Node>
    tail: atomic<Node>

    void enqueue(data) {
        newNode = new Node(data)
        while (true) {
            last = tail.load()
            next = last.next.load()
            if (last == tail.load()) { // Check if tail was not changed
                if (next == null) { // Check if last.next is null
                    if (last.next.compare_and_swap(next, newNode)) {
                        tail.compare_and_swap(last, newNode) // Swing tail to newNode
                        break
                    }
                } else {
                    tail.compare_and_swap(last, next) // Tail was not pointing to the last node
                }
            }
        }
    }

    data dequeue() {
        while (true) {
            first = head.load()
            last = tail.load()
            next = first.next.load()
            if (first == head.load()) { // Check if head was not changed
                if (first == last) { // Queue might be empty
                    if (next == null) {
                        return null // Queue is empty
                    }
                    tail.compare_and_swap(last, next) // Tail is falling behind
                } else {
                    data = next.value
                    if (head.compare_and_swap(first, next)) {
                        return data // Dequeue is done
                    }
                }
            }
        }
    }
}
```

This pseudo-code is intended to illustrate the concept and may not be directly usable in a real-world scenario. Actual implementations would need to handle edge cases and memory reclamation more carefully. Additionally, programming languages or libraries that support concurrency may provide their own lock-free queue implementations, which should be used when available to ensure correctness and performance.