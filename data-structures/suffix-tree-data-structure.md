---
b: https://blendedfeelings.com/software/data-structures/suffix-tree-data-structure.md
---

# Suffix tree 
is a compressed trie (prefix tree) data structure that represents all the suffixes of a given string. It is particularly useful in various string-processing problems, such as substring searches, finding the longest repeated substring, the longest common substring, and the longest palindrome in a string.

Here's how a suffix tree is structured and how it works:

1. **Nodes and Edges**: Each edge of the suffix tree is labeled with a non-empty substring of the text. Each node represents a state, and each edge represents a transition between states. The root node represents the empty string.

2. **Path Label**: The concatenation of edge-labels along the path from the root to a node gives a substring of the text, which is called the path label of that node.

3. **Leaf Nodes**: Each leaf node corresponds to one of the suffixes of the text. The path label of a leaf node is a suffix of the text.

4. **Internal Nodes**: Internal nodes are any nodes except the root and leaves. An internal node with more than one child represents a branching in the tree where the path label is shared by multiple suffixes.

5. **Suffix Links**: A suffix link is a pointer from one internal node to another. If there is an internal node \( u \) with path label \( x\alpha \) (where \( x \) is a single character and \( \alpha \) is a substring), it may have a suffix link to an internal node \( v \), whose path label is \( \alpha \).

6. **Construction**: The suffix tree for a string \( S \) of length \( n \) can be constructed in \( O(n) \) time using various algorithms like Ukkonen's algorithm, which builds the tree incrementally.

7. **Termination**: To ensure that no suffix is a prefix of another, a unique termination symbol (often denoted as \$) is appended to the end of the string, which is not found anywhere else in the string.

For example, consider the string \( S = "banana" \). The suffixes of \( S \) are:

- "banana"
- "anana"
- "nana"
- "ana"
- "na"
- "a"

The suffix tree for \( S \) will have edges labeled with substrings of \( S \), and each leaf will represent one of these suffixes.

Suffix trees are powerful data structures but can be memory-intensive. They are often replaced with more space-efficient data structures like suffix arrays, especially when dealing with large texts.