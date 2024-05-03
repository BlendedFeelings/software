---
b: https://blendedfeelings.com/software/hash/adler-32.md
---

# Adler-32 checksum 
is a checksum algorithm which was invented by Mark Adler. It is widely used in network protocols and file formats, notably in zlib compression library which is part of the PNG image format. The algorithm is simpler and faster than the CRC32 algorithm but is less reliable for protecting against intentional tampering with data.

The Adler-32 checksum is computed as follows:

1. The checksum is divided into two 16-bit components: `A` and `B`.
2. Initially, `A` is set to 1 and `B` is set to 0.
3. For each input byte `data[i]`:
   - `A` is updated to `(A + data[i]) mod 65521`
   - `B` is updated to `(B + A) mod 65521`
4. The Adler-32 checksum is then `(B << 16) | A`.

The number 65521 is a prime number that is used in the modulo operation, which is the largest prime number smaller than 2^16. This property helps in providing a good distribution of the checksum values.

Here is a simple implementation of the Adler-32 checksum in Python:

```python
def adler32(data):
    MOD_ADLER = 65521
    A = 1
    B = 0
    for byte in data:
        A = (A + byte) % MOD_ADLER
        B = (B + A) % MOD_ADLER
    return (B << 16) | A
```

You would call this function with a bytes-like object, for example:

```python
data = b"Hello, World!"
checksum = adler32(data)
print(f"Adler-32 Checksum: {checksum:#010x}")  # Print the checksum in hex format with leading '0x' and zero-padding
```

Please note that in a real-world application, you would typically use a library function for computing Adler-32 to ensure it's optimized and reliable. In Python, for instance, you could use the `zlib.adler32()` function.