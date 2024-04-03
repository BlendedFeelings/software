---
b: https://blendedfeelings.com/software/concurrency/lock-free-stack-data-structure.md
---

# Lock-free stack 
is a concurrent data structure that allows multiple threads to operate on it without the need for traditional locking mechanisms like mutexes or semaphores. Lock-free data structures are designed to avoid the pitfalls of locking, such as deadlocks, priority inversion, and convoying, by using atomic operations to ensure consistency.

The basic operations of a lock-free stack are `push` (to insert an element) and `pop` (to remove and return an element). These operations are usually implemented using atomic Compare-And-Swap (CAS) operations, which can atomically compare the value at a memory location with a given value and, only if they are the same, modify the memory location to a new given value.

Here's a simplified example of how a lock-free stack might be implemented in pseudocode:

```pseudocode
class Node
    value: data_type
    next: pointer to Node

class LockFreeStack
    top: pointer to Node (atomic)

    function push(value)
        new_node = new Node(value)
        loop
            new_node.next = top
            if CAS(&top, new_node.next, new_node)
                break

    function pop()
        loop
            old_top = top
            if old_top is null
                return null
            new_top = old_top.next
            if CAS(&top, old_top, new_top)
                return old_top.value
```

In the `push` method:
1. A new node is created with the value to be pushed.
2. The `next` pointer of the new node is set to the current `top` of the stack.
3. An atomic CAS operation is used to set the `top` to the new node only if the `top` hasn't changed since the new node's `next` was assigned. If the CAS fails (meaning another thread has modified `top`), the loop retries.

In the `pop` method:
1. The method enters a loop where it reads the current `top`.
2. If the `top` is null, the stack is empty, and the method returns null.
3. Otherwise, it reads the `next` node to be the new `top`.
4. An atomic CAS operation is used to set the `top` to `new_top` only if the `top` hasn't changed since it was read into `old_top`. If the CAS is successful, the value is returned; otherwise, the loop retries.

This is a highly simplified version of a lock-free stack. In practice, implementing a truly lock-free and thread-safe stack is much more complex, especially when considering issues such as the ABA problem, where a location is changed from A to B and back to A between the time a thread reads it and tries to update it, making the CAS operation incorrectly succeed.

To handle such issues, more sophisticated techniques are often used, such as tagged pointers or double-wide CAS operations that can check for changes in a version number or tag alongside the pointer value. Additionally, memory reclamation in lock-free structures (like when nodes are popped off the stack) is non-trivial because other threads might still be accessing the nodes. Techniques like hazard pointers, epoch-based reclamation, or the use of garbage collectors can help manage this problem.