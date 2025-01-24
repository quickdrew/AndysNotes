# Jetson Nano

The Jetson Nano is a powerful yet compact AI computing platform designed for edge AI projects. It provides the performance and flexibility needed for real-world AI applications while remaining accessible to hobbyists, students, and developers alike. Below, you'll find essential resources to get started with the Jetson Nano:


## Resources

- **[Jetson Nano Datasheet](https://components101.com/sites/default/files/component_datasheet/Jetson-Nano-DataSheet.pdf)**: Comprehensive technical specifications for the Jetson Nano.
- **[Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro)**: Official page for setup guides, tutorials, and detailed documentation.
- **[NVIDIA Jetson Projects](https://developer.nvidia.com/embedded/community/jetson-projects)**: Explore a collection of projects built by the Jetson community for inspiration and guidance.


## Getting Started

### Setting up SSH
**On Windows:**

1. Go to **Control Panel** → **Network and Sharing Center** → **Change adapter settings**.
2. Right-click on the **Ethernet connection** and select **Properties**.
3. Select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.
4. Assign a static IP (e.g., `192.168.1.1`) and subnet mask (e.g., `255.255.255.0`). Leave the **gateway** and **DNS** blank.

**On Jetson Nano:**
1. Got to **Netowrk** → **Edit Connections** 
2. Select **wired connection 1** under **Ethernet** and click the settings button located in the bottom left 
3. Go to **IPV4 Settings** and assign a static IP (e.g., `192.168.1.2`) and Netmask (e.g., `24`). Leave the **gateway** blank. 

**On Windows:** 

1. Ping the Jetson Nano:
```bash
   ping 192.168.1.2
```
2. If the ping works, try SSH:
```bash
   ssh jetson@192.168.1.2
```
3. Create a fingerprint, password is ``jetson``


## Hello AI World

Based off the [Jetson AI introductionary project](https://github.com/dusty-nv/jetson-inference)