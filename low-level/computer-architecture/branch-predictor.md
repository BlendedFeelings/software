---
b: https://blendedfeelings.com/software/low-level/computer-architecture/branch-predictor.md
---

# CPU branch predictor 
is a hardware component in modern microprocessors that attempts to guess the outcome of a branch (such as an if-then-else structure) before it is known for sure. The purpose of a branch predictor is to improve the flow in the instruction pipeline. Branch predictors play a critical role in achieving high performance in pipelined processors by allowing the processor to speculatively execute instructions ahead of the completion of a branch instruction.

Branch prediction is necessary because the outcome of a branch might not be determined until the previous instructions are completed, which could cause delays if the processor has to wait for the branch resolution before continuing execution. By guessing the outcome, the CPU can continue to fetch and execute instructions without waiting, which keeps the pipeline full and improves the overall throughput.

There are various types of branch predictors:

1. **Static Branch Predictors**: These make a prediction that is fixed throughout the execution of the program. For example, a simple static predictor might assume that backward branches (loops) are always taken and forward branches are not.

2. **Dynamic Branch Predictors**: These use runtime information to make predictions. They are more sophisticated and have a higher accuracy than static predictors. Examples include:
   - **Bimodal Predictors**: Use a table of 2-bit counters to predict whether a branch will be taken or not.
   - **Two-Level Adaptive Predictors**: Use a history of branch outcomes to make predictions.
   - **Hybrid Predictors**: Combine several prediction mechanisms to improve accuracy.

When a branch prediction is correct, the processor can continue executing without interruption. However, if the prediction is incorrect (a misprediction), the CPU must flush the speculative instructions from the pipeline and fetch the correct path, which can lead to performance penalties.

Modern CPUs have highly sophisticated branch predictors that use complex algorithms to achieve high accuracy rates, which is essential for maintaining high performance in deeply pipelined and superscalar processors.