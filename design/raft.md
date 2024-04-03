---
b: https://blendedfeelings.com/software/design/raft.md
---

# Raft consensus algorithm 
is a protocol for managing a replicated log. It is used to ensure that multiple servers agree on the contents of this log, which is crucial for maintaining a consistent state across a distributed system. Raft is designed to be easy to understand and it's often used as a more understandable alternative to the Paxos algorithm.

Here are the key components and concepts of Raft:

1. **Consensus**: The primary goal of Raft is to allow a cluster of servers to agree on a sequence of actions, such as data updates, in a way that ensures all servers see the same action sequence and any action that has been agreed upon is executed on all servers.

2. **Terms**: Raft divides time into terms, which are consecutive and each term starts with an election to choose one server as the leader. The leader handles all client interactions and log replication during its term. If the leader fails, a new term will begin with a new election.

3. **Election**: When a server starts a new term, it transitions to a candidate state and requests votes from other servers. The candidate becomes the leader if it receives votes from a majority of servers. If no candidate receives a majority, a new term will start, and a new election will take place.

4. **Log Replication**: Once a leader is elected, it begins accepting log entries from clients and replicates these entries to the other servers. The leader ensures that the other servers have the same log entries and commits the log entries in a consistent order.

5. **Safety**: Raft ensures safety by only allowing a server to become a leader if it has all the committed entries. It also uses a mechanism called "log matching" to ensure that the leader and follower logs are consistent.

6. **Committing Entries**: A log entry is considered committed when it has been safely replicated on a majority of servers. Once committed, the log entry can be applied to the server's state machine.

7. **Follower and Candidate States**: Servers in a Raft cluster can be in one of three states: leader, follower, or candidate. Followers passively replicate log entries and vote for leaders. Candidates actively seek to become leaders.

8. **Heartbeats**: The leader regularly sends heartbeat messages to all followers to maintain authority and prevent new elections.

The Raft algorithm is typically explained in terms of five subproblems it solves:

- Leader election
- Log replication
- Safety
- Leader changes (handling leader crashes and ensuring smooth transition)
- Membership changes (adding and removing servers from the cluster)

Raft is widely used in distributed systems and serves as the foundation for various distributed databases and coordination services. It is appreciated for its simplicity and the ease with which it can be implemented and understood compared to other consensus algorithms.