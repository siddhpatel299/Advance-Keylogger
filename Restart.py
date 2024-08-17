import SystemRecognition
import os

def restart():
    # Function to restart the system
    def restart_laptop():
        print("Restarting the laptop...")
        # For Windows
        if SystemRecognition.SystemRecognition() == 'Windows':
            os.system("shutdown /r /t 1")
    
        # For Linux/Unix-based systems, use this line instead:
        if SystemRecognition.SystemRecognition() == 'Linux':
            os.system("sudo reboot")

        # For macOS, use this line:
        if SystemRecognition.SystemRecognition() == 'Darwin':
            os.system("sudo shutdown -r now")

        # Function that will be triggered on key press
    # def on_press(key):
    #     try:
    #         # If the Enter key is pressed
    #         if key == keyboard.Key.enter:
    #             print("Enter key pressed")
    #             restart_laptop()
    #     except AttributeError:
    #         pass

    # # Listener for keyboard events
    # with keyboard.Listener(on_press=on_press) as listener:
    #     listener.join()
