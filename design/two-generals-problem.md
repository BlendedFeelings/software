---
b: https://blendedfeelings.com/software/design/two-generals-problem.md
---

# Two Generals Problem 
is a classic thought experiment and problem in computer science related to distributed systems and the challenges of coordinating actions in the presence of communication failures. It is a fundamental result in the theory of distributed computing and is used to illustrate issues of reliability and consensus in a system where communication may fail.

### The Problem:

The Two Generals Problem is usually presented as a story involving two generals who are planning to attack a fortified city. The generals are located in separate camps on opposite sides of the city. In order to succeed, they must launch a coordinated attack at the same time. However, the only way for them to communicate is by sending messengers through the city, and there's a chance that any messenger sent could be captured, making the communication unreliable.

The problem is for the generals to agree on a time to attack the city. One general might send a messenger to the other general with a proposed time for the attack. If the messenger gets through, the second general must send an acknowledgment back. However, because there is no guarantee that any message will be received, there is no way to ensure that both generals have agreed on the same plan. Even if the acknowledgment is received, the first general cannot be sure that the second general knows that the acknowledgment has been received, and so on ad infinitum.

### Implications in Distributed Systems:

The Two Generals Problem illustrates the impossibility of achieving perfect agreement or consensus in the presence of unreliable communication. In distributed systems, this is a significant concern because computers in a network may need to reach consensus to proceed with operations, and messages can be lost or delayed due to network issues.

The problem demonstrates that there is no deterministic solution to achieve consensus with one hundred percent certainty when there is a possibility of message loss. This has led to the development of various consensus algorithms that aim to achieve a high degree of confidence in agreement, even if absolute certainty is not possible. Examples include Paxos, Raft, and Byzantine Fault Tolerance algorithms, which are designed to handle failures in a network and still reach a consensus among the majority of nodes.

The Two Generals Problem is also related to the Byzantine Generals Problem, which extends the issue to situations where actors in the system may be malicious or faulty, further complicating the consensus process.

In summary, the Two Generals Problem is a fundamental issue in distributed computing that highlights the difficulty of achieving consensus in the face of communication uncertainties. It has influenced the design of many distributed systems and consensus protocols.