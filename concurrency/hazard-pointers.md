---
b: https://blendedfeelings.com/software/concurrency/hazard-pointers.md
---

# Hazard pointers 
are a technique used in concurrent programming to ensure safe memory reclamation. They are particularly useful in lock-free data structures where multiple threads may access shared data concurrently. The main goal of hazard pointers is to prevent a thread from deallocating a node that another thread is about to access.

Here's how hazard pointers generally work:

1. **Hazard Pointer Registration**: When a thread wants to access a shared node, it first claims a hazard pointer by writing the address of the node to its own hazard pointer record. This is a way of saying, "I am about to access this node, so please don't delete it."

2. **Access the Node**: After claiming the hazard pointer, the thread can safely access the node. Other threads that might want to delete nodes will see the hazard pointer and know that they cannot deallocate this particular node.

3. **Check for Hazard Pointers**: Before a thread deallocates a node, it must check the hazard pointers of all other threads. If any hazard pointer points to the node that is about to be deallocated, the deallocation must be deferred because another thread is still using it.

4. **Clear Hazard Pointer**: Once the thread is done accessing the node, it clears its hazard pointer record to indicate that the node can now be safely deallocated by others.

5. **Memory Reclamation**: Deallocating a node can be done once it's verified that no hazard pointers are pointing to it. However, because other threads might have deferred deallocation, a reclamation scheme is usually needed to periodically check and free nodes that are no longer in use.

The hazard pointers technique is a way to solve the ABA problem in lock-free data structures. The ABA problem occurs when a thread reads a value A from shared memory, gets preempted, and by the time it is scheduled again, another thread has changed the value to B and then back to A. The first thread sees the value A again and proceeds, not realizing that the state of the shared memory has changed in the meantime.

Hazard pointers mitigate this issue by ensuring that even if the node has been removed and potentially reallocated (the ABA scenario), a thread with a hazard pointer to the old node will not access the new node that happens to occupy the same memory address.

Implementing hazard pointers can be complex and requires careful consideration of memory ordering and synchronization between threads. It's important to ensure that all operations on hazard pointers are performed with the appropriate memory barriers to prevent reordering by the compiler or the CPU.