---
b: https://blendedfeelings.com/software/hash/fnv.md
---

# Fowler–Noll–Vo (FNV) hash functions 
are a family of non-cryptographic hash functions created by Glenn Fowler, Landon Curt Noll, and Phong Vo. They are designed to be fast and efficient for hashing data in hash tables and can be used in various applications where a non-cryptographic hash is suitable.

There are two primary variants of the FNV hash: FNV-1 and FNV-1a.

### FNV-1

The algorithm for FNV-1 is as follows:

1. Initialize the hash value to an offset basis.
2. For each byte of data:
   - Multiply the current hash value by a prime number (FNV prime).
   - XOR the current hash value with the byte of data.

The initial hash value (offset basis) and the prime number depend on the size of the hash you want to produce (e.g., 32-bit, 64-bit).

### FNV-1a

The FNV-1a variant is very similar to FNV-1, but it switches the order of the XOR and the multiplication:

1. Initialize the hash value to an offset basis.
2. For each byte of data:
   - XOR the current hash value with the byte of data.
   - Multiply the current hash value by a prime number (FNV prime).

This small change can result in different hash values and can improve the dispersion of the hash values for certain types of data.

### Parameters for 32-bit Hash

- **Offset basis (32-bit):** 2166136261
- **FNV prime (32-bit):** 16777619

### Example in Pseudocode

Here is a simple pseudocode example for FNV-1a:

```
function fnv1a(data):
    hash = 2166136261 # 32-bit offset basis
    prime = 16777619 # 32-bit FNV prime
    
    for each byte in data:
        hash = hash XOR byte
        hash = hash * prime
    
    return hash
```

### Usage Considerations

- FNV hashes are not suitable for cryptographic purposes because they are not designed to be resistant to collisions or to hide the original data.
- They are often used for hash tables, checksums, and unique identifiers within non-cryptographic contexts.
- FNV-1 and FNV-1a are sensitive to the order of the data; changing the order of bytes will result in a different hash value.
- The choice between FNV-1 and FNV-1a can be based on empirical testing with the specific data types and patterns you expect to encounter in your application.

Keep in mind that for real-world applications, you would use a well-tested implementation of these algorithms, as subtle implementation details can significantly affect the performance and distribution of the hash values.