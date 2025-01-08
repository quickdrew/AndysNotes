
## Data Types
| Data Type  | Purpose                                          | Characteristics                                         |
|------------|--------------------------------------------------|---------------------------------------------------------|
| `wire`     | Combinational logic and connections              | Cannot hold state, used in continuous assignments        |
| `reg`      | Sequential and combinational logic               | Holds state, used inside `always` blocks                 |
| `integer`  | Signed 32-bit value for loops/counters           | Used in loops and non-synthesizable code                 |
| `real`     | Floating-point value                             | Used in non-synthesizable, behavioral code               |
| `time`     | 64-bit value to represent simulation time        | Used for timing and measuring delays in simulation       |
| `tri`      | Tri-state buffer signal                          | Can take high-impedance (`Z`) values                     |

## Vectors in Verilog
Vectors in Verilog are used to represent multi-bit signals, which are crucial when dealing with buses, registers, or large numbers. They allow for grouping multiple bits into a single variable.

A vector is declared by specifying the range of bits using `[MSB:LSB]`, where MSB is the most significant bit and LSB is the least significant bit.
```verilog
wire [3:0] bus;   // 4-bit wide wire (vector)
reg  [7:0] data;  // 8-bit register
```
Individual bits or a range of bits within a vector can be accessed as follows:
```verilog
wire [7:0] data;
assign bit3 = data[3];     // Accessing the 3rd bit of data
assign lower_nibble = data[3:0];  // Accessing the lower 4 bits of data
```

You can assign values directly to vectors:
```verilog
reg [3:0] result;
result = 4'b1010;  // Assigning binary value
result = 4'hA;     // Assigning hexadecimal value
```

A vector can have zero width when the MSB and LSB are the same, meaning it's a single-bit signal:
```verilog
wire [0:0] single_bit;  // Equivalent to a scalar
```

By default, vectors are unsigned, but they can be declared as signed if needed:
```verilog
signed reg [7:0] signed_data;  // Signed 8-bit register
```

In signed vectors, the most significant bit (MSB) is treated as the sign bit.


## Primitives

A Verilog primitive is a pre-defined logic element used in digital designs. These include basic gates like `and`, `or`, `nand`, and `xor`, with fixed functions that don't require module definitions.

**Output Declaration:** In Verilog, when declaring a UDP, the output must always be listed first, followed by the input(s). This order is essential for the proper functioning of the UDP.

**Types of Primitives:**
- **Combinational Primitives:** e.g., `and`, `or`, `xor`
- **Sequential Primitives:** Flip-flops, latches

### User Defined Primitives (UDPs)

UDPs are custom-defined logic, either combinational or sequential, declared using the `primitive` keyword. They use a truth table to define behavior.

- **Example (Combinational UDP):**
    ```verilog
    
        primitive my_and (out, in1, in2);  
        output out;  
        input in1, in2;  

        // The 'table' defines the behavior of this custom primitive.
        // Each row in the table specifies input combinations and the corresponding output.
        // For an AND gate, the output is 1 only when both inputs are 1.
        table
            0 0 : 0;  // If both inputs are 0, the output is 0.
            1 1 : 1;  // If both inputs are 1, the output is 1.
            // For simplicity, intermediate input states (like 0 1 or 1 0) are not explicitly defined here,
            // but in a full AND gate implementation, these would typically output 0.
        endtable

        endprimitive  
    ```

## Verilog Operator Precedence

In Verilog, operators follow a specific order of precedence. This determines how expressions are evaluated when there are multiple operators in the same expression. Below is the list of operators in order of precedence, from highest to lowest:

1. **Unary operators**
   - `+`, `-` (unary plus and minus)
   - `!` (logical NOT)
   - `~` (bitwise NOT)
   - `&`, `~&` (reduction AND, NAND)
   - `|`, `~|` (reduction OR, NOR)
   - `^`, `~^`, `^~` (reduction XOR, XNOR)
  
2. **Multiplicative operators**
   - `*`, `/`, `%` (multiply, divide, modulus)

3. **Additive operators**
   - `+`, `-` (addition, subtraction)

