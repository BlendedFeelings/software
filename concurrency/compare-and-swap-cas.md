---
b: https://blendedfeelings.com/software/concurrency/compare-and-swap-cas.md
---

# Compare-and-swap (CAS) 
is an atomic instruction used in multithreading to achieve synchronization without the need for locking mechanisms. It is a fundamental operation for building lock-free and wait-free data structures and algorithms.

The CAS operation takes three parameters:

1. A memory location (`dest`) that is to be modified.
2. An expected old value (`expected`) that we believe is currently in `dest`.
3. A new value (`new_value`) that we want to set at `dest`.

The operation works as follows:

- It atomically compares the current value at the memory location `dest` with the `expected` value.
- If the current value matches the `expected` value, it means that `dest` has not been modified by another thread since we last read it. In this case, the CAS operation atomically updates `dest` to the `new_value`.
- If the current value does not match the `expected` value, it means that some other thread has modified `dest`. The CAS operation does not perform any update in this case.

The CAS operation typically returns a boolean indicating whether the swap was successful, or it may return the actual value at `dest` before the operation (which can be used to check if the operation was successful).

Here's a conceptual representation of the CAS operation:

```pseudocode
function CompareAndSwap(pointer dest, value expected, value new_value) -> (bool, value):
    atomic {
        old_value = *dest
        if old_value == expected:
            *dest = new_value
            return (true, old_value) // Successful swap
        else:
            return (false, old_value) // Swap failed, value changed
    }
```

In many programming languages, the CAS operation is provided by the standard library or the language's runtime. For instance, in C#, the `Interlocked.CompareExchange` method performs a CAS operation. Here's how you might use it in C#:

```csharp
int oldValue = Interlocked.CompareExchange(ref destination, newValue, expectedValue);
bool wasSuccessful = (oldValue == expectedValue);
```

In this C# example, `Interlocked.CompareExchange` atomically compares the value at `destination` with `expectedValue`. If they match, `destination` is updated to `newValue`. The method returns the original value that was at `destination` before the operation. If `oldValue` equals `expectedValue`, the swap was successful; otherwise, it failed because another thread modified `destination`.

CAS is a powerful primitive for concurrent programming, but it requires careful design to avoid issues like the ABA problem and to ensure that algorithms are correct and perform well under contention.