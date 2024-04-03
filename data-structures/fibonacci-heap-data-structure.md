---
b: https://blendedfeelings.com/software/data-structures/fibonacci-heap-data-structure.md
---

# Fibonacci Heap 
is a data structure for priority queue operations, including a mergeable heap. It consists of a collection of heap-ordered trees and is particularly well-suited for algorithms that frequently merge heaps together, such as Dijkstra's algorithm for shortest paths or the Prim's algorithm for minimum spanning trees.

Here are some key properties and operations of Fibonacci Heaps:

1. **Structure:** A Fibonacci Heap is a collection of rooted trees that are min-heap ordered. This means that each tree obeys the min-heap property: the key of a child is always greater than or equal to the key of the parent.

2. **Lazy Organization:** The trees within a Fibonacci Heap are not necessarily binary trees, and there is no constraint on the number of children a node may have. The structure is more relaxed compared to a binary heap, which allows operations to be more efficient on average, although they might have a high worst-case complexity.

3. **Minimal Node:** The heap maintains a pointer to the tree containing the minimum key, which allows for constant-time minimum key retrieval.

4. **Operations:**
   - **Insert:** Adding a new element to the heap is done by creating a new tree and adding it to the list of trees. This operation is done in constant amortized time.
   - **Find Minimum:** Since the heap maintains a pointer to the tree with the minimum key, this operation is done in constant time.
   - **Delete Minimum:** This operation removes and returns the element with the minimum key. It does so by removing the tree containing the minimum element, then merging its children with the remaining trees. The trees are then consolidated to adjust the heap. This operation takes \(O(\log n)\) amortized time.
   - **Union:** Two Fibonacci Heaps can be united by concatenating their tree lists. This operation takes constant amortized time.
   - **Decrease Key:** This operation decreases the key of a specified element. If this breaks the min-heap property, the tree is cut and the subtree formed by the node is merged with the other trees. This operation takes constant amortized time.
   - **Delete:** To delete a node, its key is decreased to less than the minimum key and then the minimum node is deleted. This operation takes \(O(\log n)\) amortized time.

5. **Amortized Analysis:** Fibonacci Heaps have good amortized running times. For example, insertions and decrease-key operations can be done in \(O(1)\) amortized time, and delete-minimum and delete operations can be done in \(O(\log n)\) amortized time.

6. **Lazy Consolidation:** The consolidation of trees is deferred until it's absolutely necessary (such as during delete-minimum operations), which is why the data structure is called "Fibonacci." The trees are consolidated in such a way that there is at most one tree of each degree in the final list of trees.

Fibonacci Heaps are more complex to implement than binary heaps or binomial heaps, but they can be more efficient for algorithms that require many merge operations. However, due to their complexity, they are not often used in practice, and simpler data structures like binary heaps are preferred for most applications.