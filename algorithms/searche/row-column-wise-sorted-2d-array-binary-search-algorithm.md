---
b: https://blendedfeelings.com/software/algorithms/searche/row-column-wise-sorted-2d-array-binary-search-algorithm.md
---

# RowColumnWiseSorted2dArrayBinarySearch 
is a search algorithm used to find a specific value in a two-dimensional array that is sorted in both row-wise and column-wise directions.

The algorithm starts by comparing the target value with the middle element of the matrix. If the target value is less than the middle element, then the search is performed on the submatrix to the left of the middle element. If the target value is greater than the middle element, then the search is performed on the submatrix to the right of the middle element. If the target value is equal to the middle element, the search ends and the index of the element is returned.

If the target value is not found in the middle element, then the algorithm checks if the target value is greater than or less than the middle element. If the target value is greater than the middle element, then the search is performed on the submatrix below the middle element. If the target value is less than the middle element, then the search is performed on the submatrix above the middle element.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/RowColumnWiseSorted2dArrayBinarySearch.java]
```