---
b: https://blendedfeelings.com/software/algorithms/scheduling/first-come-first-serve-scheduling-algorithm.md
---

# First Come First Serve Scheduling (FCFS)
is one of the simplest types of process scheduling algorithms in operating systems. It operates exactly as its name suggests: the first process to arrive at the scheduler is the first one to get the CPU for execution.

Here are the key characteristics of FCFS scheduling:

1. **Non-Preemptive**: Once a process starts its execution, it cannot be preempted until it finishes its CPU burst time. It will run to completion.

2. **Simple and Intuitive**: It is easy to understand and implement. Processes are managed using a FIFO (First In, First Out) queue.

3. **No Starvation**: Since every process gets a chance to execute, there is no starvation. Every process will eventually be executed.

4. **Potentially Poor Performance**: It can lead to poor average response time, especially if a process with a long CPU burst arrives before processes with shorter CPU bursts.

5. **Convoy Effect**: A single long process can delay the execution of all other waiting processes, which is known as the convoy effect.

6. **Throughput**: The throughput of the system can be low because short processes may have to wait for a long process to finish.

7. **Turnaround Time**: The turnaround time can vary significantly depending upon the order of arrival of processes.

8. **Waiting Time**: The average waiting time under FCFS can be quite high, particularly when long processes occupy the CPU frequently.

To implement FCFS scheduling, you would typically maintain a queue and follow these steps:

1. As processes enter the system, put them at the end of the queue.
2. The CPU scheduler picks the first process from the queue, sets a timer to match the process's execution time, and runs it. If the process finishes before the timer goes off, the CPU scheduler chooses the next process in the queue immediately.
3. Repeat step 2 until all processes have been executed.


```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/scheduling/FCFSScheduling.java]
```