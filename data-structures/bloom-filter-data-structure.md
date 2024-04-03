---
b: https://blendedfeelings.com/software/data-structures/bloom-filter-data-structure.md
---

# Bloom filter 
is a probabilistic data structure that is used to test whether an element is a member of a set. It is very efficient in terms of space, which makes it useful when dealing with large sets of data. However, because it is a probabilistic structure, it can have false positives, meaning it may sometimes report that an element is in the set when it is not. There are no false negatives; if a Bloom filter reports that an element is not in the set, it is definitely not in the set.

Here's how a Bloom filter works:

1. **Initialization**: You start with a bit array of `m` bits, all set to 0, and `k` different hash functions, each of which will map an element to one of the `m` bit positions.

2. **Adding elements**: To add an element to the Bloom filter, you pass it through all `k` hash functions to get `k` bit positions. You then set the bits at all these positions to 1.

3. **Querying for membership**: To check if an element is in the set, you pass it through the same `k` hash functions to get `k` bit positions. If any of the bits at these positions is 0, then the element is definitely not in the set. If all the bits are 1, then the element might be in the set, but there's a chance that those bits were set to 1 by other elements (this is where the possibility of false positives comes from).

4. **False Positive Rate**: The likelihood of false positives can be reduced by increasing the size of the bit array and the number of hash functions, but this also increases the space and computational requirements.

5. **No Deletion**: Standard Bloom filters do not support deletion of items from the set, as unsetting a bit might cause other items to be falsely reported as not in the set. However, there are variants like the Counting Bloom filter that support deletion.

Bloom filters are often used in situations where the space savings outweigh the cost of potential false positives, such as in network routers to avoid storing large routing tables, or by web browsers to check if a URL is in a list of malicious sites without storing the entire list.