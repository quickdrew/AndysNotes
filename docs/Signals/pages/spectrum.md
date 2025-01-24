# FCC Electromagnetic Spectrum
Based off the [FCC Electromagnetic Spectrum](https://transition.fcc.gov/oet/spectrum/table/fcctable.pdf), this page covers technical details for working with specific frequency bands.



## 960-1164MHz Aeronautical Radionavigational Service (ARNs) & Aeronautical Mobile (Route) Service (AM(R)S)

### [1090MHz Automatic Dependent Surveillance–Broadcast](https://mode-s.org/1090mhz/content/ads-b/1-basics.html)

- Data: Broadcasted messages include flight details such as position, altitude, and speed.
- Usage: Decode these signals and visualize the real-time locations of aircraft on a map.
- RTL-SDR decoder (has a basic visualization tool): [dump1090](https://github.com/antirez/dump1090)
- For plotting track lines use: [Virtual Radar Server](https://www.virtualradarserver.co.uk/)