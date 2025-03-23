# Cache-Aware Matrix Multiplication & GPU Performance Analysis

This document explains a set of homework problems that analyze matrix multiplication performance in two scenarios: one on a CPU with a cache and one on a GPU. It includes both the problem statements and detailed reasoning behind each answer.

## Overview

The homework explores:

- **CPU-side matrix multiplication** with memory and cache constraints.
- **GPU-based matrix multiplication** with thread and cache considerations.

The problems examine how data layout, cache locality, and architectural parameters affect performance.

## Part I: CPU – Matrix Multiplication with Cache

```
You experiment with a computer having a one-level data cache (128 Bytes) and a main memory 
(1K Bytes). You exclusively focus on data accesses instead of instruction access. The latencies (in 
CPU cycles) of the different kinds of accesses are as follows:  
Cache hit: 1 cycle; Cache miss: 110 cycles; Main memory access with cache disabled: 80 cycles; 
Now, considering the following matrix multiplication C=A×B, please answer the following questions 
(please show detailed steps)
```

### System Specifications

- **Cache:** One-level data cache with 128 Bytes.
- **Main Memory:** 1K Bytes.
- **Focus:** Data accesses (instruction accesses are ignored).
- **Access Latencies:**
  - Cache hit: **1 cycle**
  - Cache miss: **110 cycles**
  - Main memory access (with cache disabled): **80 cycles**

### Matrix Multiplication Problem

Given matrices:

**Matrix A:**

$$
A = \begin{bmatrix}
x_{0,0} & x_{0,1} & \cdots & x_{0,l} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m,0} & x_{m,1} & \cdots & x_{m,l}
\end{bmatrix}
$$

**Matrix B:**

$$
B = \begin{bmatrix}
y_{0,0} & y_{0,1} & \cdots & y_{0,n} \\
\vdots & \vdots & \ddots & \vdots \\
y_{l,0} & y_{l,1} & \cdots & y_{l,n}
\end{bmatrix}
$$

The product is given by:

$$
C = A \times B.
$$

### Questions and Explanations

#### Q1. What is the dimension of the matrix \( C \)?

- **Explanation:**  
  Since \( A \) is \((m+1) \times (l+1)\) and \( B \) is \((l+1) \times (n+1)\), the resulting matrix \( C \) has dimensions:
  \( (m+1) \times (n+1) \).

---

#### Q2. Memory Constraints & Maximum \( l \)

```
Raw question: For multiplication using ALU, assume you pre-load both A and B into the main memory 
from the storage and reserve space for C in the main memory to speed up the performance. 
If pre-loading A and B takes 50% of the main memory space and reserved space for C takes 12.5% of 
the main memory. All elements in A, B, and C have the same bitwidth. Assuming we know the 
value of m and (m+n) is a constant, then what is the maximum value of l?
Answer: l = 2(m+1) - 1 = 2m + 1.
```

- **Problem Setup:** 
    - Pre-loading \( A \) and \( B \) into main memory uses **50%** of the memory.
    - Reserving space for \( C \) uses **12.5%** of the memory.
    - All elements in \( A \), \( B \), and \( C \) have the same bitwidth.
    - Assume \( m+n \) is constant.
  
- **Explanation:**

  Since pre-loading A and B uses 50% of the memory while reserving space for \( C \) uses 12.5%, the ratio of memory allocated for (A+B) to \( C \) is 50:12.5, or 4:1. This means the total number of elements in A and B is four times the number of elements in \( C \). Given that every element has the same size:

  - Matrix A has \((m+1)(l+1)\) elements.
  - Matrix B has \((l+1)(n+1)\) elements.
  - Matrix \( C \) has \((m+1)(n+1)\) elements.

  So, the relationship becomes:

  $$
  (m+1)(l+1) + (l+1)(n+1) = 4\,(m+1)(n+1).
  $$

  Notice that both terms on the left share the factor \((l+1)\), so we can factor it out:

  $$
  (l+1)\Big[(m+1) + (n+1)\Big] = (l+1)(m+n+2).
  $$

  Using a calculator to solve for \( l+1 \), we get:

  $$
  l+1 = \frac{4\,(m+1)(n+1)}{m+n+2}.
  $$

  Since we assume \( m+n \) is constant and we're looking to maximize \( l \), the product \((m+1)(n+1)\) is maximized when \( m = n \). Setting \( m = n \) simplifies the expression (because \( m+n+2 \) becomes \( 2(m+1) \)), and we eventually find that:

  $$
  l+1 = 2(m+1),
  $$
  which means:
  $$
  l = 2(m+1) - 1 = 2m+1.
  $$

