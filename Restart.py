import SystemRecognition
import os
if SystemRecognition.SystemRecognition() == 'Darwin':
    print("shutdown")
    
from pynput import keyboard
import os
def restart():
    # Function to restart the system
    def restart_laptop():
        print("Restarting the laptop...")
        # For Windows
        os.system("shutdown /r /t 1")
    
        # For Linux/Unix-based systems, use this line instead:
        # os.system("sudo reboot")

        # For macOS, use this line:
        # os.system("sudo shutdown -r now")

        # Function that will be triggered on key press
    def on_press(key):
        try:
            # If the Enter key is pressed
            if key == keyboard.Key.enter:
                print("Enter key pressed")
                restart_laptop()
        except AttributeError:
            pass

    # Listener for keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
