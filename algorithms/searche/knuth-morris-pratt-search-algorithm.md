---
b: https://blendedfeelings.com/software/algorithms/searche/knuth-morris-pratt-search-algorithm.md
---

# KMP (Knuth-Morris-Pratt)
is a string searching algorithm that searches for occurrences of a pattern within a larger text by comparing characters of the pattern to the text being searched, without wasting time comparing previously matched characters.

The algorithm preprocesses the pattern to determine the longest possible proper prefix of the pattern that is also a suffix of each possible substring of the pattern. This information is then used to avoid matching characters that have already been matched.

The KMP algorithm has a time complexity of O(m+n), where m is the length of the pattern and n is the length of the text being searched. This makes it more efficient than naive string searching algorithms, which have a time complexity of O(m*n).

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/KMPSearch.java]
```