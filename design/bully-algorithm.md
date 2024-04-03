---
b: https://blendedfeelings.com/software/design/bully-algorithm.md
---

# Bully Algorithm 
is a method used to elect a coordinator or leader among distributed processes in a system where each process can uniquely identify itself with a number (its process ID). The process with the highest process ID number is selected as the leader. The algorithm is called "bully" because the process with the highest ID "bullies" its way to becoming the leader.

Here's how the Bully Algorithm works:

1. **Election Initiation**: When a process, say `P`, notices that the coordinator is not responding (indicating a failure), it initiates an election.

2. **Election Message**: `P` sends an ELECTION message to all processes with higher process IDs than its own.

3. **Waiting for Responses**:
   - If `P` receives no response from any process with a higher ID, it wins the election and becomes the coordinator.
   - If `P` receives an OK message from any process with a higher ID, it steps down and waits for one of these processes to announce itself as the coordinator.

4. **Taking Control**: If a process receives an ELECTION message from a lower-ID process, it sends an OK message back to the sender to indicate that a process with a higher ID is alive. It then takes over the election process by sending ELECTION messages to processes with higher IDs than its own unless it's the process with the highest ID.

5. **Coordinator Announcement**: Once the process with the highest ID takes control (either because it received no responses to its ELECTION message or because it's the one that started the election), it sends a COORDINATOR message to all processes to announce its leadership.

6. **Recovery from Failure**: If a process recovers from failure (or a new process joins with a higher ID than the current coordinator), it holds an election to assert its right to control if it has the highest ID.

The Bully Algorithm has the following characteristics:
- **Termination**: The algorithm guarantees that an election will complete and a new leader will be elected if the old leader fails.
- **Accuracy**: The elected leader is always the process with the highest process ID among the non-faulty processes.
- **Fault Tolerance**: The algorithm can tolerate failures up to the point where communication between processes is still possible.

However, the Bully Algorithm can be inefficient in systems with a large number of processes or frequent failures, as it involves sending a large number of messages. It also assumes that process IDs are unique and that the processes can reliably determine if other processes are up or down.