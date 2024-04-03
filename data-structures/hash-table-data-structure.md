---
b: https://blendedfeelings.com/software/data-structures/hash-table-data-structure.md
---

# Hash table 
also known as a hash map, is a data structure that implements an associative array, a structure that can map keys to values. It provides a way to store and retrieve data efficiently based on a key. Hash tables are widely used because of their fast average-case time complexity for each of the basic operations: insertion, deletion, and lookup.

### How a Hash Table Works

1. **Hash Function**: A hash table uses a hash function to compute an index into an array of slots, from which the desired value can be found. The hash function takes a key and converts it into an integer index, which corresponds to the position in the hash table where the value should be stored.

2. **Handling Collisions**: Since the range of possible keys can be much larger than the number of indices in the array, different keys may produce the same index. This is known as a collision. Hash tables use various collision resolution techniques to handle this issue, such as:
   - **Chaining**: Each slot in the array points to a linked list of entries that have the same index. When a collision occurs, the item is added to the end of the list.
   - **Open Addressing**: When a collision occurs, the hash table searches for the next available slot according to a probing sequence (linear probing, quadratic probing, or double hashing).

3. **Load Factor**: The load factor is a measure of how full the hash table is. It is defined as the number of entries divided by the number of slots. A higher load factor means more collisions are likely. To maintain efficient performance, hash tables often resize dynamically as items are added or removed.

4. **Resizing**: When the load factor exceeds a certain threshold, the hash table may need to be resized. This involves creating a new, larger hash table, rehashing all the existing keys, and inserting them into the new table.

### Time Complexity

- **Average Case**: O(1) for insertion, deletion, and lookup.
- **Worst Case**: O(n) for insertion, deletion, and lookup, where n is the number of entries. This occurs when all keys hash to the same index, effectively creating a linked list.

### Applications

Hash tables are used in many applications, including:
- Implementing associative arrays or dictionaries.
- Database indexing.
- Caching (e.g., web page caching, DNS lookups).
- Object representation (e.g., objects in JavaScript or Python dictionaries).
- Compilers and interpreters (e.g., for variable and function lookups).

### Limitations

- Hash tables do not maintain the order of elements.
- The performance of a hash table is heavily dependent on the quality of the hash function and the load factor.
- Hash tables are not very efficient in terms of space when the load factor is kept low to avoid collisions.

In summary, hash tables are a fundamental data structure that provides efficient key-based access to data, making them a staple in software development for various applications.