---
b: https://blendedfeelings.com/software/design/leader-election.md
---

# Leader election 
is a fundamental problem in distributed systems where multiple processes or nodes must agree on a single process that will act as the "leader." This leader will typically coordinate actions among the nodes, make decisions, and perform tasks that require a single point of control. The leader election process ensures that even in the case of failures or network partitions, the distributed system can recover and continue to function correctly.

There are various algorithms and protocols to achieve leader election in distributed systems, each with its own advantages and trade-offs. Some of the well-known algorithms include:

1. **Bully Algorithm**: This algorithm assumes that each process has a unique and fixed priority number. When a process notices that the leader has failed, it initiates an election. The process with the highest priority number will become the new leader. Processes with lower priority numbers will withdraw if they receive an election message from a process with a higher priority.

2. **Ring Algorithm**: In this algorithm, each process is arranged in a logical ring. When an election is initiated, a process sends an election message around the ring. Each process passes the message along until it returns to the initiator, which then becomes the leader if it has the highest identifier.

3. **Raft**: Raft is a consensus algorithm designed to be easy to understand. It splits time into terms, and each term starts with an election to choose a single leader. The leader handles all client interactions and log replication. If a leader fails, a new term will start with a new election.

4. **Paxos**: Paxos is a family of protocols for solving consensus in a network of unreliable processors. Consensus is the process of agreeing on one result among a group of participants. Paxos is designed to have a minimum number of critical parts and to ensure consistency.

5. **ZooKeeper's Zab Protocol**: Apache ZooKeeper uses an algorithm called Zab for leader election and message ordering. It is designed for high-performance coordination service for distributed applications.

6. **Multi-Paxos**: This is an optimization of Paxos that provides a more efficient way to handle a sequence of consensus problems, such as a log of commands in state machine replication.

7. **Viewstamped Replication**: This is another approach to the consensus problem that is similar to Paxos and Raft but predates them. It also uses a view-change protocol to ensure that a new leader can be elected if the current leader fails.

Leader election protocols must handle various challenges such as network delays, partitions, and the possibility of nodes crashing or recovering. The correctness properties that these protocols aim to achieve include safety (never electing more than one leader at a time) and liveness (eventually electing a leader despite failures).