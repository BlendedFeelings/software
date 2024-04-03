---
b: https://blendedfeelings.com/software/concurrency/double-wide-compare-and-swap-cas.md
---

# Double-wide CA (Compare-And-Swap) 
refers to an atomic operation that can compare and swap two contiguous memory locations in a single, indivisible step. This is in contrast to the standard CAS operation, which typically operates on a single memory location.

The double-wide CAS is useful when you need to atomically update two related pieces of data without the risk of another thread intervening and causing inconsistencies. For example, you might use a double-wide CAS to update a pointer and its associated counter atomically, ensuring that other threads see both changes simultaneously or none at all.

Here's a conceptual overview of how a double-wide CAS works:

1. The operation takes four parameters: two expected old values (`oldValue1` and `oldValue2`) and two new values (`newValue1` and `newValue2`) to store if the comparison is successful.
2. It atomically compares the current values at two contiguous memory locations to `oldValue1` and `oldValue2`.
3. If the current values match the expected old values, the operation swaps both locations to `newValue1` and `newValue2` respectively.
4. The operation returns a boolean indicating whether the swap was successful.

The actual implementation of double-wide CAS depends on the hardware and the programming language. Some processors provide a specific instruction for this operation (e.g., the `CMPXCHG16B` instruction on x86-64 processors). In programming languages, this operation might be exposed through atomic libraries or intrinsic functions.

Here's an example of how you might use a double-wide CAS in pseudo-code:

```pseudo
// Pseudo-code for a double-wide CAS operation
function doubleWideCAS(memoryAddress1, memoryAddress2, oldValue1, oldValue2, newValue1, newValue2):
    if (atomic_compare_and_swap_double(memoryAddress1, memoryAddress2, oldValue1, oldValue2, newValue1, newValue2)):
        return true // The swap was successful
    else:
        return false // The swap failed because the expected values did not match
```

In real-world programming, you would need to use the appropriate functions or methods provided by your language's standard library or by your processor's instruction set. For example, in C++ you might use atomic operations from the `<atomic>` header, and in Java, you might use classes from the `java.util.concurrent.atomic` package.

Keep in mind that not all platforms support double-wide CAS natively, and on such platforms, you may need to use locks or other synchronization mechanisms to achieve the same effect, albeit with potential performance implications.