# Smart-Voice-Assistant-with-ESP-32
Voice-controlled system using ESP32, Android (Kotlin), and Python. Converts speech to text, transmits commands via Wi-Fi, and executes tasks in VS Code. Features real-time speech recognition, IoT integration, and smart automation. Ideal for AI, IoT, and home automation projects.

##  Features  
**Real-time speech recognition & execution**  
**Wi-Fi-based communication between Android → ESP32 → Laptop**  
**Automated control of system applications & tasks**  
**Expandable for AI, IoT, and home automation**  


##  Technologies Used  
- **Android (Kotlin, Kotlin DSL)** → Speech-to-text conversion & Wi-Fi communication  
- **ESP32 (Arduino/PlatformIO)** → Handles Wi-Fi & serial transmission  
- **Python (VS Code/PlatformIO)** → Reads serial data & executes system commands  


##  Project Structure  
ESP32-Voice-Control-System/ │── 📁 Android_App/ # Kotlin app for speech-to-text conversion
│── 📁 ESP32_Code/ # ESP32 Wi-Fi communication & serial transmission
│── 📁 Python_Scripts/ # Python script for command execution in VS Code
│── 📁 Docs/ # Circuit diagrams, flowcharts, and setup guides
│── 📁 Assets/ #demo videos
│── README.md # Project documentation




##  Installation & Setup Guide  

### **1) Android App (Speech-to-Text & Wi-Fi Communication)**  
- Clone the `Android_App/` folder.  
- Open in **Android Studio**.  
- Grant **Microphone & Wi-Fi** permissions.  
- Build and run the app on your mobile device.  

### **2️) ESP32 Setup (Wi-Fi & Serial Communication)**  
- Clone the `ESP32_Code/` folder.  
- Open the `.ino` file in **Arduino IDE** (or use PlatformIO in VS Code).  
- Select **ESP32 board**, connect via USB, and **upload the code**.  

### **3️) Python Script (Command Processing in VS Code)**  
- Clone the `Python_Scripts/` folder.  
- Install dependencies (if required):  
  pip install pyserial

## How It Works
1️) User speaks a command in the Android app (e.g., "Open YouTube").
2️) The app converts speech to text and sends it to ESP32 via Wi-Fi.
3️) ESP32 receives the command and transmits it to the laptop via a serial connection.
4️) Python script on the laptop reads the command and executes the corresponding system task.

## WORK-FLOW:



Future Enhancements
> Integrate AI (ChatGPT/GPT-4) for smart responses
> Expand to home automation (control lights, fans, IoT devices)
> Enable voice authentication for security








