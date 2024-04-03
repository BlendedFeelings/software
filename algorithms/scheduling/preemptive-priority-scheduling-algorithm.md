---
b: https://blendedfeelings.com/software/algorithms/scheduling/preemptive-priority-scheduling-algorithm.md
---

# Preemptive Priority Scheduling
is a process scheduling algorithm that selects processes based on priority and allows for preemption if a process with a higher priority arrives while a lower priority process is executing. The CPU is allocated to the process with the highest priority (the smallest priority number, if we consider 1 to be the highest priority). If two processes have the same priority, FCFS scheduling is used to break the tie.

Here are the key characteristics of Preemptive Priority Scheduling:

1. **Preemptive**: A running process can be interrupted and moved back to the ready queue if a new process with a higher priority arrives.

2. **Priority-Based**: Each process is assigned a priority. Processes with higher priority are executed first.

3. **Starvation**: Lower priority processes may suffer starvation if higher priority processes keep arriving. Starvation can be mitigated using aging techniques, which gradually increase the priority of waiting processes.

4. **Overhead**: There is overhead from the need to handle the preemption and context switch between processes.

5. **Complexity**: It is more complex to implement compared to non-preemptive algorithms like FCFS because it requires a mechanism to handle the interruption and resumption of processes.

6. **Response Time**: It can offer good response times for high priority processes.

To implement Preemptive Priority Scheduling, you would typically maintain a priority queue and follow these steps:

1. As processes enter the system, insert them into the priority queue based on their priority.
2. The CPU scheduler picks the process with the highest priority from the queue.
3. If a new process arrives with a higher priority than the currently running process, preempt the current process and move it back to the ready queue.
4. If the current process finishes or is preempted, choose the next highest priority process from the queue.
5. Repeat steps 2-4 until all processes have been executed.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/scheduling/PreemptivePriorityScheduling.java]
```