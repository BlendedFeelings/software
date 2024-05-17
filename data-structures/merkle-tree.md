---
b: https://blendedfeelings.com/software/data-structures/merkle-tree.md
---

# Merkle tree 
named after Ralph Merkle who patented it in 1979, is a fundamental data structure used in computer science and information security. It is a type of binary tree, consisting of a set of nodes with a large number of leaf nodes at the bottom of the tree that contain the underlying data, a set of intermediate nodes where each node is the hash of its two children, and a single node at the top, known as the root, which represents the hashes of all the underlying data.

Here are some key points about Merkle trees:

- **Hash Function**: A Merkle tree uses a cryptographic hash function to secure the integrity of the data. Common hash functions used include SHA-256 and SHA-3.

- **Data Integrity and Verification**: The primary use of a Merkle tree is to verify the contents of the data blocks in distributed systems, especially in peer-to-peer networks like blockchains. Because each non-leaf node is a hash of its children, you can verify the integrity of any data chunk without needing the entire dataset.

- **Efficiency**: Merkle trees are efficient both in terms of space and in terms of the ability to verify the data. If you have the top hash, you can receive a small set of hashes from a trusted source and verify that a piece of data is part of the set by computing a small number of hashes.

- **Blockchain and Distributed Ledger Technologies**: In blockchain, each block contains a Merkle tree root of all the transactions included in the block. This allows for a quick and secure way to verify whether a particular transaction is included in the block without having to download all transactions.

- **Merkle Proof**: A Merkle proof consists of a leaf, a root, and a proof, which is a list of the hashes that are needed to go from the leaf to the root. This allows a verifier to prove that a transaction is included in a block without having to hold the entire blockchain.

Here is a simplified example of how a Merkle tree might look:

```
         Root
         /  \
        /    \
   Hash AB    Hash CD
    / \        / \
Hash A Hash B Hash C Hash D
```

In this tree, `Hash A` is the hash of some data block A, `Hash B` is the hash of some data block B, and so on. `Hash AB` is the hash of the concatenation of `Hash A` and `Hash B`, and the root is the hash of the concatenation of `Hash AB` and `Hash CD`. If you want to prove that block A is part of this tree, you would provide `Hash A`, `Hash B`, and `Hash CD` along with the root. The verifier can then hash `Hash A` and `Hash B` to get `Hash AB`, and then hash `Hash AB` with `Hash CD` to see if it matches the root.

Merkle trees are a crucial component in ensuring the integrity and efficiency of data verification processes in various types of networks and systems.