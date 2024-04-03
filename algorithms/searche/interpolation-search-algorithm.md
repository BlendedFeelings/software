---
b: https://blendedfeelings.com/software/algorithms/searche/interpolation-search-algorithm.md
---

# Interpolation Search
is an algorithm used to search for a specific value in a sorted array. It works by estimating the position of the target value based on its value and the values of the endpoints of the array.

The algorithm uses the following formula to estimate the position of the target value:

pos = low + ((high - low) / (arr[high] - arr[low])) * (x - arr[low])

Where low and high are the indices of the endpoints of the array, arr is the sorted array, and x is the target value.

The algorithm then checks the value at the estimated position. If it is equal to the target value, the algorithm returns the position. If it is greater than the target value, the algorithm searches the left half of the array. If it is less than the target value, the algorithm searches the right half of the array.

Interpolation Search has an average time complexity of O(log log n), making it faster than binary search for large arrays with uniformly distributed values. However, it can perform poorly for arrays with non-uniformly distributed values or when the target value is at the beginning or end of the array.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/InterpolationSearch.java]
```