# Entanglement  
*From Sean Carroll's "Quantum and Fields"*

---

## **Key Concepts**

### 1. **Particle Decay and Momentum**
In quantum mechanics, particle decay is described by the wavefunction:

$$|\psi(t)\rangle = \alpha(t) |\text{undecayed}\rangle + \beta(t) |\text{decayed}\rangle$$

Here, $\alpha(t)$ represents the amplitude for the particle to remain undecayed, and $\beta(t)$ represents the amplitude for the particle to decay. The normalization condition ensures:
$$
|\alpha(t)|^2 + |\beta(t)|^2 = 1
$$

Over time, the probability of the particle remaining undecayed decreases, and the probability of decay increases. The survival probability at time $t$ is $P_{\text{undecayed}}(t) = |\alpha(t)|^2$, and the probability of the particle decaying is $P_{\text{decayed}}(t) = 1 - |\alpha(t)|^2$.

**Momentum conservation** plays a crucial role in particle decay. The total momentum before and after decay remains the same:
$$
\vec{p}_{\text{original}} = \vec{p}_{1} + \vec{p}_{2}
$$
where $\vec{p}_{\text{original}}$ is the momentum of the original particle, and $\vec{p}_{1}$ and $\vec{p}_{2}$ are the momenta of the decay products. This allows us to calculate the momentum of one decay product without directly observing it:
$$
\vec{p}_{2} = \vec{p}_{\text{original}} - \vec{p}_{1}
$$

**Example: Decaying Boson**  
Consider a stationary boson that decays into an electron-positron pair. Since the original boson has no initial momentum ($\vec{p}_{\text{original}} = 0$), the momentum of the electron and positron must be equal and opposite to conserve momentum:
$$
\vec{p}_{\text{positron}} = -\vec{p}_{\text{electron}}
$$
If we know the position of the original boson before decay, we can measure the momentum of one of the decay products (e.g., the positron) and use momentum conservation to determine the momentum of the other particle, even without directly measuring it. This is useful in particle physics experiments, where some particles (like neutrinos) are hard to detect directly. By measuring other decay products, we can infer properties of the undetected particles.

---

### 2. **Entanglement: One State, Many Parts**
Entanglement describes a quantum phenomenon where the states of two or more particles become deeply interconnected. Unlike classical systems, where particles are independent, entangled particles share a combined quantum state. This means that measuring one particle’s state instantly determines the state of the other, no matter the distance between them.

The entangled state is typically written as:
$$
|\psi\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_1 |\downarrow\rangle_2 - |\downarrow\rangle_1 |\uparrow\rangle_2 \right)
$$
Here, $|\uparrow\rangle_1$ and $|\downarrow\rangle_2$ represent the spin states of two entangled particles. Measuring the spin of one particle gives immediate knowledge of the spin of the other.

Building on the previous example of particle decay, we see how momentum conservation connects the decay products. Similarly, entangled particles are not independent; they are connected in such a way that measuring one particle gives us information about the other, even if they are far apart.

In quantum mechanics, entanglement goes beyond momentum conservation. It links the properties of particles in a non-local way, forming a single quantum system that cannot be separated into individual parts. This phenomenon is fundamental to quantum technologies like quantum cryptography and quantum teleportation, which exploit these correlations to achieve tasks impossible with classical systems.


---

### 3. **Spooky Action at a Distance and the EPR Puzzle**
The term "spooky action at a distance" was coined by Einstein to criticize the non-local nature of quantum entanglement. It describes how entangled particles exhibit correlations that seem to violate the principle of locality, which states that objects are only directly influenced by their immediate surroundings.
  
**Key Features**

- Entangled particles, even when separated by vast distances, are correlated in such a way that measuring one particle’s state (e.g., its spin or polarization) immediately determines the state of the other. This happens instantaneously, seemingly defying the constraints of space and time.
- Importantly, this "spooky action" does not allow faster-than-light communication, thus preserving causality in quantum mechanics. While the information is transmitted instantaneously, it cannot be used to send information faster than light, which prevents paradoxes.  
    - For example, if Bob and Alice have an entangled pair and travel great distances from each other, when Bob measures his particle, he will immediately know the state of Alice’s particle. However, Alice, unaware of Bob's measurement, still has the same odds of measurement outcomes as if Bob never measured his particle. The act of measuring Bob's particle doesn't change the fact that Alice's measurement will still have a probabilistic outcome based on her own measurements. Making the instantaneous information useless for communication between observers.


**The EPR Puzzle**

Proposed by Einstein, Podolsky, and Rosen (EPR) in 1935, the EPR thought experiment challenged the completeness of quantum mechanics. EPR argued that if quantum mechanics were complete, it would have to explain physical reality through either:

  1. **Local Realism**: Particles have pre-existing properties (hidden variables) that determine their behavior before measurement.
  2. **Non-Locality**: The measurement of one particle instantaneously affects the state of another, regardless of the distance between them.

EPR believed that **non-locality** was problematic because it implies that quantum mechanics allows for instantaneous influences between distant particles, which violates classical ideas of locality and causality. This made quantum mechanics seem incomplete because it relied on non-local effects without offering a fully deterministic explanation.

