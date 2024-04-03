---
b: https://blendedfeelings.com/software/data-structures/red-black-tree-data-structure.md
---

# Red-Black Tree 
is a type of self-balancing binary search tree, a data structure used in computer science to maintain a sorted set of elements and to provide efficient search, insertion, and deletion operations. Each node in the Red-Black Tree contains an extra bit for denoting the color of the node, either red or black. The colors are used to ensure the tree remains balanced during insertions and deletions.

Red-Black Trees have the following properties:

1. **Node Color**: Every node is either red or black.
2. **Root Property**: The root of the tree is always black.
3. **Leaf Property**: Every leaf (NIL node) is black. Here, NIL nodes are considered as leaves and are usually represented by `null` or a special node.
4. **Red Node Property**: If a red node has children, then both its children are black (i.e., no two red nodes can be adjacent; a red node cannot have a red parent or red child).
5. **Black Height Property**: Every path from a node to any of its descendant NIL nodes has the same number of black nodes (i.e., the black height is consistent).

These properties ensure that the tree remains approximately balanced, which guarantees that the basic dynamic set operations (`INSERT`, `DELETE`, and `FIND`) can be performed in O(log n) time, where n is the number of nodes in the tree.

Here's a high-level description of how insertions and deletions are handled:

- **Insertions**: When a new node is inserted, it is initially colored red. If this causes a violation of the Red-Black Tree properties (e.g., two red nodes become adjacent), the tree performs a series of rotations and recolorings to restore the properties.

- **Deletions**: When a node is deleted, if it causes a black node to be removed, the tree may become unbalanced. To fix this, the tree performs a series of operations called "fixing up" to redistribute the black height across the tree and restore the properties.

Rotations are a fundamental operation used to maintain balance during insertions and deletions. There are two types of rotations: left rotation and right rotation. These operations change the structure of the tree while preserving the binary search tree property.

Here's a simple representation of a Red-Black Tree:

```
    B
   / \
  R   B
 /   / \
B   R   B
```

In this diagram, `B` represents a black node, and `R` represents a red node. The tree maintains the Red-Black properties: the root is black, red nodes have black children, all paths from the root to the leaves have the same number of black nodes, and all leaves (not shown) are black.

Implementing a Red-Black Tree requires careful attention to the properties during insertions and deletions to ensure that the tree remains balanced. It's a complex data structure but provides excellent performance for many types of applications, particularly those that require frequent, dynamic changes to the dataset.