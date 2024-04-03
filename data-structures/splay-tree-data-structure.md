---
b: https://blendedfeelings.com/software/data-structures/splay-tree-data-structure.md
---

# Splay Tree 
is a self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again. It performs basic operations such as insertion, look-up, and removal in \(O(\log n)\) amortized time. For many sequences of non-random operations, Splay Trees perform better than other search trees, even when the specific pattern of the sequence is unknown.

The main idea of a Splay Tree is to move the accessed item to the root of the tree through a series of tree rotations, a process called "splaying". This ensures that recently accessed elements are easy to access again, and it also maintains a roughly balanced tree, which is important for keeping the tree operations efficient.

Splaying involves three types of rotations, depending on the position of the node being accessed (let's call it 'x') and its parent ('p') and grandparent ('g'):

1. **Zig**: This is a single rotation and it happens when 'x' is a child of the root. The tree is rotated directly to move 'x' to the root.

2. **Zig-Zig**: This is a double rotation and it happens when 'x' and its parent 'p' are either both left children or both right children of their respective parents. The tree is rotated to move 'x' two levels up.

3. **Zig-Zag**: This is also a double rotation but it happens when 'x' is a right child and 'p' is a left child or vice versa. The tree is rotated to move 'x' two levels up, but in two steps, each in the opposite direction.

Splay Trees have several advantages:
- They are relatively simple to implement.
- They have good amortized performance for a sequence of operations.
- They do not need to store any balance information, so they use less memory than other balanced trees.

However, they also have some disadvantages:
- The worst-case time for a single operation can be \(O(n)\) (though this is rare and is offset by the amortized time).
- The tree is not strictly balanced, so performance can degrade if it is not accessed in a way that takes advantage of its self-adjusting property.

In summary, Splay Trees are a good choice for applications where the access pattern is not random and has temporal locality, which means that recently accessed items are likely to be accessed again in the near future.