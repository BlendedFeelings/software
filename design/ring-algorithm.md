---
b: https://blendedfeelings.com/software/design/ring-algorithm.md
---

# Ring Algorithm 
is another approach to leader election in distributed systems, particularly suited for systems organized in a logical ring topology. In this topology, each process is aware of its immediate successor on the ring, and communication only occurs between neighbors. The algorithm aims to elect a leader by circulating a message around the ring until all nodes have agreed on the leader.

Here is how the Ring Algorithm works:

1. **Election Initiation**: When a process, say `P`, detects that the current leader has failed or when the system starts up without a leader, `P` initiates an election.

2. **Election Message**: `P` creates an ELECTION message containing its own process ID and sends it to its successor in the ring.

3. **Message Passing**:
   - When a process receives an ELECTION message, it compares the ID in the message with its own.
   - If its own ID is greater, it replaces the ID in the message with its own and forwards the message to its successor.
   - If its own ID is smaller, it simply forwards the message without changes, unless the message already contains its ID, in which case it becomes the leader.
   - If its own ID is equal to the ID in the message, it means the message has made a full loop, and this process is the one with the highest ID, so it elects itself as the leader.

4. **Leader Announcement**: Once a process elects itself as the leader, it sends a COORDINATOR message around the ring to inform all other processes of the new leader.

5. **Acknowledgment**: As each process receives the COORDINATOR message, it marks the sender as the leader and may send an acknowledgment back. The leader waits until it receives acknowledgments from all processes or until it has confirmation that all processes have received the COORDINATOR message.

6. **Completion**: Once the COORDINATOR message has circulated the entire ring and returns to the leader, the election process is considered complete.

The Ring Algorithm has the following characteristics:
- **Termination**: The algorithm ensures that an election will always complete with the selection of a new leader.
- **Accuracy**: The elected leader is the process with the highest process ID that participated in the election.
- **Fault Tolerance**: The algorithm can tolerate failures, provided that the ring can be repaired (e.g., by skipping over failed processes) and that there is at least one process functioning correctly.

The Ring Algorithm can be slow, as the time to elect a leader is proportional to the number of processes in the ring, and it can be disrupted by process failures or message loss. It also requires that the ring topology be maintained, which can be a challenge in dynamic systems where processes can join or leave at any time.