#importing all the necessary libraries

"""
import cv2
import dlib
import face_recognition
import pandas 
"""

"""# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 for the default camera

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Capture frames from the camera
while True:
    # Capture frame-by-frame
    state, frame = cap.read()

    if not state:
        print("Can't receive frame. Exiting...")
        break

    # Display the captured frame
    cv2.imshow('frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break
    
print(cap.isOpened(), cap.getExceptionMode())
# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()"""


print("Hello World!")




