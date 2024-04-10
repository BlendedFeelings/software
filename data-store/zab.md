---
b: https://blendedfeelings.com/software/data-store/zab.md
---

# ZooKeeper Zab (ZooKeeper Atomic Broadcast) algorithm 
is a crash-recovery atomic broadcast algorithm used by Apache ZooKeeper for replicating data across all the nodes in the ZooKeeper ensemble (cluster). The Zab protocol is designed to guarantee the consistency and reliability of updates to the distributed data store that ZooKeeper manages.

Here's a high-level overview of how the Zab algorithm works:

1. **Leader Election**: When a ZooKeeper ensemble starts up or after a leader failure, the nodes perform a leader election to choose a new leader. The leader is responsible for handling write requests and coordinating updates to the data store.

2. **Discovery Phase**: Once a leader is elected, it enters the discovery phase. In this phase, the leader collects information about the most recent proposals (transactions) from all the followers to ensure that it has the most up-to-date state.

3. **Synchronization Phase**: The leader then synchronizes its state with all the followers. This involves sending any missing proposals to the followers so that all nodes have the same set of committed transactions.

4. **Broadcast Phase**: After synchronization, the leader enters the broadcast phase, where it can start processing client requests. When a write request is received, the leader creates a proposal and broadcasts it to all followers.

5. **Acknowledgment and Commit**: Each follower, upon receiving a proposal, writes it to its transaction log and sends an acknowledgment back to the leader. Once the leader has received acknowledgments from a quorum of nodes (a majority), it commits the proposal and sends a commit message to the followers. The followers then also commit the proposal.

6. **Client Response**: After the commit, the leader sends a response back to the client, indicating that the write operation has been successfully replicated across the ensemble.

The Zab protocol ensures that all committed updates are delivered in the same order to all ZooKeeper servers, which is crucial for maintaining a consistent state across the cluster. In the event of failures, such as a leader crash, the protocol can recover and continue to provide a reliable service without losing any committed updates.

Zab is specifically tailored for ZooKeeper's use case of managing a distributed coordination service and is not a general-purpose consensus algorithm like Paxos or Raft. However, it shares some similarities with these algorithms, particularly in terms of achieving consensus across a distributed set of nodes.