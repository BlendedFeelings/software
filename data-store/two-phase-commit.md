---
b: https://blendedfeelings.com/software/data-store/two-phase-commit.md
---

# Two-phase commit (2PC) protocol 
is a distributed algorithm used in computer science to achieve consensus among nodes in a distributed system, ensuring that all nodes either commit to a transaction or abort it, thus maintaining data consistency across the distributed system. It is commonly used in distributed databases to ensure that all parts of a transaction are completed successfully or none at all.

Here's a high-level overview of how the two-phase commit protocol works:

### Phase 1: Voting Phase
1. **Transaction Initiation**: A coordinator node initiates the transaction process and sends a `VOTE_REQUEST` message to all participant nodes involved in the transaction.
2. **Voting**: Each participant node executes the transaction up to the point where it will either commit or abort and then votes. If the participant is ready to commit, it votes `YES` and logs this vote to stable storage. If it encounters an issue and decides to abort, it votes `NO`.
3. **Collection of Votes**: The coordinator collects all votes from the participants.

### Phase 2: Commit/Abort Phase
1. **Decision**: Based on the votes received, the coordinator makes a decision.
   - If all votes are `YES`, the coordinator decides to `COMMIT` the transaction.
   - If any vote is `NO`, or if there is a failure to communicate with any participant, the coordinator decides to `ABORT` the transaction.
2. **Broadcast Decision**: The coordinator sends the decision to all participants.
   - `COMMIT` message if the decision was to commit.
   - `ABORT` message if the decision was to abort.
3. **Acknowledgment**: Participants complete the action (commit or abort) based on the coordinator's decision and send an acknowledgment back to the coordinator.
4. **Completion**: Once all acknowledgments are received, the coordinator completes the transaction process.

### Properties
- **Atomicity**: The protocol ensures that all participants either commit or abort the transaction, which upholds the atomicity property of transactions.
- **Blocking**: If the coordinator fails after sending the `VOTE_REQUEST` and before the decision is made, participants may be left in a blocking state, unable to proceed because they don't know whether to commit or abort. This is one of the main drawbacks of the 2PC protocol.

### Failure Scenarios
- **Coordinator Failure**: If the coordinator fails before sending the decision, participants will not know whether to commit or abort and will be blocked.
- **Participant Failure**: If a participant fails after voting but before the decision is received, the protocol can handle this as long as the participant's vote is stored in stable storage. When the participant recovers, it can proceed based on the coordinator's decision.

The two-phase commit protocol is a fundamental concept in distributed systems, but it has limitations, especially regarding blocking and performance in the presence of failures. Alternative protocols like three-phase commit and Paxos have been developed to address some of these limitations.