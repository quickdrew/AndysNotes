# CUDA C/C++ Programming Notes

## Overview

**What is CUDA?**  
CUDA is a parallel computing architecture developed by NVIDIA that allows developers to leverage GPU acceleration for general-purpose computing, not just graphics.

**Key points:**

- Exposes GPU parallelism for general-purpose computing while retaining high performance.
- Based on industry-standard C/C++ with a small set of extensions, like `Malloc() -> cudaMalloc()` and `Memcpy() -> cudaMemcpy()`
- Provides straightforward APIs to manage devices, memory, and kernels.
- Enables writing and launching CUDA kernels, managing GPU memory, and handling synchronization between the CPU (host) and GPU (device).

**Difference between host and device:**

- **Host:** CPU
- **Device:** GPU

**Using `__global__` to declare a function as device code:**

- Executes on the device (GPU)
- Called from the host (CPU)

---

## Heterogeneous Computing

### Host and Device relationship

- **Host:** The CPU and its associated memory; executes serial portions of code.
- **Device:** The GPU and its dedicated memory; executes parallel portions of code efficiently.

![](../assets/hetero.png)


### Simple Processing Flow

![](../assets/cuda_gif0.gif)

---

## Hello World

### Host (CPU) Example

A simple C program running entirely on the CPU:

```c
#include <stdio.h>

int main(void) {
    printf("Hello World!\n");
    return 0;
}
```

- Standard C code executed by the CPU.
- Compiled using a standard C compiler like `gcc`.
- Outputs `Hello World!` directly.


### CUDA Device (GPU) Example

A basic CUDA C program that launches a kernel (device function) on the GPU:

```c
#include <stdio.h>

// Device kernel (does nothing here)
__global__ void mykernel(void) {
}

int main(void) {
    // Launch kernel on the GPU
    mykernel<<<1, 1>>>();

    // Host code continues
    printf("Hello World!\n");
    return 0;
}
```

- `__global__` keyword specifies a CUDA kernel (runs on GPU, called from CPU).
- Triple angle brackets `<<< >>>` indicate kernel launch parameters (1 block, 1 thread).
- Requires NVIDIA's CUDA compiler (`nvcc`) to compile.
- Kernel launch does nothing visible here; real work happens inside device code.
- Still prints `Hello World!` from the CPU (host).

---


## Addition on the Device
A basic CUDA C program performing addition on the GPU:

```c
#include <stdio.h>

// Device kernel for addition
__global__ void add(int *a, int *b, int *c) {
    *c = *a + *b;
}

int main(void) {
    int a = 2, b = 7, c;
    int *d_a, *d_b, *d_c;

    // Allocate memory on GPU
    cudaMalloc((void **)&d_a, sizeof(int));
    cudaMalloc((void **)&d_b, sizeof(int));
    cudaMalloc((void **)&d_c, sizeof(int));

    // Copy values to GPU
    cudaMemcpy(d_a, &a, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, sizeof(int), cudaMemcpyHostToDevice);

    // Launch kernel on GPU
    add<<<1, 1>>>(d_a, d_b, d_c);

    // Copy result back to CPU
    cudaMemcpy(&c, d_c, sizeof(int), cudaMemcpyDeviceToHost);

    // Free GPU memory
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);

    printf("Sum: %d\n", c);
    return 0;
}
```

- `__global__` defines a kernel function to execute on the GPU.
- Uses CUDA-specific functions for memory management (`cudaMalloc`, `cudaMemcpy`, `cudaFree`).
- Kernel launch syntax (`<<<1, 1>>>`) specifies execution configuration: 1 block, 1 thread.
- Data must be explicitly transferred between host (CPU) and device (GPU).
- Compiled with NVIDIA's CUDA compiler (`nvcc`).

---


## Vector Addition on the Device

### Device Kernel

```c
__global__ void add(int *a, int *b, int *c) {
    c[blockIdx.x] = a[blockIdx.x] + b[blockIdx.x];
}
```

- Each block handles one element of the addition.
- Blocks run in parallel on the GPU.

**Example of Parallel Execution:**

- **Block 0:** `c[0] = a[0] + b[0];`
- **Block 1:** `c[1] = a[1] + b[1];`
- **Block 2:** `c[2] = a[2] + b[2];`
- **Block 3:** `c[3] = a[3] + b[3];`

