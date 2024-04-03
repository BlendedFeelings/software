---
b: https://blendedfeelings.com/software/design/state-machine-replication.md
---

# State machine replication (SMR) 
is a fundamental concept in distributed systems used to ensure consistency across multiple servers or nodes. The idea behind SMR is to have each server implement the same deterministic state machine, where the state machine is an abstract model that consists of a state and a set of transitions that change the state based on input commands.

In a distributed system, ensuring that every replica processes the same sequence of inputs in the same order is crucial for maintaining a consistent state across all replicas. State machine replication achieves this by coordinating the replicas so that they execute the same commands in the same order.

Here's how state machine replication typically works in distributed systems:

1. **Command Propagation**: A client sends a command to one of the replicas, which acts as a leader or coordinator.
   
2. **Agreement Protocol**: The leader replicates the command to the other replicas using a consensus algorithm like Paxos, Raft, or Multi-Paxos. The goal of the consensus algorithm is to ensure that a majority of replicas agree on the sequence of commands to be executed, even in the presence of failures.

3. **Command Execution**: Once consensus is reached, each replica executes the command on its local state machine. Because the state machines are deterministic and the commands are executed in the same order, each replica's state machine transitions to the same new state.

4. **Response to Client**: After executing the command, the replicas send a response back to the client. In some systems, the client waits for responses from a majority of replicas to ensure that the command has been committed.

5. **State Machine Updates**: The state machine on each replica is updated according to the command, and the system continues to process further commands.

State machine replication is widely used because it provides strong consistency guarantees and fault tolerance. If some replicas fail, the system can continue to operate as long as a majority of replicas are functioning and can agree on command sequences.

Using a consensus algorithm is crucial in state machine replication because it handles the complexities of distributed systems, such as network partitions, message loss, and replica failures. Different consensus algorithms have different properties and trade-offs in terms of latency, throughput, and fault tolerance.

SMR is the core of many distributed data stores and services that require high availability and consistency, such as distributed databases, filesystems, and configuration management systems.