---

#### Q3. Dimensions with 16-bit Integers

```
Raw question: Following the result from 2), If x is a 16-bit integer, what are the dimensions of A, B, and C?
Answer: (m=n=7; l=15)
```

**Explanation:**

- The problem states that 12.5% of the 1K bytes is reserved for matrix \( C \). Since each 16‑bit element is 2 bytes, \( C \) gets \(128 \div 2 = 64\) elements.
- If \( C \) is square (which is optimal when \( m \) and \( n \) are equal), then:
  
  $$
  (m+1)(n+1) = 64.
  $$
  
  The simplest square factorization is \(8 \times 8\), so \( m+1 = 8 \) and \( n+1 = 8 \), which gives \( m = n = 7 \).

- From Q2, we derived that \( l = 2(m+1) - 1 \). Plugging \( m = 7 \) into this gives:
  
  $$
  l = 2 \times 8 - 1 = 16 - 1 = 15.
  $$

Thus, we have:

- **m = n = 7**
- **l = 15**

This means:

- Matrix A is \(8 \times 16\),
- Matrix B is \(16 \times 8\),
- Matrix C is \(8 \times 8\).

---

#### Q4. Total Memory Access Time

```
Raw question: Following the result from 3), assume that the cache is a fully associative cache with 
the least recently used (LRU) replacement policy and the result can be directly written back to the main memory 
without sacrificing the memory read. What is the total memory access time (total cycles) for the matrix multiplication 
if we strictly follow the instructions below? Assume that we are using a 32B cache line.

for (int i=0; i<=m; i++)
{
    for (int j=0; j<=n; j++)
    {
         C(i,j) = A(i,:) * BT(:,j)
    }
}
Answer: Assume 32B cache line: 8×(1(A) + 8×8(B)) = 65×8 = 520 misses.
```

**Explanation:**

For our matrix multiplication (with \( m=7 \), so 8 rows):

- **Matrix A:**  
  Each row of \( A \) has 16 elements. Since each element is 2 bytes, one row occupies \( 16 \times 2 = 32 \) bytes, exactly one cache line.  
  → **Result:** Loading one row of \( A \) causes 1 cache miss per row.

- **Matrix B:**  
  In the inner loop, elements from \( B \) (or its transposed version) are accessed in a less contiguous manner.  
  For each row of \( C \), the multiplication requires accessing an 8×8 block from \( B \).  
  In the worst-case scenario, each element of this block might be in a different cache line, which would yield 64 cache misses per row.

- **Total for each row of \( C \):**  
  1 miss (for \( A \)) + 64 misses (for \( B \)) = 65 misses per row.

- With 8 rows, the total number of cache misses is:

  $$
  65 \text{ misses/row} \times 8 \text{ rows} = 520 \text{ misses}.
  $$

---

#### Q5. Leveraging Cache Locality

```
Raw question: How can you modify the approach to leverage the locality of the data in cache for improvement? 
How much can you improve with your method? (Use Tiling, transpose, or other techniques as long as you can show the improvement.)
```

**Explanation:**

**Technique:**  
  Use **tiling (blocking)** and/or **transpose** \( B \) to improve spatial and temporal locality.
  
**How it helps:**  

  - **Tiling/Blocking:**  
    Break the matrices into smaller sub-blocks that fit entirely in the cache. Once a sub-block is loaded, you can reuse the data multiple times for computations, significantly reducing cache misses.
  - **Transposing \( B \):**  
    This ensures that the memory accesses for \( B \) are more contiguous, further reducing the number of cache misses.

**Improvement:**  
  Depending on the chosen block size, such techniques can reduce cache misses by an order of magnitude, making the matrix multiplication much more efficient.

---

#### Q6. Average Memory Access Time (Random Access)

```
Raw question: After the computation, if we randomly access elements from A, B, and C continuously, what would the average memory access time (cycles per access) be?
(Hit rate = 128/(512+128) → 110×4/5 + 1/5 = 88.2 cycles)
```

