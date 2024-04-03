---
b: https://blendedfeelings.com/software/monitoring/tracing.md
---

# Tracing
refers to the process of monitoring and recording information about a program's execution. This can include a wide range of data, such as function calls, variable values, system events, and performance metrics. Tracing is often used for debugging purposes to understand the flow of execution and identify issues within the software. It can also be used for performance analysis, monitoring, and logging.

There are several levels and types of tracing:

1. **Static Tracing**: This involves inserting print statements or logging calls into the code, which output information to a console or log file when the program is run.

2. **Dynamic Tracing**: This uses tools or frameworks that attach to a running program to collect trace data. Dynamic tracing can often be enabled without modifying the source code and can be turned on or off as needed.

3. **Instrumentation**: This is a more sophisticated form of tracing where additional code is injected into the program, either statically at compile time or dynamically at runtime, to gather detailed information about the program's behavior.

4. **Profiling**: While not strictly tracing, profiling is related and involves measuring the performance of a program, such as the time spent in each function, the number of times functions are called, memory usage, and so on.

5. **Distributed Tracing**: In distributed systems or microservices architectures, tracing can span across multiple services and nodes, allowing developers to track a request as it travels through the different parts of the system.

6. **System Tracing**: This involves tracing system-level events, such as system calls, context switches, and I/O operations, which can help in understanding the interactions between the software and the operating system.

Tracing tools vary by language and platform, but some common ones include:

- **GDB**: A debugger for several languages, including C and C++, that can be used for tracing.
- **strace/ltrace**: Linux utilities for tracing system calls (strace) and library calls (ltrace).
- **DTrace**: A comprehensive dynamic tracing framework available on some Unix-like systems.
- **SystemTap**: A Linux tool similar to DTrace.
- **Zipkin, Jaeger**: Tools for distributed tracing in microservices.

Tracing can generate a huge amount of data, so it's important to have a strategy for managing this data, such as filtering and aggregation, to make the information useful and actionable.