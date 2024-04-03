---
b: https://blendedfeelings.com/software/concurrency/elimination.md
---

# Elimination 
is a concurrency optimization technique used in the design of lock-free and concurrent data structures, particularly when dealing with high contention scenarios. The core idea behind elimination is that certain pairs of operations can cancel each other out, effectively negating the need to modify the shared state and thus reducing contention.

### How Elimination Works

Consider a concurrent stack as an example. A stack has two primary operations: `push`, which adds an element to the top of the stack, and `pop`, which removes the topmost element. Under high contention, multiple threads attempting to push or pop can lead to performance degradation due to contention for the top of the stack. Elimination can optimize this by pairing `push` and `pop` operations that occur concurrently.

Here's a simplified explanation of how elimination might work in a concurrent stack:

1. **Elimination Array:** There is a shared elimination array where threads can announce their intent to perform a `push` or `pop` operation.
   
2. **Announce Operation:** When a thread wants to perform a `pop`, it checks the elimination array for a corresponding `push` operation with a value to be added to the stack.

3. **Pairing:** If it finds a matching `push`, the `pop` operation takes the value directly from the `push` operation, and both operations complete without actually modifying the stack.

4. **Fallback:** If no matching operation is found within a certain time frame, the thread falls back to performing the operation on the stack itself, using atomic operations.

5. **Retries:** If the fallback also experiences contention, the thread may retry the elimination strategy several times before falling back to the normal operation.

### Benefits of Elimination

- **Reduced Contention:** By pairing operations that negate each other, elimination reduces contention on the central data structure.
- **Improved Throughput:** The system can handle a higher rate of operations because some operations are resolved without accessing the shared resource.
- **Scalability:** Elimination can help improve scalability on multi-core processors by reducing the synchronization overhead.

### Challenges and Considerations

- **Complexity:** Implementing elimination adds complexity to the data structure, as it requires additional mechanisms to coordinate between threads and to handle cases where operations cannot be eliminated.
- **Limited Applicability:** Elimination is not universally applicable. It works best for operations that have a natural inverse, such as `push` and `pop` in a stack or `enqueue` and `dequeue` in a queue.
- **Contention Levels:** Elimination is most beneficial under high contention. At low contention levels, the overhead of managing the elimination mechanism might not be justified.
- **Timeouts and Backoff:** To prevent threads from waiting indefinitely, elimination often includes timeouts or backoff strategies to ensure progress.

Designing and implementing elimination requires careful consideration of the concurrency properties of the data structure and the expected access patterns. It's crucial to ensure that the optimization does not introduce new concurrency bugs or violate the data structure's invariants. Additionally, thorough testing is needed to validate correctness and performance under various contention scenarios.