**Explanation:**

- **Calculation of Hit Rate:**  
  The cache holds 128 Bytes out of a total of 512 + 128 = 640 Bytes that are being accessed.  
  So, the hit rate is \( 128/640 = 20\% \) and the miss rate is \( 80\% \).

- **Average Memory Access Time:**  
  With a hit taking 1 cycle and a miss taking 110 cycles, the average access time is:
  
  $$
  \text{Average} = 0.8 \times 110 + 0.2 \times 1 \approx 88.2 \text{ cycles}.
  $$

---

#### Q7. Conclusion on Cache Usefulness

```
Raw question: Based on the observation from Q6 and the memory access time given before, what can you conclude?
(88.2 > 80 → cache is useless if there is no locality)
```

**Explanation:** The average access time when randomly accessing memory (88.2 cycles) is higher than the 80 cycles required for a main memory access when the cache is disabled.

**Conclusion:** Without proper data locality, the cache not only fails to provide benefits but may actually hurt performance. This shows that effective use of the cache (via locality improvements) is critical for performance gains.

---

## Part 2: GPU Matrix Multiplication

In this section, we analyze matrix multiplication on a GPU. The problem assumes that all elements in matrices A, B, and C are 2-byte values. We use the following GPU characteristics to answer the questions:

- **Element Bitwidth:** 2 Bytes.
- **GPU Specifications:**

    - 2 Stream Multiprocessors (SM).
    - Each SM has 2 warp schedulers.
    - Each warp scheduler manages 4 warps.
    - Each warp contains 32 threads.

### Questions and Explanations

#### Q1. Thread Requirement

```
Raw question: If you use one thread to compute each element in the matrix C, how many threads should you request in your program code?
Answer: (m+1)(n+1)
```

**Explanation:**  
Since each element of C is computed by a single thread, the total number of threads equals the number of elements in C, which is \((m+1)(n+1)\).

---

#### Q2. Maximizing GPU Resource Utilization

```
Raw question: Assume that the GPU has 2 Stream Multiprocessors (SM), each SM has 2 warp schedulers, each warp scheduler is in charge of 4 warps, and each warp contains 32 threads. What are the possible dimensions of C that can maximize GPU resource utilization? Please provide at least four different dimensions.
Answer (professor’s interpretation): 2 × 2 × 32 = 128 → (i.e. 128×... threads)
```

**Explanation:**

Even though the GPU specifications mention that each warp scheduler manages 4 warps, in practice only one warp per scheduler is active at any given cycle. This means that each warp scheduler effectively handles only 32 threads concurrently.

Thus, the total number of threads that can be scheduled at the same time is:

$$
2 \text{ SMs} \times 2 \text{ warp schedulers per SM} \times 32 \text{ threads per scheduler} = 128 \text{ threads.}
$$

To maximize GPU utilization, the total number of threads (i.e., the total elements in matrix C) should be a multiple of 128. For example, dimensions of C such that \((m+1)(n+1)\) equals 128, 256, 384, etc., would be optimal.

---
#### Q3. Minimum Dimension for Square Matrix \( C \)

```
Raw question: Following the settings in Q2, if m = n, what is the minimum dimension of C?
Answer: (m+1)(n+1) = 256 → m = n = 15.
```

**Explanation:**  
For a square matrix \( C \), the total number of elements is given by \((m+1)^2\) (since there are \(m+1\) rows and \(m+1\) columns). To align with a convenient GPU thread count, we want the number of elements to be 256. Setting up the equation:

$$
(m+1)^2 = 256,
$$

we take the square root of both sides to obtain:

$$
m+1 = 16.
$$

This immediately gives:

$$
m = 15.
$$

Since \( m = n \) for a square matrix, we also have \( n = 15 \). Thus, matrix \( C \) is \( 16 \times 16 \) (since \(m+1 = 16\) and \(n+1 = 16\)), which provides exactly 256 elements, matching the desired GPU thread count.

---

#### Q4. Minimum L1 Cache Size per SM