### Host Code Example

```c
#define N 512

int main(void) {
    int *a, *b, *c; // host copies of a, b, c
    int *d_a, *d_b, *d_c; // device copies of a, b, c
    int size = N * sizeof(int);

    // Allocate space for device copies
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);

    // Allocate space for host copies and setup input values
    a = (int *)malloc(size); random_ints(a, N);
    b = (int *)malloc(size); random_ints(b, N);
    c = (int *)malloc(size);

    // Copy inputs to device
    cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

    // Launch add() kernel on GPU with N blocks
    add<<<N, 1>>>(d_a, d_b, d_c);

    // Copy result back to host
    cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);

    // Cleanup
    free(a); free(b); free(c);
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);

    return 0;
}
```

- Allocates and manages memory explicitly.
- Each GPU block computes one addition in parallel.
- Data transferred between host and GPU explicitly.

---


Below is a new section on **Indexing** that integrates the concepts covered on pages 37–48:

---

## Indexing

Efficient indexing is key to mapping threads to data elements in CUDA. In CUDA’s parallel programming model, each thread in a grid must be assigned a unique portion of the data. This section outlines the common strategies and formulas used for indexing in CUDA kernels.

### 1. Basic Indexing Concepts

CUDA organizes threads into blocks, and blocks form a grid. Each thread within a block is uniquely identified by `threadIdx`, while each block in the grid is identified by `blockIdx`.

![](../assets/thread0.png)

**Built-in Variables:**  

  - `threadIdx.x`: The thread’s index within its block (in the x-dimension).  
  - `blockIdx.x`: The block’s index within the grid (in the x-dimension).  
  - `blockDim.x`: The number of threads in a block (in the x-dimension). In the example above `blockDim.x = 8`

### 2. The Indexing Formula

When processing one-dimensional arrays, the unique global index for each thread is calculated using:
  
```c
int index = threadIdx.x + blockIdx.x * blockDim.x;
```

- **Explanation:**  
  - `threadIdx.x` gives the thread’s local position within its block.  
  - `blockIdx.x * blockDim.x` offsets the local index by the total number of threads in all preceding blocks.  
  - Together, they ensure each thread handles a unique element in the data array.

### 3. Practical Example

Consider a kernel launch where each block contains 8 threads. For a thread with:
  
- `threadIdx.x = 5`  
- `blockIdx.x = 2`  
- `M = blockDim.x = 8`
  
![](../assets/index.png)

This means that the thread processes the 22nd element (using zero-based indexing) of the array.

### 4. Multi-Dimensional Indexing

For higher-dimensional data, CUDA supports three-dimensional configurations:
  
**2D Indexing:**  
When working with images or matrices, you may compute a unique index using both x and y dimensions:
  
```c
int col = threadIdx.x + blockIdx.x * blockDim.x;
int row = threadIdx.y + blockIdx.y * blockDim.y;
int index = row * width + col; // 'width' is the number of columns
```
  
**3D Indexing:**  

For volume data, a similar approach extends to three dimensions using `threadIdx.z`, `blockIdx.z`, and `blockDim.z`.

### 5. Handling Arbitrary Vector Sizes

Often, the total number of data elements is not an exact multiple of the block size. To safely process all elements without accessing out-of-bound memory, include a bounds check in your kernel:

```c

__global__ void add(int *a, int *b, int *c, int n) {
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    if (index < n) {
        c[index] = a[index] + b[index];
    }
}
```

- **Kernel Launch:**  
  The number of blocks is computed to cover all elements:
  
```c
  add<<<(n + blockDim.x - 1) / blockDim.x, blockDim.x>>>(d_a, d_b, d_c, n);
```

### 6. Summary

- **Indexing in CUDA** is essential for correctly mapping threads to array elements.
- Use the formula `index = threadIdx.x + blockIdx.x * blockDim.x` for one-dimensional data.
- For multi-dimensional problems, extend the indexing strategy using corresponding dimensions.
- Always consider boundary conditions to prevent memory errors when the data size is not an exact multiple of the block size.

By mastering these indexing techniques, you can efficiently parallelize data processing across the GPU’s many threads.

---

This section brings together the key ideas discussed in the referenced pages and should serve as a practical guide for implementing effective indexing in CUDA applications.