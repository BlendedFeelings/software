---
b: https://blendedfeelings.com/software/design/quorum.md
---

# Quorum In distributed systems
is a concept used to ensure consistency and coordination among a set of nodes or processes that do not have a central authority to manage their state. A quorum is the minimum number of members that must participate in a decision or action for it to be considered valid and to proceed. Quorums are particularly important in the context of fault tolerance and are used to handle partial system failures where some nodes might be unreachable or down.

The idea of a quorum comes from the world of governance and decision-making, where it refers to the minimum number of members of an assembly or group that must be present to make the proceedings of that group valid.

In distributed systems, quorums are used in several ways, including:

1. **Write quorums**: To ensure that data is reliably written to the system, a write operation might require acknowledgment from a quorum of nodes before it is considered successful. This ensures that enough replicas of the data have been updated to withstand a certain number of node failures.

2. **Read quorums**: To ensure that data is reliably read from the system, a read operation might require responses from a quorum of nodes. This ensures that the read data is up-to-date and has been confirmed by a majority of the nodes.

3. **Majority quorums**: The most common form of quorum is a majority quorum, where more than half of the nodes must agree for an operation to be considered valid. This ensures that there is only one group of nodes that can make decisions and avoid split-brain scenarios where two separate groups think they are in charge.

4. **Dynamic quorums**: In some systems, the size of the quorum may be adjusted dynamically based on the number of nodes that are currently operational. This can help maintain availability even when many nodes fail.

5. **Byzantine fault tolerance**: In systems that need to tolerate Byzantine faults (where nodes can fail in arbitrary ways, including acting maliciously), more sophisticated quorum systems are needed, often requiring a larger number of nodes to agree to counteract the potential for malicious behaviour.

Quorum-based systems often use consensus algorithms like Paxos, Raft, or Zab to agree on system states or values. These algorithms are designed to ensure that the system can reach agreement even in the face of failures, network partitions, or delays.

The use of quorums is a critical aspect of distributed databases, distributed file systems, and other distributed storage systems, where data consistency and availability are paramount. It's a trade-off between consistency, availability, and partition tolerance, as described by the CAP theorem.