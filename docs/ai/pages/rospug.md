# Jetson Nano USB Networking Debug Guide (VMware)

This guide explains how to fix Jetson Nano USB networking when following [jetson burn instructions](https://drive.google.com/drive/folders/1R8W_awlw6L6BnML3On4hu7pJtXLEG8uR).


## 🧯 Quick Reference: What Command to Run When

| Situation | Command |
|----------|---------|
| USB not showing up in VM | Connect via `VM > Removable Devices` |
| Interface is down | `sudo ip link set ensXXX up` |
| No IP assigned | `sudo dhclient ensXXX` |
| DHCP fails | `sudo ip addr add 192.168.55.100/24 dev ensXXX` |
| SSH doesn't respond | `sudo systemctl start ssh` |
| Connection randomly breaks | `sudo dhclient -v` |

---

## 🟡 SCENARIO: Your VM doesn’t get an IP address or can’t ping `192.168.55.1`

> You’re in this situation if:
> - `ip a` inside the VM shows `ens35u1` or `ens35u1i5`, but **no IPv4 address**
> - You run `ping 192.168.55.1` and it fails
> - SDK Manager can’t detect the Jetson even though it’s booted

### 🔧 Step-by-step fix:

1. **Make sure VMware has the USB device connected to the VM:**

   In VMware:
   - Go to `VM > Removable Devices`
   - Find the **NVIDIA USB Gadget** or **Linux File-Stor Gadget**
   - Click **Connect (Disconnect from Host)**

2. **Bring the interfaces up in the VM:**

   ```bash
   sudo ip link set ens35u1 up
   sudo ip link set ens35u1i5 up
   ```

3. **Try getting an IP via DHCP:**

   ```bash
   sudo dhclient ens35u1
   ```

   or

   ```bash
   sudo dhclient ens35u1i5
   ```

   - ✅ If `ping 192.168.55.1` works after this — you're done.
   - ❌ If `dhclient` just hangs or fails, continue below.

4. **Manually assign an IP address:**

   ```bash
   sudo ip addr add 192.168.55.100/24 dev ens35u1i5
   ```

5. **Now test it:**

   ```bash
   ping 192.168.55.1
   ssh hiwonder@192.168.55.1
   ```

---

## 🔵 SCENARIO: SDK Manager still doesn't connect, even after ping works

> If `ping 192.168.55.1` works, but SDK Manager can’t connect:

- Make sure SSH is **running** on the Jetson:
  
  ```bash
  sudo systemctl start ssh
  ```

- Then, in SDK Manager:
   - Set **Connection** to: `Manual`
   - IP: `192.168.55.1`
   - Username: `hiwonder`
   - Password: your Jetson Nano password
   - Click **Refresh**

---

## 🔁 SCENARIO: Internet broke

> You were able to ping or connect before, but now it stopped.

### 🧼 Simple fix:

```bash
sudo dhclient -v
```

This renews the DHCP lease and resets the network.

If it doesn’t work:
- Replug the Jetson’s USB cable
- Reconnect the USB gadget in VMware
- Repeat steps from the “no IP” scenario above

---
