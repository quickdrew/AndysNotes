# Vehicle Electrical/Electronic Architecture

Vehicle Electrical/Electronic (E/E) architecture refers to the overall design and integration of a vehicle's electrical and electronic systems, encompassing hardware, software, and communication networks. It defines how components such as sensors, actuators, electronic control units (ECUs), wiring, and communication protocols (e.g., CAN, LIN, Ethernet) are organized and interconnected to enable vehicle functionality. Modern E/E architectures are evolving to support increasing system complexity, including advanced driver-assistance systems (ADAS), infotainment, and electrification, while meeting stringent requirements for performance, scalability, safety, and cybersecurity.

---

## Electronic Control Units (ECUs)

An Electronic Control Unit (ECU) is an embedded system within automotive electronics that manages a system or task in a vehicle. ECUs act as the brains processing sensory or other relevant data to send control signals to actuators and interfaces. Like most embedded systems, ECUs can take many hardware forms such as microcontrollers, microprocessors, ASICs, and FPGAs.

---

## Automotive domains

A domain refers to a system typically composed of a collection of ECUs and their subordinate systems, working together to perform a specific vehicle-level function. What a domain is and which electronics belong in each domain can vary depending on who you ask and the specifics of the vehicle, especially as vehicles become more complex and interconnected over time. Here's how [Dr. Ahmad MK Nasser](#references) breaks down the domains:


### **Fuel-Based Powertrain Domain**

This domain manages internal combustion engines (ICEs), focusing on tasks such as engine performance, gear shifting, and emissions control.

- **Engine Control Module (ECM)**: Regulates engine functions, including ignition timing, fuel injection, and engine cooling
- **Transmission Control Module (TCM)**: Optimizes gear shifting in automatic transmissions by analyzing input data such as engine speed, vehicle speed, throttle position


### **Electric Drive Powertrain Domain**

This domain handles battery management and electric motor control in electric vehicles (EVs).

- **Battery Management System (BMS)**: Monitors the state of charge (SoC) and state of health (SoH), and ensures battery safety and thermal management.
- **Powertrain Electronic Control Unit (PECU)**: Manages motor speed and acceleration, and controls voltage and frequency supplied to the motor.


### Chassis Safety Control Domain

The chassis domain ensures vehicle stability and safety through active and passive safety systems.

- **Electronic Braking Control Module (EBCM)**: Provides functions like ABS, ESC, and emergency braking.
- **Electronic Power Steering (EPS)**: Assists steering and enables lane correction.
- **Airbag Control Module**: Deploys airbags during collisions for passenger safety.


### Interior Cabin Domain

This domain focuses on comfort, convenience, and security features.

- **Body Control Module (BCM)**: Controls keyless entry, seat adjustments, and lighting.
- **Climate Control Module (CCM)**: Manages cabin heating, cooling, and ventilation.


### Infotainment and Connectivity Domain

This domain integrates driver and passenger-facing interfaces, focusing on entertainment and connectivity.

- **In-Vehicle Infotainment (IVI)**: Provides entertainment, navigation, and driver information.
- **Telematics Control Unit (TCU)**: Facilitates GPS, remote connectivity, and over-the-air (OTA) updates.


### Cross-Domain Communication

Cross-domain functionality provides a reliable communication framework for inter-domain message exchange.

- **Central Gateway (CGW)**: Acts as an in-vehicle router, enabling communication across different network segments (e.g., CAN to Ethernet) and supporting cybersecurity measures to block unwanted traffic.

---

## References

1. Ahmad MK Nasser, *Automotive Cybersecurity Engineering Handbook*.