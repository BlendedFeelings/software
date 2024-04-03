---
b: https://blendedfeelings.com/software/data-structures/heap-data-structure.md
---

# Heap 
is a specialized tree-based data structure that satisfies the heap property. In a heap, for any given node C, if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C. The node at the "top" of the heap (with no parents) is called the root node.

The heap is one possible implementation of a priority queue. There are two kinds of heaps: a max heap and a min heap.

### Max Heap:
- **Max Heap Property**: In a max heap, for any given node C, the key of C is greater than or equal to the keys of its children.
- **Application**: A max heap can be used to implement a priority queue where the element with the greatest key is always at the front (i.e., the root).

### Min Heap:
- **Min Heap Property**: In a min heap, for any given node C, the key of C is less than or equal to the keys of its children.
- **Application**: A min heap can be used to implement a priority queue where the element with the lowest key is always at the front (i.e., the root).

### Common Operations:
- **Insert**: Add a new key to the heap.
- **Extract Max/Min**: Removes and returns the largest/smallest key from a max/min heap, respectively.
- **Peek**: Returns the largest/smallest key from a max/min heap without removing it.
- **Increase Key/Decrease Key**: Increases/decreases the value of a key in a max/min heap, respectively, and then restructures the heap if necessary.
- **Heapify**: Given an array of elements, rearranges the elements to satisfy the heap property.

### Representation:
A heap can be represented as a binary tree, but it is usually implemented using an array. For an array-based representation:
- If the index of any element in the array is `i`, the index of its parent is `floor((i-1)/2)` and the index of its children are `2*i + 1` (left child) and `2*i + 2` (right child).
- The root element will be at `array[0]`.

### Time Complexity:
- **Insert**: O(log n)
- **Extract Max/Min**: O(log n)
- **Peek**: O(1)
- **Increase Key/Decrease Key**: O(log n)
- **Heapify**: O(n)

Heaps are widely used because they are efficient (O(log n) time for insert and extract), and they can efficiently find the max or min element.