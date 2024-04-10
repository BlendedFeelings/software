---
b: https://blendedfeelings.com/software/design/paxos.md
---

# Paxos 
is a family of protocols for solving consensus in a network of unreliable processors (which are referred to as nodes or peers). Consensus is the process of agreeing on one result among a group of participants. This is particularly important in distributed systems where processes need to agree on a single value that will be used, despite the possibility of failures.

Paxos was first described by Leslie Lamport in 1989 and is designed to operate in systems where nodes can fail or messages can be delayed, without requiring strict real-time bounds on message delivery. The key idea of Paxos is to find a value that a majority of nodes will agree upon.

Here is a high-level overview of how Paxos works:

1. **Roles**: Nodes in a Paxos system can take on three roles: proposers, acceptors, and learners.
   - **Proposers** suggest values to be chosen.
   - **Acceptors** agree on proposed values and choose one.
   - **Learners** learn the chosen value.

2. **Phases**: Paxos operates in two phases, each with two steps:
   - **Phase 1 (Prepare):**
     - **a.** A proposer selects a proposal number and sends a prepare request to a majority of acceptors.
     - **b.** If an acceptor receives a prepare request with a number greater than any it has previously seen, it promises not to accept any more proposals with a lower number and replies with the highest-numbered proposal (if any) it has accepted.
   - **Phase 2 (Accept):**
     - **a.** If the proposer receives responses from a majority of acceptors, it sends an accept request to each of those acceptors for a proposal with its number and the value of the highest-numbered proposal it received (or its own value if none were returned).
     - **b.** If an acceptor receives an accept request for a proposal numbered higher than any it has promised to consider, it accepts the proposal and notifies the proposer and all learners.

3. **Chosen Value**: A value is chosen when a majority of acceptors have accepted a proposal. Once a value is chosen, learners can be informed, and the system can act on the chosen value.

Paxos ensures safety (no two nodes decide on different values) and eventual liveness (the system eventually decides on a value, assuming a majority of nodes are functioning correctly and can communicate).

However, Paxos is known to be complex and difficult to understand and implement correctly. It has been used as the foundation for many distributed systems but often with modifications to suit particular use cases. Variants of Paxos, like Multi-Paxos, have been developed to handle multiple consensus rounds more efficiently. Other consensus algorithms, such as Raft, have been proposed as more understandable alternatives to Paxos, with a focus on ease of understanding and implementation.