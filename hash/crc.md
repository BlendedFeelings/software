---
b: https://blendedfeelings.com/software/hash/crc.md
---

# Cyclic Redundancy Check (CRC) 
is a type of hash function used to detect accidental changes to raw data in digital networks and storage devices. It is a form of checksum that calculates a fixed-size binary value from an arbitrary block of digital data for the purpose of detecting accidental changes to the data.

The CRC is based on polynomial division, where the dividend is the data converted to a binary number and the divisor is a fixed binary number, known as the 'generator polynomial.' The result of the division is the CRC value, which can be appended to the data. When the data with the CRC is received, the same polynomial division is performed, and if the remainder is non-zero, an error is detected.

The CRC algorithm involves binary arithmetic with no carries (XOR operations), and the generator polynomial is chosen to maximize the error-detecting capabilities.

Here is a simple example of how to compute a CRC in Python using the `binascii` module, which includes an implementation of the CRC-32 algorithm:

```python
import binascii

# Sample data
data = b'Hello, World!'

# Calculate CRC-32 checksum
crc_value = binascii.crc32(data)

print(f'The CRC-32 value is: {crc_value:#010x}')
```

In this example, `crc32` function computes the CRC-32 checksum of the data, and the result is formatted as a hexadecimal value with a `0x` prefix and zero-padded to 8 digits.

Please note that there are many different CRC algorithms, each with its own generator polynomial and properties. The CRC-32 algorithm is commonly used, but others like CRC-16, CRC-CCITT, and CRC-64 are also in use for different applications.