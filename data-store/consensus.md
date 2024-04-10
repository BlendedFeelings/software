---
b: https://blendedfeelings.com/software/data-store/consensus.md
---

# Consensus in distributed systems 
refers to the agreement among multiple components (like servers, processes, or nodes) on a single data value or a single state of the system. It is a fundamental challenge in distributed computing because of issues like network failures, message delays, and the presence of faulty or malicious nodes.

Consensus algorithms are designed to achieve reliability in a network involving multiple unreliable nodes. These algorithms ensure that all non-faulty nodes can agree on the same value, even in the presence of a number of faulty nodes.

Key properties that a consensus algorithm aims to achieve are:

1. **Termination**: Eventually, every correct process must make a decision and stop participating in the consensus protocol.
2. **Agreement**: All correct processes must agree on the same value.
3. **Validity**: If all correct processes receive the same input value, then they must all output that value.
4. **Integrity**: Each correct process decides at most once, and if it decides some value, then it must have been proposed by some process.

Some well-known consensus algorithms used in distributed systems include:

- **Paxos**: A family of protocols for solving consensus in a network of unreliable processors. Paxos is based on the concept of a "majority" and is known for being fault-tolerant.
- **Raft**: Similar to Paxos in fault tolerance and performance but is designed to be more understandable.
- **Practical Byzantine Fault Tolerance (PBFT)**: An algorithm that can provide consensus even when there are malicious nodes in the network, as long as the number of malicious nodes is less than one-third of all nodes.
- **Proof of Work (PoW)**: Used in blockchain systems like Bitcoin, it requires a node to solve a computationally hard problem to propose a new block.
- **Proof of Stake (PoS)**: Another blockchain consensus mechanism that selects validators in proportion to their quantity of holdings in the associated cryptocurrency.

Consensus is crucial in systems that require consistency and coordination, such as databases, filesystems, and blockchain technologies. Each algorithm has its trade-offs in terms of performance, fault tolerance, and the conditions under which they can guarantee consensus.