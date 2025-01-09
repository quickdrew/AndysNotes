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
- Proposed by Einstein, Podolsky, and Rosen (EPR) in 1935, the EPR thought experiment challenged the completeness of quantum mechanics.
- EPR argued that if quantum mechanics were complete, it would have to explain physical reality through either:
  1. **Local Realism**: Particles have pre-existing properties (hidden variables) that determine their behavior before measurement.
  2. **Non-Locality**: The measurement of one particle instantaneously affects the state of another, regardless of the distance between them.

- EPR believed that **non-locality** was problematic because it implies that quantum mechanics allows for instantaneous influences between distant particles, which violates classical ideas of locality and causality. This made quantum mechanics seem incomplete because it relied on non-local effects without offering a fully deterministic explanation.

- Quantum mechanics rejects **local realism** and embraces **non-locality** through entanglement, where the state of entangled particles is not determined until one is measured, and the measurement of one affects the state of the other instantly.
  
- The EPR paradox led to experiments testing **Bell's Theorem**, which showed that quantum mechanics’ predictions cannot be reproduced by any theory based on local hidden variables, confirming that non-locality is an intrinsic feature of quantum mechanics.

---

### 5. **Measurement and Entanglement**
- Measurement plays a key role in defining entanglement.
- Entangled particles cannot be described independently; they share a joint wavefunction:
  
  $$ |\psi_{\text{entangled}}\rangle = \frac{1}{\sqrt{2}} \big( |0\rangle |1\rangle + |1\rangle |0\rangle \big) $$

  - This represents two particles, one in state $|0\rangle$ and the other in state $|1\rangle$.
  - Measurement on one particle collapses the wavefunction, determining the state of the other.

  **Example**:
  - Two electrons in a singlet spin state:
    $$ |\psi\rangle = \frac{1}{\sqrt{2}} \big( |\uparrow\rangle_1 |\downarrow\rangle_2 - |\downarrow\rangle_1 |\uparrow\rangle_2 \big) $$
    - Measuring the spin of one electron determines the spin of the other.

---

### 6. **Foundations of Quantum Entanglement**
- Entanglement lies at the heart of quantum mechanics and has foundational implications for physics:
  - **Bell’s Theorem**:
    - Demonstrates that no theory based on local hidden variables can reproduce the predictions of quantum mechanics.
    - The famous Bell inequality:
      $$ |C(A, B) - C(A, B')| + |C(A', B) + C(A', B')| \leq 2 $$
      - Quantum mechanics violates this inequality, confirming entanglement.
  - **Non-Locality vs. Causality**:
    - Entanglement introduces non-local correlations but does not violate causality.
  - **Information and Measurement**:
    - Measurement collapses the wavefunction, but the mechanism remains a central mystery in quantum foundations.

---

## **Key Examples**

### **1. Particle Decay**
- A particle decays probabilistically with the exponential law:
  $$ P(t) = e^{-\Gamma t} $$
  - Mean lifetime ($\tau$): $\tau = 1 / \Gamma$.
  - Example: Radioactive decay and its detection.

### **2. Spin Entanglement**
- Two electrons in a singlet state exhibit perfect anti-correlation in their spins:
  $$ |\psi_{\text{singlet}}\rangle = \frac{1}{\sqrt{2}} \big( |\uparrow\rangle |\downarrow\rangle - |\downarrow\rangle |\uparrow\rangle \big) $$

### **3. The Bell Test**
- Experiments testing Bell’s inequality confirm quantum predictions, ruling out local realism.

---

## **Takeaways**
1. Entanglement highlights the non-local and probabilistic nature of quantum mechanics.
2. Particle decay demonstrates quantum uncertainty, governed by exponential probability distributions.
3. The EPR puzzle and Bell’s Theorem provide key insights into the foundations of quantum mechanics.
4. Measurement collapses the wavefunction, making entanglement a key challenge for interpretations of quantum theory.

# Resources
1. [Quanta and Fields by Sean Carroll](https://www.amazon.com/Quanta-Fields-Biggest-Ideas-Universe/dp/0593186605)

---

<div style="display: flex; justify-content: space-between;">
  <a href="measurement.md"><- Measurement</a>
  <a href="fields.md">Fields -></a>
</div>
