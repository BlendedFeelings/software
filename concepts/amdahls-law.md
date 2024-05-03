---
b: https://blendedfeelings.com/software/concepts/amdahls-law.md
---

# Amdahl's Law 
is a formula used to find the maximum improvement possible by enhancing a particular part of a system. In computing, it is often used to predict the theoretical maximum speedup for program processing using multiple processors compared to a single processor.

The law is named after computer scientist Gene Amdahl, and it is used to highlight the potential speedup of a task's execution as a result of increasing the resources, typically in the context of parallel processing.

Amdahl's Law can be expressed by the following formula:

$$
S = \frac{1}{(1 - P) + \frac{P}{N}}
$$

Where:
- $S$ is the theoretical speedup of the execution of the whole task.
- $P$ is the proportion of the execution time that the enhanced component affects (0 ≤ P ≤ 1).
- $N$ is the speedup of the enhanced component (e.g., the number of processors).

The key insight from Amdahl's Law is that as $N$ increases, the speedup of the program tends towards $\frac{1}{1-P}$, meaning that there is a limit to the benefit gained from adding more processors. This is because the portion of the program that cannot be parallelized ($1-P$) does not benefit from additional processors.

Amdahl's Law is particularly important in parallel computing because it shows that adding more processing units has a diminishing return due to the sequential portion of a task. It emphasizes the importance of minimizing the non-parallelizable components of a task to maximize the effectiveness of parallelization.