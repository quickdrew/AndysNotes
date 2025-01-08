
## Delays in Verilog
Propagation delays in Verilog simulate the time it takes for signals to propagate through circuits.

### Delayed Assignments
In **continuous assignments**, use `#delay` to specify how long it takes for the output to update after a change in the inputs.

```verilog
 assign #5 y = a & b;  // y updates 5 time units after a or b changes 
 ```

### Why Use Delays?

- **Timing Simulation:** Models real-world signal delays.
- **Accurate Behavior:** Ensures proper timing in combinational logic.

### Delays in Procedural Assignments

Delays can also be applied in **procedural blocks** like `always`:

```verilog
 always @ (a or b) begin
    #3 out = a & b;  // out updates 3 time units after input changes
end 
```

### Inertial vs. Transport Delays

- **Inertial Delay**: This is the default type of delay in Verilog. It filters out glitches, meaning only input pulses longer than the delay propagate to the output. 
  - **Example**: If `#5` is used, pulses shorter than 5 time units will be filtered.
  
  ```verilog
  assign #5 y = a & b;  // Inertial delay, y updates only if changes persist for 5 time units 
   ```

- **Transport Delay**: This models a physical delay without filtering any input pulses. Even if an input changes rapidly, the signal is propagated to the output after the delay.
  - **Example**: Use `transport` to force transport delay behavior.

  ```verilog
  assign #5 y = transport a & b;  // Transport delay, y updates exactly 5 time units after input change 
  ```

### Key Differences:

- **Inertial delay**: Mimics real-world circuits where short glitches are filtered.
- **Transport delay**: Models pure signal propagation without glitch filtering.


## Wait Statements

In Verilog, the `wait` statement is used to pause the execution of a block until a certain condition becomes true. Unlike an `always` or `@(posedge clk)` block that waits for specific events (like clock edges), the `wait` statement halts the execution until the specified condition is met. Primarily used with delays to simulate hardware restrictions.

### **Syntax:**
```verilog
wait (condition) begin
    // Code to execute after the condition is true
end
```

### Example:
```verilog
reg signal, result;

initial begin
    result = 0;
    signal = 0;
    #10 signal = 1;  // Signal changes after 10 time units
    wait (signal == 1) begin
        result = 1;   // Result is updated after signal becomes high
    end
end
```