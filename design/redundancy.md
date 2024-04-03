---
b: https://blendedfeelings.com/software/design/redundancy.md
---

# Redundancy 
refers to the inclusion of additional components, systems, or functionalities that are not strictly necessary for the primary operation of the software but are included to provide a backup in case of failure. The main goal of redundancy is to increase reliability, availability, and fault tolerance. There are several types of redundancy in software design:

1. **Hardware Redundancy**: Involves using multiple hardware components that perform the same function. If one component fails, another can take over, ensuring that the system continues to operate. Examples include RAID setups in storage, dual power supplies, and server clusters.

2. **Software Redundancy**: This includes having multiple instances of software components running in parallel. This can be achieved through load balancing, where incoming requests are distributed across multiple servers, or through active-active or active-passive setups where one system is always on standby.

3. **Data Redundancy**: Ensures that data is not lost in case of a failure. This can be implemented through techniques such as database replication, where data is copied to multiple databases, or through regular backups.

4. **Time Redundancy**: Involves repeating a task or computation to ensure its correctness. This is often used in safety-critical systems where it's imperative to have correct data, such as in avionics or medical devices.

5. **Information Redundancy**: Involves adding extra data to messages to detect or correct errors. This is commonly used in communication systems through error detection and correction codes, such as parity bits, checksums, and more sophisticated coding schemes.

6. **Geographical Redundancy**: Distributing data centers or servers across different geographic locations to protect against regional failures due to natural disasters, power outages, or other location-specific issues.

7. **Component Redundancy**: Using multiple interchangeable components within the software architecture. If one component fails, another can replace it without affecting the system's functionality.

The implementation of redundancy must be carefully planned, as it can lead to increased complexity and cost. It's important to conduct a cost-benefit analysis to determine the appropriate level of redundancy for a given system based on the criticality of the application and the acceptable level of risk.