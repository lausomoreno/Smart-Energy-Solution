# Smart-Energy-Solution
A hardware–software system that cuts lab test system idle power consumption by 50–60%. Uses a Raspberry Pi Pico + high-voltage relay controlled via a Python script that detects inactivity (keyboard/mouse + applications) and powers down inefficient instruments. Demonstrated ROI in under six months.


# Automated Lab Power Optimizer

## Overview
This project provides a **hardware–software solution to reduce lab test system idle power consumption by 50–60%**.  
By monitoring user activity and running applications on the host PC, the system can automatically power down inefficient lab instruments through a **Raspberry Pi Pico + high-voltage relay setup**, delivering an **ROI in less than six months**.

---

## Repository Structure
- **powermanager.py**  
  Python script that runs on the host PC.  
  - Monitors keyboard/mouse activity and active applications.  
  - Sends control signals to the Raspberry Pi Pico to signal when the system is active or idle

- **main.py**  
  Firmware for the Raspberry Pi Pico.  
  - Decodes incoming signals from the PC.  
  - Toggles the high-voltage relay to cut or restore power to lab instruments.

- **RUN_Power_Manager.vbs**  
  Windows script to ensure `powermanager.py` runs continuously in the background.  

---

## Hardware Setup
- **Raspberry Pi Pico** connected via USB to the PC  
- **USB-controllable high-voltage relay** replacing the power strip extension  
- **Lab instruments** powered through the relay  



