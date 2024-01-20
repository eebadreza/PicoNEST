# Source Code

The `src` folder contains the source code for the PicoNest home automation system, specifically designed for the Raspberry Pi Pico microcontroller. The primary code file is named `main.py`.

## Raspberry Pi Pico Code

1. **main.py:**
   - This file is the main Python script for the PicoNest project, designed to run on the Raspberry Pi Pico microcontroller. It encompasses the core functionalities of the home automation system, including device control, communication, and sensor interactions.

## How to Use

#### On Computer using Thonny

To run the PicoNest project on the Raspberry Pi Pico while connected to a computer, follow these steps:

1. **Prepare Raspberry Pi Pico:**
   - Ensure your Raspberry Pi Pico is properly powered and connected to the necessary devices (sensors, actuators, etc.) as per the project requirements.

2. **Connect to Computer:**
   - Connect the Raspberry Pi Pico to your computer using a USB cable.

3. **Download System Files:**
   - Download the required system files for Raspberry Pi Pico [here](https://micropython.org/download/RPI_PICO_W/).

4. **Add System Files to Boot Up:**
   - Extract the downloaded uf2 files and copy them to the root directory of your Raspberry Pi Pico.

5. **Execution:**
   - Run code using Thonny after connecting to the correct Raspberry Pi Pico in device option.

#### Without Computer using 5V Adapter

To run the PicoNest project on the Raspberry Pi Pico without connecting it to a computer, follow these steps:

1. **Prepare Raspberry Pi Pico:**
   - Ensure your Raspberry Pi Pico is properly powered and connected to the necessary devices (sensors, actuators, etc.) as per the project requirements.

2. **Save Code:**
   - Save the `main.py` file to the root directory of your Raspberry Pi Pico.

3. **Power On:**
   - Power on the Plug for the Circuit.

4. **Execution:**
   - The `main.py` script will execute automatically upon boot, initiating the PicoNest home automation system.

## Note

- Make sure to configure the GPIO pins and connections in the `main.py` file according to your specific hardware setup.

- Refer to the project documentation for detailed information on GPIO pin configurations, hardware requirements, and any additional setup steps.

- In case of issues or modifications, feel free to reach out to the project maintainers or community for assistance.
