---
b: https://blendedfeelings.com/software/concurrent-programming/deadlock.md
---

# Deadlock 
is a situation in computer science where a set of processes or threads are blocked because each process is waiting for a resource that another process holds, and none of them can proceed. Deadlock is a common issue in concurrent programming when multiple processes must lock multiple resources.

There are four necessary conditions for a deadlock to occur, known as the Coffman conditions:

1. **Mutual Exclusion**: At least one resource must be held in a non-shareable mode; that is, only one process can use the resource at any given moment.

2. **Hold and Wait**: A process is currently holding at least one resource and requesting additional resources that are being held by other processes.

3. **No Preemption**: Resources cannot be forcibly removed from the processes that are holding them; resources must be released voluntarily.

4. **Circular Wait**: There must be a circular chain of two or more processes, each of which is waiting for a resource held by the next member of the chain.

### Example of Deadlock:
Consider two processes, P1 and P2, and two resources, R1 and R2.
- P1 holds R1 and needs R2 to proceed.
- P2 holds R2 and needs R1 to proceed.
Both processes are waiting for the other to release the resource they need, creating a cycle of dependency with no way to break it. This leads to a deadlock.

### Handling Deadlocks:
There are several strategies for handling deadlocks:

- **Deadlock Prevention**: Modify the system to invalidate one of the four necessary conditions. For example, ensuring that at least one of the conditions like mutual exclusion or hold and wait cannot occur.
  
- **Deadlock Avoidance**: Use an algorithm that ensures the system will never enter an unsafe state. Algorithms like Banker's algorithm can be used to pre-calculate the allocation of resources to prevent deadlocks.
  
- **Deadlock Detection and Recovery**: Allow deadlocks to occur, detect them when they do, and take action to recover. This can involve killing processes or forcing them to release resources.
  
- **Ostrich Algorithm**: Ignore the problem altogether, which can be an acceptable approach if deadlocks occur very rarely and the cost of prevention is higher than the cost of the problem itself.

### Recovery from Deadlock:
Once a deadlock is detected, the system must recover from it. Recovery methods include:

- **Process Termination**: Killing one or more processes involved in the deadlock.
- **Resource Preemption**: Forcibly taking a resource from a process and giving it to another process.

Deadlocks can be particularly troublesome in complex systems with many interdependent resources and processes. It is crucial to design systems carefully to either prevent deadlocks or ensure that they can be detected and recovered from with minimal impact on the system's operation.