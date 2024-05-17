---
b: https://blendedfeelings.com/software/gossip-protocol/gossip-protocol.md
---

# Gossip protocols 
also known as epidemic protocols, are a family of protocols used for distributed systems to ensure that information is quickly and efficiently disseminated among nodes in a network. The term "gossip" is used because the way information spreads in these protocols is similar to how gossip spreads among people—rapidly and in multiple directions. These protocols are particularly useful in large-scale, peer-to-peer, and distributed computing environments where traditional broadcast methods are not scalable or efficient.

Here are some key points about gossip protocols:

- **Decentralisation**: Gossip protocols do not rely on a centralised control structure. Each node in the network independently executes the protocol.

- **Robustness**: They are robust against node failures because the protocols do not depend on any single node to disseminate information.

- **Scalability**: Gossip protocols can handle changes in the network size and topology without requiring significant changes to the protocol or the need for central coordination.

- **Efficiency**: Information spreads quickly through the network, often in a logarithmic or sub-linear relation to the number of nodes in the system.

- **Redundancy**: The protocols often involve sending messages to multiple nodes, which ensures redundancy and a high probability that all nodes will receive the information even if some messages are lost.

The basic operation of a gossip protocol involves the following steps:

1. A node randomly selects one or more peers from its list of known nodes in the network.
2. The node shares the information (which could be a data update, a new piece of information, etc.) with the selected peers.
3. The peers that receive the information then select other peers to share the information with, and the process continues until the information has spread to all or most nodes in the network.

There are different variations of gossip protocols, each tailored for specific scenarios and with different properties regarding message redundancy, convergence speed, and network traffic. Some common types include:

- **Push Gossip**: Where nodes actively send information to other nodes.
- **Pull Gossip**: Where nodes actively request information from other nodes.
- **Push-Pull Gossip**: A combination of push and pull, where nodes both send information and request information from others.

Gossip protocols are used in various applications, including distributed databases, peer-to-peer networks, failure detection, and consensus algorithms. They are particularly well-suited for environments where network topology changes frequently, or where it's challenging to maintain a complete and accurate list of all nodes in the network.