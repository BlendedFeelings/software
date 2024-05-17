---
b: https://blendedfeelings.com/software/concurrent-programming/torn-read.md
---

# Torn read 
refers to a situation in a computing context where a read operation on a data structure gets partial or inconsistent data due to concurrent modification of the data. This can happen when multiple threads are accessing and modifying the same data without proper synchronization.

For example, consider a 64-bit integer on a 32-bit system. If one thread is trying to read the 64-bit value while another thread is updating it, the reading thread might get the first 32 bits before the update and the last 32 bits after the update, resulting in a "torn" value that never actually existed in memory as a whole.

Torn reads can lead to unpredictable behavior in multithreaded applications and are typically prevented by using synchronization mechanisms such as locks, mutexes, or atomic operations that ensure that reads and writes to shared data are not interleaved in ways that can cause inconsistencies.