---
b: https://blendedfeelings.com/software/low-level/computer-architecture/out-of-order-execution.md
---

# CPU out-of-order execution 
is a feature in many high-performance microprocessors to make use of instruction cycles that would otherwise be wasted due to delays. Instead of processing the instruction sequence strictly in the program order, the processor executes instructions as soon as their operands are available and there is an available execution unit for the instruction, which may not be in the original program order.

Here's how out-of-order execution generally works:

1. **Instruction Fetch**: Instructions are fetched from memory in order.

2. **Instruction Decode**: Instructions are decoded into a format that can be understood by the execution units.

3. **Register Renaming**: To avoid false data dependencies, physical registers are used to hold the data, separating them from the logical registers specified by the instruction set architecture.

4. **Issue**: Instructions are issued to an instruction pool (also known as a reservation station or a reorder buffer) where they wait until their operands are ready.

5. **Execution**: Once all of an instruction's operands are available and there is an execution unit free, the instruction is executed out of order.

6. **Completion**: After execution, the results are held in a temporary location.

7. **Commit (Retirement)**: The results of the instructions are written back in the original program order. This step ensures that the program state remains consistent and that in the event of an exception or branch misprediction, the processor can roll back to a known good state.

Out-of-order execution allows the processor to make better use of its resources by overlapping the execution of multiple instructions. It can significantly increase the performance of a processor, as it can hide latencies in instruction execution, especially in the presence of slow operations like cache misses or branch mispredictions.

However, out-of-order execution adds complexity to the processor design, as it requires additional hardware to track the state of instructions in the pipeline, handle the results of the execution, and ensure that the instructions are committed in the correct order. Despite this complexity, out-of-order execution is a common feature in most high-performance processors because of the significant performance improvements it can provide.