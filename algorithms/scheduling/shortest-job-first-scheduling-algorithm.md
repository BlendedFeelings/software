---
b: https://blendedfeelings.com/software/algorithms/scheduling/shortest-job-first-scheduling-algorithm.md
---

# Shortest Job First Scheduling
also known as Shortest Job Next (SJN), is a process scheduling algorithm that selects the process with the smallest execution time to run next. SJF can be either preemptive or non-preemptive. In its non-preemptive variant, once a process starts its execution, it cannot be preempted until it finishes its CPU burst. In the preemptive variant, known as Shortest Remaining Time First (SRTF), the currently running process can be preempted if a new process with a shorter burst time arrives.

Here are the key characteristics of SJF Scheduling:

1. **Efficiency**: SJF can be very efficient because it minimises the average waiting time for a given set of processes.

2. **Non-Preemptive / Preemptive**: It can be implemented as a non-preemptive algorithm, where the shortest job is picked and runs to completion, or as a preemptive algorithm (SRTF), where the currently running process can be interrupted if a shorter job arrives.

3. **Starvation**: Longer processes may suffer from starvation because shorter processes will always be preferred.

4. **Prediction**: It requires prior knowledge of the CPU burst time for all processes, which is often not feasible in real-world scenarios. In practice, burst time can be estimated based on historical data.

5. **Overhead**: The preemptive version (SRTF) may have a higher overhead due to more frequent context switches.

6. **Throughput**: SJF can offer high throughput if most of the processes have short CPU bursts.

To implement SJF Scheduling, you would typically maintain a list of processes and follow these steps:

1. As processes enter the system, add them to the list.
2. Sort the list of processes by their CPU burst time.
3. If non-preemptive, pick the first process from the sorted list and run it to completion. If preemptive, always run the process with the shortest remaining time.
4. If a new process arrives (for preemptive SJF), sort the list again.
5. Repeat steps 2-4 until all processes have been executed.



```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/scheduling/SJFScheduling.java]
```