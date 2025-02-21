import pyautogui
import time
import keyboard

# Configuration
stop_key = "esc"      # Key to stop the autoclicker
start_key = "f6"

print("Start Autoclicker by pressing F6")

while True:
    if keyboard.is_pressed(start_key):
        print("Autoclicker started. Stop by pressing ESC")
        break

try:
    while True:
        # Perform a left mouse click
        pyautogui.doubleClick()

        # Stop the autoclicker if the stop key is pressed
        if keyboard.is_pressed(stop_key):
            print("Autoclicker stopped.")
            break
except KeyboardInterrupt:
    print("Autoclicker stopped by user.")