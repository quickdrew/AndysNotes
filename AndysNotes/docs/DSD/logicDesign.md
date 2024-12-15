
## Boolean Algebra
| Rule                             | Expression                          | Hint                                                                                          |
|-----------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Identity Law                      | A + 0 = A                           | No change when OR'ed with 0                                                                   |
| Identity Law                      | A • 1 = A                           | No change when AND'ed with 1                                                                  |
| Null Law                          | A + 1 = 1                           | OR'ing with 1 results in 1                                                                    |
| Null Law                          | A • 0 = 0                           | AND'ing with 0 results in 0                                                                   |
| Complement Law                    | A + A' = 1                          | A variable OR'ed with its complement is 1                                                     |
| Complement Law                    | A • A' = 0                          | A variable AND'ed with its complement is 0                                                    |
| Idempotent Law                    | A + A = A                           | OR'ing a variable with itself leaves it unchanged                                             |
| Idempotent Law                    | A • A = A                           | AND'ing a variable with itself leaves it unchanged                                            |
| Domination Law                    | A + A'B = A + B                     | Apply the Distributive Law to simplify                                                        |
| Distributive Law                  | A(B + C) = AB + AC                  | Distributes AND over OR                                                                       |
| Distributive Law                  | A + BC = (A + B)(A + C)             | Distributes OR over AND                                                                       |
| Absorption Law                    | A + AB = A                          | Removes redundant terms                                                                      |
| Absorption Law                    | A(A + B) = A                        | Removes redundant terms                                                                      |
| Double Negation Law               | (A')' = A                           | Negation of a negation returns the original value                                             |
| De Morgan’s Law                   | (A • B)' = A' + B'                  | Apply to break AND terms when converting SOP to POS                                           |
| De Morgan’s Law                   | (A + B)' = A' • B'                  | Apply to break OR terms when converting POS to SOP                                            |
| Involution Law                    | (A'') = A                           | A variable twice negated is equal to itself                                                   |
| Consensus Theorem                 | AB + A'C + BC = AB + A'C            | Simplifies expressions by eliminating redundant terms                                         |
| Distributive (SOP to POS hint)    | A + BC = (A + B)(A + C)             | Useful for converting SOP to POS                                                             |
| Distributive (POS to SOP hint)    | A(B + C) = AB + AC                  | Useful for converting POS to SOP                                                             |
| Demorgans (SOP to POS hint)       | (A • B)' = A' + B'                  | Apply De Morgan’s Law during the conversion                                                   |
| Demorgans (POS to SOP hint)       | (A + B)' = A' • B'                  | Apply De Morgan’s Law during the conversion                                                   |
| Redundancy Law                    | AB + AB' = A                        | Removes redundant variables from the equation                                                 |


## Sequential and Combinational Assignments

- **Sequential = Procedural:** Sequential logic updates state based on clock edges and uses procedural assignments, typically with **non-blocking (`<=`) assignments**. It is modeled inside `always` blocks that are sensitive to clock edges (e.g., `posedge clk`). This describes systems like flip-flops or registers that rely on previous states.

  **Example:**
  ```verilog
  always @(posedge clk or posedge reset) begin
      if (reset)
          q <= 0;      // Asynchronous reset
      else
          q <= d;      // Update q with d at clock edge
  end
  ```

- **Combinational = Continuous:** Combinational logic depends purely on the current inputs and is described using **continuous (blocking) assignments**. It models circuits like AND, OR gates, where output is updated as soon as inputs change, without regard to clock cycles.

    **Example:**
    ```verilog
    assign y = a & b;  // Output y changes immediately based on a and b
    ```

### Relevant Constructs

- **`always` blocks:** Used to describe both sequential and combinational logic. For sequential logic, `always @(posedge clk)` or `always @(negedge clk)` is used, whereas for combinational logic, `always @(*)` is used to capture all input changes automatically.
    **Example:**
    ```verilog
    always @(*) begin
        result = a | b;  // Combinational logic triggered by any input change
    end
    ```

- **`initial` blocks:** Used to define initial conditions in simulations. They execute once at the start of the simulation and are commonly used for testbenches or initializing registers/variables in simulation but are not synthesized into hardware.
    **Example**
    ```verilog
    initial begin
        reg_x = 0;  // Initialize reg_x to 0 at simulation start
    end
    ```

### Key Points

- **Blocking (`=`) vs. Non-blocking (`<=`):** In sequential logic (`always @(posedge clk)`), use non-blocking assignments (`<=`) to ensure parallel updates. In combinational logic, blocking assignments (`=`) can be used to execute statements sequentially.
## State Machine
A state machine is a computational model used to design both software and hardware systems. It consists of a set of states, transitions between states, and actions that occur based on inputs.

### Components

1. **States**: Defined conditions or situations the system can be in.
2. **Transitions**: Conditions that trigger a change from one state to another.
3. **Inputs**: External events or conditions that affect state transitions.
4. **Outputs**: Actions or results produced during or after a state transition.

### Types of State Machines

1. **Finite State Machine (FSM)**: Has a finite number of states and transitions between them.
   - **Deterministic FSM (DFA)**: Every state has exactly one transition for each input.
   - **Non-deterministic FSM (NFA)**: A state can have multiple transitions for the same input.

2. **Mealy Machine**: The output depends on both the current state and the input.
3. **Moore Machine**: The output depends only on the current state.

### Applications

- **Control Systems**: Used in embedded systems for managing device behavior.
- **Protocols**: Helps in defining the sequence of operations in communication protocols.
- **Game Design**: To model different game states such as playing, paused, or game over.

### Example

```verilog 
module fsm_example (
    input wire clk,        // Clock input
    input wire reset,      // Asynchronous reset signal (active high)
    input wire trigger,    // Trigger input to transition between states
    output reg out         // Output signal that depends on the current state
);

    // Define the states as an enumerated type using a 2-bit register
    typedef enum reg [1:0] {
        IDLE   = 2'b00,    // State 0: Idle state (default)
        STATE1 = 2'b01,    // State 1: Represents the first active state
        STATE2 = 2'b10     // State 2: Represents the second active state
    } state_t;

    // Current state and next state registers
    reg state_t current_state, next_state;

    // Sequential logic for state transition
    // This block updates the current state on every clock edge or reset
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= IDLE;   // On reset, go to IDLE state
        end else begin
            current_state <= next_state;  // On clock, update to the next state
        end
    end

    // Combinational logic for state transition based on current state and input trigger
    always @(*) begin
        // Default next state and output values
        next_state = current_state; // Hold the current state by default
        out = 1'b0;                 // Default output is 0

        // State transition logic
        case (current_state)
            IDLE: begin
                // In IDLE, if 'trigger' is high, move to STATE1
                if (trigger)
                    next_state = STATE1;
                // Output remains 0 in IDLE
            end

            STATE1: begin
                // In STATE1, set output high
                out = 1'b1;
                // If 'trigger' is high, move to STATE2, otherwise go back to IDLE
                if (trigger)
                    next_state = STATE2;
                else
                    next_state = IDLE;
            end

            STATE2: begin
                // In STATE2, output remains high
                out = 1'b1;
                // If 'trigger' goes low, return to IDLE
                if (!trigger)
                    next_state = IDLE;
            end

            default: begin
                // Default case to handle any undefined state (shouldn't happen)
                next_state = IDLE; // Return to IDLE state if something goes wrong
            end
        endcase
    end

endmodule
```