Quantum mechanics rejects **local realism** and embraces **non-locality** through entanglement, where the state of entangled particles is not determined until one is measured, and the measurement of one affects the state of the other instantly.
  
The EPR paradox led to experiments testing **Bell's Theorem**, which showed that quantum mechanics’ predictions cannot be reproduced by any theory based on local hidden variables, confirming that non-locality is an intrinsic feature of quantum mechanics.

---

### 4. **Decoherence: The Quantum-Classical Divide**
Decoherence explains how a quantum system appears to transition into classical behavior due to interactions with its environment, including measurement apparatus and surroundings.

**Key Concepts:**

- **Interaction with the Environment**: Decoherence occurs when a quantum system interacts with its environment, such as measurement devices, air molecules, or photons. These interactions cause the quantum system to become **entangled** with the environment, making the superpositions of quantum states effectively unobservable.
- **Entanglement with the Measurement Apparatus**: In quantum mechanics, when a measurement is made, the quantum system becomes entangled with the measuring device. This means that the state of the system and the state of the apparatus are linked. The act of measurement doesn't just collapse the system's state but causes both the system and the apparatus to evolve into a combined state.
- **Loss of Superposition**: As the quantum system entangles with the environment or measuring device, its superposition states (e.g., being in two places at once) effectively disappear. The system appears to collapse into one definite classical state as the environment "measures" it.
- **No Wavefunction Collapse**: Decoherence does not imply a traditional wavefunction collapse. Instead, it explains why certain outcomes appear classical: the system is entangled with the environment in such a way that it no longer displays quantum superposition in a measurable way.

**Implications:**

- **Quantum to Classical Transition**: Decoherence helps explain why macroscopic systems behave classically. When a quantum system interacts with a large environment, it loses its quantum coherence and behaves as a classical system, even though the underlying dynamics remain quantum.
- **Measurement Problem**: Decoherence helps solve the measurement problem by showing how measurement interactions between the system and the apparatus lead to classical outcomes. The entanglement between the system and measurement apparatus prevents the superposition from being observed in practice.
- **Quantum Computing**: In quantum computing, decoherence is a significant challenge. Qubits are highly susceptible to decoherence from environmental interactions, which limits the time during which quantum information can be preserved. Reducing decoherence is critical for reliable quantum computing.


---

### 5. Foundations of Quantum Mechanics

The foundations of quantum mechanics explore principles, interpretations, and unresolved questions at the core of the theory. Below are common theories:

1. **Copenhagen Interpretation**  
   Quantum systems are described by a wavefunction that collapses upon measurement. Measurement defines reality, but the collapse mechanism remains unexplained.

2. **Many-Worlds Interpretation**  
   All possible outcomes occur in separate, branching universes. There is no wavefunction collapse, and the universe evolves deterministically.

3. **Pilot-Wave Theory (Bohmian Mechanics)**  
   Particles follow definite trajectories guided by a "pilot wave." This restores determinism but introduces non-local interactions.

4. **Quantum Bayesianism (QBism)**  
   The wavefunction represents an observer’s subjective knowledge. Measurement outcomes are probabilistic, avoiding objective collapse.

5. **Relational Quantum Mechanics**  
   Properties of a quantum system exist only relative to an observer or another system. Reality is observer-dependent, avoiding universal collapse.

6. **Objective Collapse Theories**  
   Wavefunction collapse is a real, physical process independent of observation. Examples include GRW theory, which aims to bridge quantum and classical behavior.

Each interpretation addresses the role of measurement, the nature of reality, and the origins of randomness, highlighting the ongoing debate in quantum mechanics.

## Takeaways

1. **Wavefunctions and Probabilities**  
   Quantum states are represented by wavefunctions, with probabilities derived from their squared amplitudes. Particle decay exemplifies how these probabilities evolve over time.

2. **Momentum Conservation in Quantum Systems**  
   Momentum conservation in particle decay allows properties of unobserved decay products to be inferred from observed ones, a crucial principle in particle physics.

3. **Entanglement and Non-Locality**  
   Entangled particles share a combined quantum state, meaning the measurement of one instantly determines the state of the other, regardless of distance. This underpins phenomena like "spooky action at a distance."

4. **The EPR Puzzle and Bell’s Theorem**  
   The EPR paradox challenges quantum mechanics with concepts like local realism, but Bell’s Theorem confirms quantum mechanics’ intrinsic non-locality, ruling out local hidden variable theories.

5. **Decoherence and the Quantum-Classical Divide**  
   Decoherence explains how quantum systems lose their coherence through interaction with the environment, transitioning to classical-like behavior without requiring wavefunction collapse.

6. **Interpretations of Quantum Mechanics**  
   Competing interpretations—such as Copenhagen, Many-Worlds, and Pilot-Wave—offer differing perspectives on measurement, reality, and randomness, reflecting the unresolved nature of quantum foundations.




# Resources
1. [Quanta and Fields by Sean Carroll](https://www.amazon.com/Quanta-Fields-Biggest-Ideas-Universe/dp/0593186605)

---

<div style="display: flex; justify-content: space-between;">
  <a href="../measurement"><- Measurement</a>
  <a href="../fields">Fields -></a>
</div>
