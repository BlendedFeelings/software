---
b: https://blendedfeelings.com/software/concurrent-programming/read-copy-update-rcu.md
---

# Read-Copy-Update (RCU) 
is a synchronization mechanism that is used in computer programming, particularly in operating systems kernels, to manage access to shared data structures. It is designed to be efficient for read-heavy workloads where data is read more frequently than it is updated.

RCU allows multiple threads to read from a shared data structure without locking, which can greatly improve performance in read-intensive scenarios. When a thread wants to update the shared data, it does not immediately modify the data in place. Instead, it follows these general steps:

1. **Read**: The thread reads the data structure.
   
2. **Copy**: The thread creates a copy of the data structure.

3. **Update**: The thread applies the changes to the copy.

4. **Publish**: The updated copy is published so that subsequent readers will see the new version.

5. **Synchronize**: Synchronization is performed to ensure that all pre-existing readers have finished their read operations on the old data structure.

6. **Reclaim**: Once it is safe (all pre-existing readers have completed their read operations), the old data structure is reclaimed or freed.

The key advantage of RCU is that readers can access data without being blocked by writers, which can lead to high levels of concurrency and performance. However, it also requires careful design to ensure that the system correctly identifies when it is safe to reclaim old versions of data structures.

RCU is particularly useful in kernel development and has been used extensively in the Linux kernel. It is less commonly used in user-space programming due to its complexity and the availability of other synchronization mechanisms that are easier to use correctly.