```
Raw question: Following the result from Q3, assume that each SM has its own L1 and L2 caches and the L2 cache is large enough to preload all necessary data. Let’s further assume that m = n = l. If each L1 cache only allows up to 80% of its space for data buffering, what is the minimum size of L1 that can accommodate all necessary data for each warp operation without causing any runtime L1 cache miss? (Hint: Consider both inputs and outputs.)
Answer: 960 Bytes.
```

**Explanation:**

For each warp operation, the algorithm must have the necessary data buffered in the cache. Here’s how we determine the numbers:

1. **Matrix C:**  
   A warp consists of 32 threads, and each thread computes one output element of matrix \( C \). To support both reading and writing (or double-buffering) for \( C \), we need space for:
   $$
   2 \times 32 = 64 \text{ elements}.
   $$

2. **Matrix A:**  
   Similarly, each thread uses one element from matrix \( A \) as an input. Doubling this for buffering gives:
   $$
   2 \times 32 = 64 \text{ elements}.
   $$

3. **Matrix B:**  
   The tiling strategy for matrix \( B \) requires a block of data sized \( 16 \times 16 \) (from the square matrix assumption when \( m = n = l \)), which equals:
   $$
   256 \text{ elements}.
   $$

Adding these together, the total number of elements that must be buffered for one warp operation is:

$$
64 \text{ (for \( C \))} + 64 \text{ (for \( A \))} + 256 \text{ (for \( B \))} = 384 \text{ elements}.
$$

Since each element is 2 bytes, the total data size is:
$$
384 \times 2 = 768 \text{ bytes}.
$$

However, only 80% of the L1 cache is available for data buffering. To ensure that 768 bytes fit into just 80% of the cache, we need the L1 cache to be at least:
$$
\frac{768 \text{ bytes}}{0.8} = 960 \text{ bytes}.
$$

Thus, the minimum L1 cache size required for each warp operation is 960 bytes.


---

#### Q5. Delay Due to Compulsory Cache Misses

```
Raw question: Following the result from Q4, assume the cache has four ports that can concurrently support four data transfers between L2 and L1. The cache line is 32B and an L1 cache miss takes 20 cycles. What is the delay of compulsory misses for the matrix multiplication C = A×B?
Answer: For (m+1)(n+1) = 256, the compulsory miss with a single port is estimated as:
16×16 (matrix dimension) × (2B/32B) × (1 (for B) + ½ (for A) + ½ (for C)) × 20 cycles = 640 cycles. With four ports, the delay is 640/4 = 160 cycles.
```
**Explanation:**

1. **Matrix Dimension:**  
   With \((m+1)(n+1)=256\), matrix \(C\) is \(16 \times 16\).

2. **Cache Line Usage:**  
   Each element is 2 bytes and each cache line is 32 bytes, so one cache line holds \(32/2=16\) elements.  
   Therefore, the fraction of a cache line used per element is \(\frac{2 \text{ B}}{32 \text{ B}}\).

3. **Weighted Data Requirements:**  

    For matrix \(B\), every element is loaded fresh (weight 1).  
    
    For matrices \(A\) and \(C\), only about half of the required data is loaded on a compulsory miss (weight \(1/2\) each).  
    Thus, the combined weight is:  

    $$
    1 \;(\text{for } B) + \frac{1}{2} \;(\text{for } A) + \frac{1}{2} \;(\text{for } C) = 2.
    $$

4. **Calculating Misses:**  
   Multiply the total number of elements in \(C\) (which is \(16 \times 16\)) by the fraction of a cache line per element and then by the weight:
   $$
   16 \times 16 \times \left(\frac{2 \text{ B}}{32 \text{ B}}\right) \times 2.
   $$
   Here, \(16 \times 16 = 256\) elements, and \(\frac{2}{32} = \frac{1}{16}\), so:
   $$
   256 \times \frac{1}{16} \times 2 = 16 \times 2 = 32 \text{ cache line misses}.
   $$

5. **Cycle Delay:**  
   Each cache miss costs 20 cycles, so with one port, the delay is:
   $$
   32 \times 20 = 640 \text{ cycles}.
   $$

6. **Parallel Cache Ports:**  
   With 4 cache ports working concurrently, the delay is divided by 4:
   $$
   \frac{640}{4} = 160 \text{ cycles}.
   $$

Thus, the delay due to compulsory cache misses is 160 cycles.


---