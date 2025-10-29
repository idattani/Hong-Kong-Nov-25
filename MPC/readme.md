# Mulit-Party-Computation

## 1. The Concept
 **Multi-Party Computation (MPC)** is a cryptographic method that allows multiple parties to jointly compute a result using their private inputs — **without revealing those inputs** to each other.
In simpler terms, each participant contributes data, and they all get the output of a shared computation (like the average, total, or decision), but **no one learns anyone else’s data**.

**Example:**

Imagine several banks want to detect fraud patterns by analyzing combined data. Using MPC, they can compute on their combined datasets **without sharing customer information directly**.
## 2. How It Works
MPC relies on mathematical techniques that “split” each participant’s input into secret shares or encrypted pieces.
These shares are distributed among 2 nodes, and computations are done on these.
Because no single share reveals useful information, privacy is preserved throughout the process.

**Common approaches include:**

* Secret sharing: Each input is divided into random parts so that only when combined do they reveal the real value.

* Secure Computation : Computations happen directly on masked data on private nodes.

## 3. Why It Matters

MPC is a cornerstone of privacy-preserving computation — it allows organizations and individuals to collaborate securely.

**It’s used in areas like:**

* Finance: Joint fraud detection or benchmarking without exposing client data.

* Healthcare: Combined medical research while keeping patient data private.

* Voting systems: Ensuring fair results without revealing individual votes.

In essence, MPC enables trustless cooperation — letting data work together without data owners having to fully trust one another.

## 4. Demo 
Here is a link to a demo application which shows the concepts of MPC.

[ACCESS THE DEMO HERE](https://mpc-demo-409588645189.us-central1.run.app/)
