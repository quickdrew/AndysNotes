# External Automotive Sensors and Signals

Modern vehicles integrate a variety of sensors to interact with their external environment. These sensors are critical for safety, efficiency, and comfort. Below is a description of key external sensors, their functionalities, and the data they provide.

---

## Vision-Based Sensors

### Cameras
Cameras capture visual data for various applications. They are used for digital rear-view mirrors, traffic sign recognition, surround view systems, and lane-keeping assistance.

Operation: Cameras detect light on a photosensitive surface using a lens and process the data into images for use by ECUs. They typically support 8 MP resolution at 60 FPS, use GMSL links for data transmission at rates up to 6 GB/s, and are often configured via I2C.

Risks: Interference can lead to misidentification of objects or privacy violations.

### Infrared Sensors
Infrared sensors detect heat signatures, improving visibility in low-light conditions.

Applications: Night vision systems, pedestrian detection, and animal detection.

Operation: Detect emitted infrared radiation and process it into thermal images.

Risks: Sensor obfuscation can reduce visibility.

---

## Proximity and Object Detection Sensors

### LiDAR (Light Detection and Ranging)
LiDAR generates 3D spatial maps by emitting laser pulses. It is used for object detection and classification, as well as autonomous navigation.

Operation: Measures time-of-flight of laser pulses to calculate distances and interfaces with the host ECU via 1000Base-T1 Ethernet.

Risks: Tampering can disrupt object detection and compromise safety systems.

### RADAR (Radio Detection and Ranging)
RADAR detects objects using electromagnetic waves. It is applied in adaptive cruise control, collision avoidance, and blind-spot monitoring.

Operation: Measures range and speed using the Doppler effect and connects to the host ECU via CAN or Ethernet.

Risks: Jamming or spoofing can impact obstacle detection.

### Ultrasonic Sensors
Ultrasonic sensors detect nearby objects using high-frequency sound waves. They are commonly used for parking assistance and proximity alerts.

Operation: Emit sound waves and calculate the distance based on reflected echoes. They communicate with the ECU via CAN.

Risks: Signal interference can compromise obstacle detection.

---

## Communication and Navigation Systems

### Vehicle-to-Everything (V2X) Communication
V2X communication enables interaction between vehicles, infrastructure, and other road users.

Applications: Traffic management and collision prevention.

Operation: Uses DSRC or cellular networks for wireless data exchange.

Risks: Cyberattacks can compromise communication reliability.

### Telematics Systems
Telematics systems integrate GPS, cellular communication, and sensors to enable real-time data exchange with remote servers.

Applications: Fleet management, remote diagnostics, over-the-air (OTA) updates, and stolen vehicle recovery.

Operation: Collects data from sensors like GPS and speedometers, sends it to cloud servers via cellular networks, and allows bidirectional communication for remote management.

Risks: Data breaches can expose sensitive information, and communication hijacking can lead to unauthorized vehicle control or tracking.

### GNSS (Global Navigation Satellite System)
GNSS provides location, velocity, and timing information. It is used for navigation, geofencing, and route optimization.

Operation: Receives satellite signals to determine position and interfaces with the host ECU via CAN or UART.

Risks: Spoofing or jamming can disrupt localization and timing.

---

## Access and Monitoring Systems

### Passive Keyless Entry (PKE) and Remote Keyless Entry (RKE)
PKE and RKE systems enable automatic vehicle access and remote locking/unlocking.

Operation: PKE detects key proximity using low-frequency (LF) and ultra-high frequency (UHF) signals, while RKE uses RF signals for remote interaction.

Risks: Relay attacks can exploit vulnerabilities in signal transmission.

### Tire Pressure Monitoring System (TPMS)
TPMS monitors tire pressure to ensure safety and efficiency.

Operation: Sensors transmit pressure data wirelessly to the ECU, typically at 315 MHz or 433 MHz.

Risks: Signal spoofing can result in false alerts or undetected issues.

---

## Summary

These external sensors and systems form the backbone of modern vehicles, enabling advanced functionalities and ensuring safety. Grouping and understanding their roles, communication methods, and potential vulnerabilities is critical for optimizing performance and securing operations.
