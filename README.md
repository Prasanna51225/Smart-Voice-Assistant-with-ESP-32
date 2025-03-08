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
ESP32-Voice-Control-System/ │──  Android_App/ # Kotlin app for speech-to-text conversion
│── ESP32_Code/ # ESP32 Wi-Fi communication & serial transmission
│──  Python_Scripts/ # Python script for command execution in VS Code
│──  Docs/ # Circuit diagrams, flowcharts, and setup guides
│──  Assets/ #demo videos
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
- 1️) User speaks a command in the Android app (e.g., "Open YouTube").
- 2️) The app converts speech to text and sends it to ESP32 via Wi-Fi.
- 3️) ESP32 receives the command and transmits it to the laptop via a serial connection.
- 4️) Python script on the laptop reads the command and executes the corresponding system task.

## WORK-FLOW:
### Esp32 code-output terminal
![WhatsApp Image 2025-03-08 at 16 26 47_4d3e3fa8](https://github.com/user-attachments/assets/c675fe30-3bba-4d93-aa4a-d725a9ae68e4)
### python script-output terminal
![WhatsApp Image 2025-03-08 at 16 26 46_8144f356](https://github.com/user-attachments/assets/59a580fd-08db-4fdf-b38b-c1d818b20d8d)
### Android App UI
![WhatsApp Image 2025-03-08 at 16 27 26_df9e7922](https://github.com/user-attachments/assets/ff7a1bbf-6296-49aa-ae77-cbaf13f69bc1)
- (use your esp32 ip address)


# Voice-Controlled Assistant for ESP32

This project is a voice-controlled assistant that can execute various commands through a Flask API. Below are the supported commands:

##  System Commands:
- *"Open Notepad"* — Opens Notepad on your computer  
- *"Open Calendar"* — Opens your system’s calendar  
- *"Open PowerPoint"* — Opens PowerPoint with a blank slide  

##  Web Commands:
- *"Open YouTube"* — Opens YouTube in your browser  
- *"Open Google"* — Opens Google in your browser  
- *"Open My Amrita"* — Opens the My Amrita website  

##  Alarm Command:
- *"Set alarm at HH:MM"* — Sets an alarm at the specified time (24-hour format)  

##  Media Commands:
- *"Open Camera"* — Captures a photo using your webcam  
- *"Take Screenshot"* — Takes a screenshot and saves it  
- *"Record Video"* — Records a 5-second video using your webcam  

##  YouTube Search:
- *"Play [song/term] on YouTube"* — Opens YouTube and searches for the term you mentioned  



Future Enhancements
- > Integrate AI (ChatGPT/GPT-4) for smart responses
- > Expand to home automation (control lights, fans, IoT devices)
- > Enable voice authentication for security









