from flask import Flask, request
import webbrowser
import os
import urllib.parse
import re
import cv2
import numpy as np
import pyautogui
import time
import mss
import pyaudio
import wave
import ffmpeg
import threading
from datetime import datetime, timedelta

app = Flask(__name__)

alarm_time = None
alarm_thread = None

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def check_alarm():
    global alarm_time
    while True:
        if alarm_time and datetime.now() >= alarm_time:
            print("Alarm time reached!")
           
            os.system('echo "\a"')  # This plays a beep sound
            alarm_time = None  # Reset alarm time
        time.sleep(1)  # Check every second

@app.route('/command', methods=['GET'])
def handle_command():
    global alarm_time
    command = request.args.get('cmd')
    command = urllib.parse.unquote(command)  # Decode any URL-encoded characters
    print(f"Received command: {command}")

    # Open YouTube
    if command.strip().lower() == "open youtube":
        try:
            print("Opened YouTube")
            webbrowser.open("https://www.youtube.com")
            return {"message": "YouTube opened!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening YouTube: {str(e)}", "status": "failure"}, 500

    # Open Google
    elif command.strip().lower() == "open google":
        try:
            print("Opened Google")
            webbrowser.open("https://www.google.com/")
            return {"message": "Google opened!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening Google: {str(e)}", "status": "failure"}, 500

    # Open My Amrita
    elif command.strip().lower() == "open my amrita":
        try:
            print("Opened My Amrita")
            webbrowser.open("https://my.amrita.edu")
            return {"message": "My Amrita opened!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening My Amrita: {str(e)}", "status": "failure"}, 500

    # Open Notepad
    elif command.strip().lower() == "open notepad":
        try:
            print("Opened Notepad")
            os.system("notepad.exe")
            return {"message": "Notepad opened!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening Notepad: {str(e)}", "status": "failure"}, 500

    # Open Calendar
    elif command.strip().lower() == "open calendar":
        try:
            print("Opened Calendar")
            os.system('explorer.exe outlookcal:')
            return {"message": "Calendar opened!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening Calendar: {str(e)}", "status": "failure"}, 500

    # Open PowerPoint Blank Slide
    elif command.strip().lower() == "open powerpoint":
        try:
            print("Opened PowerPoint with a Blank Slide")
            os.system('start powerpnt')  # This opens PowerPoint
            return {"message": "PowerPoint opened with a blank slide!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error opening PowerPoint: {str(e)}", "status": "failure"}, 500

    # Set Alarm
    elif command.strip().lower().startswith("set alarm at"):
        try:
            # Extract the time from the command
            time_pattern = r"set alarm at (\d{1,2}):(\d{2})"
            match = re.search(time_pattern, command.strip().lower())
            if match:
                hour = int(match.group(1))
                minute = int(match.group(2))

                # Get current time and set the alarm
                now = datetime.now()
                alarm_time = datetime(now.year, now.month, now.day, hour, minute)

                # If the alarm time is in the past, set it for the next day
                if alarm_time < now:
                    alarm_time += timedelta(days=1)

                print(f"Alarm set for {alarm_time}")
                return {"message": f"Alarm set for {alarm_time.strftime('%H:%M')}", "status": "success"}, 200
            else:
                return {"message": "Invalid time format. Please use 'HH:MM'.", "status": "failure"}, 400
        except Exception as e:
            return {"message": f"Error setting alarm: {str(e)}", "status": "failure"}, 500

    # Open Camera and Capture Image
    elif command.strip().lower() == "open camera":
        try:
            print("Opening camera")
            cap = cv2.VideoCapture(0)  # Open the camera (0 is the default camera)
            if not cap.isOpened():
                return {"message": "Error opening camera!", "status": "failure"}, 500

            ret, frame = cap.read()
            if ret:
                filename = "captured_image.jpg"
                cv2.imwrite(filename, frame)  # Save the captured frame as an image
                cap.release()
                cv2.destroyAllWindows()  # Close the camera window
                return {"message": f"Photo captured and saved as {filename}!", "status": "success"}, 200
            else:
                return {"message": "Failed to capture image", "status": "failure"}, 500
        except Exception as e:
            return {"message": f"Error opening camera: {str(e)}", "status": "failure"}, 500

    # Take Screenshot
    elif command.strip().lower() == "take screenshot":
        try:
            print("Taking screenshot")
            screenshot = pyautogui.screenshot()  # Take a screenshot
            filename = "screenshot.png"
            screenshot.save(filename)  # Save the screenshot as a PNG file
            return {"message": f"Screenshot saved as {filename}!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error taking screenshot: {str(e)}", "status": "failure"}, 500

    # Record a 5-second video
    elif command.strip().lower() == "record video":
        try:
            print("Recording video for 5 seconds")
            cap = cv2.VideoCapture(0)  # Open the camera (0 is the default camera)
            if not cap.isOpened():
                return {"message": "Error opening camera for video recording!", "status": "failure"}, 500

            # Set video codec and output file
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

            start_time = time.time()
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Write the frame to the video file
                out.write(frame)

                # Stop recording after 5 seconds
                if time.time() - start_time > 5:
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()

            return {"message": "Video recorded and saved as video.avi!", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error recording video: {str(e)}", "status": "failure"}, 500

    # Check if the command matches the pattern for 'play on youtube'
    yt_search_term = extract_yt_term(command)
    if yt_search_term:
        try:
            print(f"Searching for '{yt_search_term}' on YouTube")
            youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(yt_search_term)}"
            webbrowser.open(youtube_url)
            return {"message": f"Searching for '{yt_search_term}' on YouTube...", "status": "success"}, 200
        except Exception as e:
            return {"message": f"Error searching YouTube: {str(e)}", "status": "failure"}, 500

    return {"message": "Command not recognized.", "status": "failure"}, 400


if __name__ == '__main__':
    alarm_thread = threading.Thread(target=check_alarm, daemon=True)
    alarm_thread.start()
    app.run(host='0.0.0.0', port=5000)
