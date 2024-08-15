import SystemRecognition
import os
if SystemRecognition.SystemRecognition() == 'Darwin':
    os.system("sudo shutdown -h 23:30")
