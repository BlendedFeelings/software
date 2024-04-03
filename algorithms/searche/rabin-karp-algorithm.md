---
b: https://blendedfeelings.com/software/algorithms/searche/rabin-karp-algorithm.md
---

# Rabin-Karp
is a string searching algorithm that searches for a pattern in a text by using a hash function to compare the pattern with substrings of the text. It has a time complexity of O(n+m) in the worst case, where n is the length of the text and m is the length of the pattern. The algorithm is useful in cases where the pattern is relatively short and the text is relatively long.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/RabinKarpAlgorithm.java]
```