4. [**Shift operators**](#shifts)
   - `<<`, `>>` (logical shift left, right)

5. **Relational operators**
   - `<`, `<=`, `>`, `>=` (less than, less than or equal, greater than, greater than or equal)

6. **Equality operators**
   - `==`, `!=` (logical equality, inequality)
   - `===`, `!==` (case equality, case inequality)

7. **Bitwise operators**
   - `&`, `|`, `^`, `^~`, `~^` (AND, OR, XOR, XNOR)

8. **Logical operators**
   - `&&` (logical AND)
   - `||` (logical OR)

9. **Conditional operator**
   - `? :` (ternary operator)

10. **Assignment operators**
    - `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `|=`, `^=` (assignment and compound assignments)


## Shifts

In Verilog, shift operations move bits of a value to the left or right. There are two types: **logical shifts** and **arithmetic shifts**.

### 1. Logical Shifts

Logical shifts move bits and fill the vacated positions with zeros.

**a. Logical Left Shift (`<<`)**
Shifts bits to the left by the specified amount, inserting zeros on the right. This is equivalent to multiplying by a power of 2.

**Syntax:**
```verilog
result = value << shift_amount;
```

**Example:**
```verilog
wire [3:0] value = 4'b1010; 
assign result = value << 1;  // Result: 0100
```

**b. Logical Right Shift (`>>`)**
Shifts bits to the right, inserting zeros on the left.

**Syntax:**
```verilog
result = value >> shift_amount;
```

**Example:**
```verilog
wire [3:0] value = 4'b1010;
assign result = value >> 1;  // Result: 0101
```

### 2. Arithmetic Shifts

Arithmetic shifts preserve the sign of signed numbers when shifting right.

**a. Arithmetic Right Shift (`>>>`)**
Shifts bits to the right, preserving the sign by filling the leftmost bits with the sign bit (MSB).

**Syntax:**
```verilog
result = value >>> shift_amount;
```

**Example:**
```verilog
wire signed [3:0] value = -4;  // Binary: 1100 (two's complement)
assign result = value >>> 1;   // Result: 1110
```

## Functions and Tasks

| **Aspect**                | **Functions**                                       | **Tasks**                                         |
|---------------------------|-----------------------------------------------------|---------------------------------------------------|
| **Return Type**            | Returns a **single value**.                         | Can return **multiple values** via `output` ports.|
| **Time Control**           | **No timing control** (`#`, `@`, `wait` not allowed).| **Supports timing control** (can use `#`, `@`, `wait`). |
| **Arguments**              | **Only `input` arguments**.                        | Can have `input`, `output`, and `inout` arguments. |
| **Usage**                  | Used in expressions directly.                      | Called as a separate statement.                   |
| **Execution Time**         | Executes in **zero simulation time**.               | Takes **simulation time** to execute.             |
| **Use Case**               | Simple, combinational calculations.                 | Complex tasks with delays or multiple outputs.     |

### Example Function:
```verilog
function [3:0] add;
  input [3:0] a, b;
  begin
    add = a + b;
  end
endfunction
```

### Example Task:
```verilog
task add_sub;
  input [3:0] a, b;
  output [3:0] sum, diff;
  begin
    sum = a + b;
    diff = a - b;
  end
endtask
```

### Example Task (With Event Control):
```verilog
task event_control_example;
  input [3:0] a, b;
  output reg [3:0] result;
  begin
    wait (a == b);   // Wait until a equals b
    result = a + b;  // Perform addition
  end
endtask
```

### Example Task (with `output` and `inout` Arguments Called as a Separate Statement):
```verilog
module task_example;
  reg [3:0] x, y, z, sum_result, diff_result;

  initial begin
    x = 4'b1010;              // Assign some values
    y = 4'b0110;
    z = 4'b0011;

    // Call the task as a separate statement
    arithmetic_operations(x, y, sum_result, z);  // `z` will be modified in-place as an inout
  end
endmodule

task arithmetic_operations;
  input [3:0] a, b;           // Input arguments
  output reg [3:0] sum;       // Output argument
  inout [3:0] diff;           // Inout argument
  begin
    sum = a + b;              // Perform addition
    diff = diff - a;          // Modify the inout value
  end
endtask
```