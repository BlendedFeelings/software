---
b: https://blendedfeelings.com/software/concurrent-programming/livelock.md
---

# Livelock 
is a situation similar to a deadlock in concurrent programming. In a livelock, two or more processes or threads are effectively stuck in a loop, where each process is unable to make progress because the other processes are continuously changing their state in response to changes in the others. Unlike a deadlock, where processes do nothing and wait indefinitely, in a livelock, processes remain active but are unable to complete their tasks.

### Characteristics of Livelock:
- **Busy Waiting**: Processes or threads involved in a livelock are not idle; they are actively performing operations, such as retrying an action, responding to others' actions, or waiting for some condition to change.
- **Lack of Progress**: Despite being active, none of the processes can move forward with their intended tasks.
- **Cyclic Dependencies**: The processes' actions are often in response to the state of other processes, leading to a cycle where each process's actions provoke a reaction from the others.

### Example of Livelock:
Consider two processes, P1 and P2, that are programmed to be polite and give way to each other when they encounter a conflict for a shared resource.

- P1 notices that P2 wants the same resource, so it steps back to allow P2 to use it.
- P2, also being polite, notices that P1 was using the resource first and steps back to allow P1 to use it.
- Both processes are now in a state where they continuously yield to each other, never acquiring the resource they need.

### Handling Livelocks:
Livelocks can be difficult to detect because the system is not idle; however, they can be handled by:

- **Randomization**: Introduce randomness in the decision-making process to break the symmetry of the situation. For example, processes could wait for a random amount of time before retrying an action.
- **Backoff Protocol**: Implement a backoff protocol where a process waits for a progressively longer period after each failed attempt to perform an action.
- **Priority Assignment**: Assign different priorities to different processes or change priorities over time to ensure that one process can make progress over the others.

### Difference from Deadlock:
The key difference between a livelock and a deadlock is that in a livelock, processes or threads are actively trying to resolve the situation but fail to make any progress, while in a deadlock, processes are stuck waiting and do nothing.

Livelocks are generally less common than deadlocks but can be just as problematic. They can degrade system performance and lead to inefficiencies because the system resources are being consumed without accomplishing any useful work. It is important to design concurrency control mechanisms that prevent both deadlocks and livelocks to ensure the smooth operation of concurrent systems.