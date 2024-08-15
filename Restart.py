import SystemRecognition
import os
if SystemRecognition.SystemRecognition() == 'Windows':
    print("shutdown")
if SystemRecognition.SystemRecognition() == 'Darwin':
    print("shutdown")