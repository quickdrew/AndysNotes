# AI Hardware and Programming
## Instructor

Notes are mainy derived from **Dr. Chen Pan's** Hardware and programming course at **UTSA**.

- Instructor Email: chen.pan@utsa.edu


## Overview

- Understanding microarchitecture of various AI hardware, parallel computing, and deep learning
- Low level (C\C++) programming for executing AI algorithms
- Bridge the gap between hardware and software in AI.

## Computational Limits in AI

AI differs from traditional sequential code in that it relies heavily on **parallelism** and processing large datasets, making operations like matrix multiplication central to tasks like training and inference. While sequential code (found in most classical microcontrollers/microcomputers) executes one instruction at a time, AI performs millions of computations simultaneously, requiring hardware like GPUs or TPUs for efficient parallel processing. AI also demands high memory bandwidth, low latency, and specialized accelerators to handle its computational intensity, exceeding the capabilities of traditional architectures designed for sequential tasks.

### The Von Neumann bottleneck

The **Von Neumann architecture** is a foundational computing model that organizes a computer into three main components: a **CPU (central processing unit)**, **memory** (for storing data and instructions), and **I/O devices**. It operates by fetching instructions from memory, decoding them, and executing them sequentially, which is known as the **fetch-decode-execute cycle**. While the Von Neumann architecture underpins most general-purpose computers, its inherent bottleneck—limited bandwidth between the CPU and memory (the "Von Neumann bottleneck")—poses challenges for AI workloads, which often require high-speed processing of massive datasets. To address this, specialized AI hardware, such as GPUs, TPUs, and neuromorphic chips, is designed to parallelize computations and overcome memory bottlenecks, enabling efficient training and inference for complex AI models. Thus, while AI builds on the principles of the Von Neumann architecture, it increasingly relies on adaptations and specialized architectures optimized for its unique demands.

![Von Neumann bottleneck](../assets/vonn.png)

### The Memory Performace Gap
The **memory performance gap** is the mismatch between CPU speed and slower memory access, creating a bottleneck for AI workloads that rely on fast data processing. AI hardware mitigates this with high-bandwidth memory (HBM), larger caches, and optimized architectures like GPUs and TPUs, which improve memory throughput and enable efficient parallel processing of large datasets.

