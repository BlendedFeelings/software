---
b: https://blendedfeelings.com/software/monitoring/runtime-instrumentation.md
---

# Runtime instrumentation 
refers to the practice of adding monitoring and measuring capabilities to a software application while it is running, without modifying its source code or requiring recompilation. This is achieved by using tools or frameworks that can dynamically attach to the application process and inject the necessary code to collect data about the application's behavior and performance.

Here are some key aspects of runtime instrumentation:

1. **Dynamic Attach**: Runtime instrumentation tools use various techniques to attach to a running application process. For example, they may use platform-specific APIs to inject probes or hooks into the application's memory space.

2. **Data Collection**: Once attached, these tools can collect a wide range of data, such as function call timings, memory usage, thread activity, and I/O operations. The collected data is typically sent to a monitoring system or logged for later analysis.

3. **Minimal Code Changes**: Runtime instrumentation allows developers and operators to monitor applications without needing to make code changes, which is particularly useful for troubleshooting issues in production environments where modifying and redeploying code may be impractical.

4. **Overhead Considerations**: While runtime instrumentation is less invasive than modifying source code, it can still introduce performance overhead. Tool developers often take great care to minimize this impact, but the level of overhead will depend on the amount and type of data being collected.

5. **Profiling and Tracing**: Runtime instrumentation is often used for profiling (measuring performance characteristics) and tracing (recording the sequence of operations performed by the application).

6. **Agent-Based Monitoring**: Many runtime instrumentation tools operate by deploying an agent—a small piece of software that runs within the application's environment and performs the instrumentation.

7. **Platform and Language Support**: Different runtime instrumentation tools support different programming languages and platforms. Some tools are language-specific, while others are more general-purpose.

Examples of runtime instrumentation tools and techniques include:

- **Java Agents**: In the Java Virtual Machine (JVM), agents can be attached to a running Java application using the Java Instrumentation API to modify bytecode and collect data.

- **.NET Profilers**: The .NET runtime allows profilers to attach to a running .NET application to collect performance data.

- **Dynamic Tracing Tools**: Tools like DTrace (on Solaris and BSD) and SystemTap (on Linux) can dynamically insert tracing into a running kernel or user-space application.

- **APM (Application Performance Management) Tools**: APM tools like New Relic, AppDynamics, and Dynatrace use runtime instrumentation to provide real-time performance monitoring and insights.

- **eBPF (Extended Berkeley Packet Filter)**: On Linux, eBPF allows for highly efficient runtime instrumentation of both the kernel and user-space applications with minimal overhead.

Runtime instrumentation is a powerful technique for understanding the behavior of complex software systems, especially when dealing with issues that are difficult to reproduce in a development environment. It enables developers and operations teams to gain visibility into production workloads, diagnose issues, and optimize performance without disrupting the service.

Attaching to a running application process for runtime instrumentation can be achieved through various techniques, depending on the operating system, programming language, and the tools being used. Below are some of the common techniques employed for runtime instrumentation:

1. **Dynamic Linking and Loading**: Many operating systems allow dynamic loading of shared libraries at runtime. Instrumentation tools can leverage this to inject a shared library into a running process, which can then intercept and wrap function calls.

2. **Debugging Interfaces**: Operating systems often provide debugging interfaces (e.g., ptrace on Linux, or the Windows Debugging API) that allow tools to control and inspect the state of a running process. These interfaces can be used to insert breakpoints, read or write memory, and modify the execution flow for instrumentation purposes.

3. **Profiling APIs**: Some programming languages and runtime environments provide APIs specifically designed for profiling and instrumentation. For example, the Java Virtual Machine (JVM) provides the Java Instrumentation API that allows Java agents to transform bytecode at load time or even after a class has been loaded.

4. **Service Hooks**: Some systems provide hooks or callbacks that can be registered to listen for specific events or intercept function calls. Instrumentation tools can use these hooks to collect data when certain actions occur within the application.

5. **Bytecode Instrumentation**: For languages that run on virtual machines (like Java or .NET), tools can modify the bytecode or intermediate language (IL) code as it is being loaded into the VM. This allows for the insertion of instrumentation code without altering the original source code.

6. **eBPF (Extended Berkeley Packet Filter)**: On Linux, eBPF allows for the creation of safe, efficient programs that run in the kernel space. These programs can be attached to various points in the kernel or user-space processes to collect data or modify behavior.

7. **Aspect-Oriented Programming (AOP)**: In languages that support AOP (e.g., Java with AspectJ), aspects can be dynamically weaved into the application at runtime to add instrumentation code around certain join points, such as method calls or field accesses.

8. **Binary Instrumentation**: Tools like Pin or Dyninst can modify the running executable at the binary level to insert instrumentation. This is done by rewriting instructions or inserting trampolines to redirect execution flow.

9. **Code Injection**: Techniques such as function hooking or detouring involve modifying a process's memory to intercept function calls. This can be done by changing the function pointers or inserting jump instructions to redirect calls to instrumentation code.

10. **System Tracing Facilities**: Tools like DTrace, SystemTap, and LTTng provide system-wide tracing facilities that can instrument both kernel and user-space code. They use high-level scripting languages to specify what data to collect and where to collect it from.