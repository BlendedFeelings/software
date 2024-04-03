---
b: https://blendedfeelings.com/software/algorithms/scheduling/round-robin-scheduling-algorithm.md
---

# Round-robin Scheduling
is a widely used process scheduling algorithm in operating systems that is designed to give each process an equal share of the CPU. It is a preemptive scheduling algorithm that is often used in time-sharing systems. The key concept of round-robin scheduling is the use of time slices or quantum, which is the fixed amount of time that each process is allowed to run before being preempted and moved to the back of the ready queue.

Here are the key characteristics of Round-robin Scheduling:

1. **Time Quantum**: Each process is given a fixed amount of time (time quantum) to run. If a process does not complete within this time, it is preempted and added to the end of the queue.

2. **Preemptive**: Processes are regularly interrupted to ensure that all processes receive equal CPU time, which allows for good responsiveness for all processes.

3. **Fairness**: All processes get an equal opportunity to execute, which ensures fairness among processes.

4. **Overhead**: There can be significant context-switching overhead if the time quantum is too small.

5. **Tuning**: The performance of round-robin scheduling can be tuned by adjusting the length of the time quantum. A larger quantum can reduce context switching but may lead to poorer response times, while a smaller quantum improves response time but increases overhead.

6. **Throughput**: Throughput depends on the time quantum and the context-switching time. It can be suboptimal if these are not well-tuned.

7. **No Priority**: RR does not take process priority into account unless it is combined with other schemes.

To implement Round-robin Scheduling, you would typically maintain a queue and follow these steps:

1. As processes enter the system, put them at the end of the queue.
2. The CPU scheduler picks the first process from the queue and sets a timer to the length of the time quantum.
3. The process runs. If it completes before the time quantum expires, it is removed from the system. If the time quantum expires and the process is still running, it is preempted and placed at the back of the queue.
4. The scheduler selects the next process in the queue and repeats step 3.
5. This continues until all processes have been completed.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/scheduling/RRScheduling.java]
```