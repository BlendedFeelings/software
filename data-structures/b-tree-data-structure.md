---
b: https://blendedfeelings.com/software/data-structures/b-tree-data-structure.md
---

# B-Tree 
is a self-balancing tree data structure that maintains sorted data in a way that allows for efficient insertion, deletion, and lookup operations. It's particularly well-suited for storage systems that read and write large blocks of data, like databases and file systems.

Here are some key characteristics of a B-Tree:

1. **Balanced Tree**: All leaf nodes are at the same level, which ensures that the time complexity for search operations is always logarithmic.

2. **Multi-way Tree**: Unlike binary trees which have at most two children (left and right), B-Trees can have multiple children per node. The number of children is determined by the order of the tree.

3. **Order of the Tree**: The order (or branching factor) of a B-Tree is denoted by 't'. A B-Tree of order 't' can have at most '2t - 1' keys and '2t' children per node.

4. **Keys and Children**: Each node can contain a minimum of 't - 1' keys and a maximum of '2t - 1' keys. Accordingly, it can have a minimum of 't' children and a maximum of '2t' children.

5. **Sorted Nodes**: The keys within a node are always sorted, and the subtree between two keys 'k1' and 'k2' contains all the keys that are between the values 'k1' and 'k2'.

6. **All Keys are Stored in the Leaves**: In some variations of B-Trees, all the keys are stored in the leaf nodes, and the internal nodes only contain copies of the keys to guide the search.

7. **Efficient Operations**: B-Trees are designed to minimize disk reads and writes. This is achieved by maximizing the number of keys within each node, which reduces the height of the tree and thus the number of disk accesses required for most operations.

8. **Insertion**: When inserting a new key, it's placed in the appropriate position to maintain the sorted order. If the node overflows (i.e., has more than '2t - 1' keys), it's split into two nodes, and the middle key is moved up to the parent. This process may propagate up to the root, which may also split, thus increasing the height of the tree.

9. **Deletion**: When deleting a key, if the key is in a leaf node and the node has more than the minimum number of keys, it's simply removed. If the key is in an internal node or the leaf has the minimum number of keys, the tree is adjusted to maintain its properties, which can involve borrowing a key from a sibling node or merging nodes.

10. **Searching**: To find a key, you start at the root and traverse the tree by making comparisons at each node and moving to the appropriate child until you reach a leaf node where the key should be if it exists in the tree.

B-Trees are widely used in databases and file systems due to their ability to handle large amounts of data while maintaining fast search, insert, and delete operations. They are particularly effective when the data is stored on disk, as their structure minimizes the number of disk reads and writes required for operations.