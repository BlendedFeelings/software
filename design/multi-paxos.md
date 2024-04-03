---
b: https://blendedfeelings.com/software/design/multi-paxos.md
---

# Multi-Paxos 
is an optimization of the basic Paxos consensus algorithm that is designed to handle multiple consensus decisions (or multiple "instances" of consensus) in a more efficient manner. In a distributed system, it is common to have to reach agreement on a series of values or commands rather than just a single value. Multi-Paxos reduces the message overhead and latency associated with reaching consensus on each individual value by reusing the same set of acceptors and by electing a distinguished proposer called the leader.

Here's an overview of how Multi-Paxos works:

1. **Leader Election**: Multi-Paxos typically begins with a leader election phase, where one of the proposers is elected as the leader. The leader will be responsible for driving the consensus process for a sequence of values.

2. **Phase 1 (Prepare) Optimization**: In basic Paxos, Phase 1 must be completed for every consensus decision. In Multi-Paxos, Phase 1 is only necessary when a new leader is elected. Once a leader is established, it can skip Phase 1 for subsequent proposals, assuming it retains its leadership and the set of acceptors remains stable.

3. **Phase 2 (Accept)**:
   - **a.** The leader proposes values for a sequence of consensus instances by sending "accept" messages to the acceptors. It includes the instance number and the proposed value for each instance.
   - **b.** Acceptors respond to these proposals as in basic Paxos. If they have not promised to a higher-numbered proposal, they accept the leader's proposal and reply with an acknowledgment.

4. **Chosen Values**: As in basic Paxos, a value is chosen for a particular instance when a majority of acceptors have accepted the proposal for that instance. The leader informs the learners of the chosen values.

5. **Log Structure**: Multi-Paxos often uses a log structure to keep track of the sequence of chosen values. Each log entry corresponds to an instance of the consensus, and the leader proposes values to be appended to the log.

6. **Handling Leader Changes**: If the leader fails or becomes unreliable, a new leader election is triggered. The new leader will perform Phase 1 to establish its leadership and learn about any decisions made by the previous leader that it might have missed.

Multi-Paxos is more efficient than basic Paxos when there are multiple values to agree upon because it minimizes the number of messages required per consensus decision after the initial leader election. However, it still inherits the complexity of the Paxos algorithm and requires careful implementation to ensure correctness.

Multi-Paxos is widely used in distributed systems. For example, it forms the basis of the consensus mechanism in Google's Chubby lock service and in the replicated state machines of many distributed databases and storage systems.