![Memory Gap](../assets/memory_gap.png)
Source: [researchgate](https://www.researchgate.net/figure/Trend-of-processing-vs-memory-performance-on-time-Hardware-parallelism-eg-in-the_fig3_329400858)

### Memory-bound vs Compute-bound

**Memory-Bound** tasks are limited by the speed of data transfer between memory and the processor, causing the CPU or GPU to wait for data. Examples include fetching large datasets or model weights in AI.

**Compute-Bound** tasks are limited by the processor's computational power, with the CPU or GPU fully utilized for calculations. Examples include matrix multiplications in deep learning.

In AI, memory-bound tasks benefit from faster memory or bandwidth, while compute-bound tasks require more powerful processors or accelerators.


## Computational View of a DNN

![DNN](../assets/dnn.png)

### Its Just Matrix Math
In deep neural networks (DNN), matrix math is the foundation for propagating data through layers, as depicted in the diagram. Each layer starts with **input features** (\( \mathbf{x}_1, \mathbf{x}_2, \dots \)) that are combined with a **weight matrix** (\( \mathbf{W} \)) to compute **scores**:

\[
\mathbf{z} = \mathbf{W} \cdot \mathbf{x} + \mathbf{b}
\]

The scores are then passed through an **activation function** \( f(\cdot) \), such as the one shown in the diagram, to introduce non-linearity:

\[
\mathbf{y} = f(\mathbf{z})
\]

The result, \( \mathbf{y} \), represents the output of **hidden units** in each layer, which then serve as inputs to the next layer. This process is repeated across multiple layers, from the **first layer** (weights, scores, and activation functions) through the **hidden layers** to the final layer, which produces the **output units**.

Each hidden layer transforms its inputs into a new representation using the same sequence: weights, scores, activation functions, and outputs. These operations are computationally intensive but highly parallelizable, making GPUs and TPUs essential for efficiently handling the large-scale computations in deep learning.

### Training the DNN
Training is the process of learning the optimal weights and biases for a DNN. It involves:

1. **Forward Pass**: Input features are propagated through the network to compute predictions.
2. **Loss Calculation**: The error between predictions and targets is measured using a loss function.
3. **Backpropagation**: Gradients of the loss with respect to the weights are calculated.
4. **Weight Update**: Weights are adjusted using an optimizer (e.g., SGD) to minimize the error.

This process repeats over many iterations (epochs) until the model converges.

### Executing the DNN (Inference) 
Inference uses the trained weights to make predictions. It involves:

1. **Forward Pass Only**: Input features propagate through the network to compute outputs.
2. **Prediction**: The final output represents the model's decision.

Unlike training, inference is faster and less computationally intensive as it skips backpropagation and weight updates.

**Key Differences**

| **Aspect**       | **Training**                       | **Inference**                    |
|-------------------|-----------------------------------|----------------------------------|
| **Purpose**       | Learn weights.                   | Make predictions.                |
| **Operations**    | Forward pass + backpropagation.  | Forward pass only.               |
| **Resource Needs**| High (GPUs/TPUs).                | Low, optimized for speed.        |


---
## Computer Architecture

![architecture](../assets/computerarchitecture.jpg)

### Instruction Sets 

RISC (Reduced Instruction Set Computing) and CISC (Complex Instruction Set Computing) are two CPU architecture approaches that impact instruction execution, power efficiency, and complexity.

| Feature         | **RISC (Reduced Instruction Set Computing)** | **CISC (Complex Instruction Set Computing)** |
|---------------|----------------------------------|----------------------------------|
| **Instruction Set** | Small, fixed-length, simple | Large, variable-length, complex |
| **Execution**  | One or few cycles per instruction | Some instructions take multiple cycles |
| **Memory Access** | Load/Store model (separate memory instructions) | Memory operations embedded in instructions |
| **Code Size** | More instructions but simpler | Fewer instructions but more complex |
| **Pipelining** | Easier to implement | More difficult due to complex decoding |
| **Power Efficiency** | More efficient, ideal for mobile and embedded devices | Higher power consumption, used in desktops and servers |
| **Examples** | ARM, RISC-V, PowerPC | x86 (Intel, AMD), IBM System/360 |

---

### Flynn's Taxonomy

Flynn's Taxonomy classifies computer architectures based on **how instructions and data are processed**. It consists of four primary categories: **SISD, SIMD, MISD, and MIMD**.

![Flynn's Taxonomy](../assets/FlynnsTaxonomy.png)


| **Category** | **Description** | **Usage Examples** |
|-------------|----------------|--------------------|
| **SISD** (Single Instruction, Single Data) | Traditional sequential execution, one instruction operates on one data at a time. | Early CPUs, simple microcontrollers |
| **SIMD** (Single Instruction, Multiple Data) | One instruction applied to multiple data elements simultaneously. | GPUs, vector processors, AI deep learning |
| **MISD** (Multiple Instruction, Single Data) | Multiple instructions process the same data stream simultaneously. Rarely used. | Fault-tolerant computing (e.g., redundant military systems) |
| **MIMD** (Multiple Instruction, Multiple Data) | Multiple processors execute different instructions on different data streams. | Multi-core CPUs, distributed computing, cloud systems |


---

### **Old vs. Real Computer Architecture**

Computing architectures can be categorized into **old (theoretical) models** and **real (practical) implementations**. Old architectures define foundational principles, while real architectures build upon them with modern enhancements.

| **Architecture Type** | **Description** | **Examples** |
|---------------------|----------------|-------------|
| **Old Architectures** | Conceptual models shaping computing principles, often with limitations in speed and memory efficiency. | Von Neumann (shared memory for data/instructions), Harvard (separate memory paths), Stack-based (operations via stack), Accumulator-based (single register for operations) |
| **Real Architectures** | Practical implementations optimizing speed, parallelism, and efficiency for real-world applications. | RISC (ARM, RISC-V), CISC (x86), VLIW (Intel Itanium), Superscalar (modern x86, ARM Cortex), Multi-core (Intel Core, AMD Ryzen) |

Modern processors often blend **Von Neumann’s model with elements of Harvard architecture** to enhance performance. Superscalar and multi-core architectures leverage parallel execution for increased computing power, making them dominant in **general-purpose computing, AI acceleration, and cloud systems**.


## Memory


![memory hierarchy](../assets/Memory-Hierarchy.jpg)

---

### **Types of Memory in Computer Architecture**
Memory can be categorized into **primary, secondary, and virtual memory**, each serving different roles in a computer system.

**A. Primary Memory (Volatile)**

| **Memory Type** | **Description** | **Examples** |
|---------------|----------------|-------------|
| **Registers** | Small storage inside the CPU for immediate processing. | Program Counter (PC), Accumulator |
| **Cache Memory** | Stores frequently accessed data for faster CPU access. | L1, L2, L3 cache |
| **RAM (Random Access Memory)** | Stores currently running programs and data. | DDR4, DDR5 |

**B. Secondary Memory (Non-Volatile)**

| **Memory Type** | **Description** | **Examples** |
|---------------|----------------|-------------|
| **HDD (Hard Disk Drive)** | Magnetic storage with moving parts, slower but cheaper. | Traditional laptop HDDs |
| **SSD (Solid State Drive)** | Flash-based storage, much faster than HDDs. | NVMe SSD, SATA SSD |

**C. Virtual Memory**

| **Memory Type** | **Description** | **Examples** |
|---------------|----------------|-------------|
| **Swap Space** | Uses disk space as an extension of RAM. | Linux Swap, Windows Pagefile |
| **Paging** | Divides memory into fixed-size pages to manage virtual memory. | 4KB page size in OS |

---

### **Memory Access Methods**
| **Access Method** | **Description** | **Example** |
|-----------------|----------------|-------------|
| **Sequential Access** | Reads data in a linear order. | Magnetic tape storage |
| **Direct Access** | Jumps directly to memory locations. | Hard drives, SSDs |
| **Random Access** | Any memory cell can be accessed in constant time. | RAM, Cache |

---

### **Virtual Memory**

Virtual memory is a memory management technique that allows a computer to use **more memory than physically available** by utilizing disk storage as an extension of RAM. It provides an abstraction that enables programs to operate as if they have access to a **large, contiguous block of memory**, even if the physical RAM is limited.

**How Virtual Memory Works**

1. **Paging** – The operating system divides memory into fixed-sized **pages** (e.g., 4KB) and stores inactive pages on the disk.
2. **Page Table** – Keeps track of mappings between **virtual addresses** (used by programs) and **physical addresses** (actual RAM locations).
3. **Page Faults** – When a program accesses a page that is not in RAM, the OS retrieves it from disk, causing a **performance delay**.
4. **Swap Space** – A reserved portion of disk storage where the OS stores temporarily unused memory pages.

**Benefits of Virtual Memory**

| **Feature** | **Description** |
|------------|----------------|
| **Increases Available Memory** | Programs can use more memory than the installed RAM. |
| **Memory Isolation** | Each process operates in its own memory space, preventing crashes from affecting other processes. |
| **Efficient Multitasking** | Multiple programs can run without worrying about limited RAM. |
| **Simplifies Memory Management** | Programs don’t need to manage physical memory directly. |

**Virtual Memory vs. Physical Memory**

| **Aspect** | **Virtual Memory** | **Physical Memory (RAM)** |
|-----------|------------------|--------------------|
| **Location** | Simulated in disk storage | Actual hardware memory |
| **Speed** | Slower (depends on disk speed) | Fast (nanosecond-level access) |
| **Capacity** | Larger than RAM | Limited by installed hardware |
| **Usage** | Extends available memory | Stores active processes |

**Challenges of Virtual Memory**

- **Slower Performance** – Retrieving data from disk (swap space) is much slower than accessing RAM.
- **Thrashing** – If too many pages are swapped frequently, performance degrades significantly.
- **Disk Wear** – On SSDs, excessive swapping can reduce lifespan.

Virtual memory is a key component of **modern operating systems** (Windows, Linux, macOS) and is essential for running large applications with limited physical RAM.

---

### **Memory Management in Operating Systems**
Operating systems manage memory through:

1. **Paging:** Divides memory into pages, swapping in/out as needed.
2. **Segmentation:** Divides memory into segments (code, stack, heap).
3. **Virtual Memory:** Uses disk space to extend RAM.

---

