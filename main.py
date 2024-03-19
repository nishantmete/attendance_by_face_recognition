#importing all the necessary libraries

import cv2
import face_recognition
from PIL import Image, ImageDraw


test_file = face_recognition.load_image_file("myface.jpg", mode="RGB")
test_face = cv2.imread("myface.jpg")

locations = face_recognition.face_locations(test_file)
print(locations)



top, right, bottom, left = locations[0]
top, right, bottom, left = int(top), int(right), int(bottom), int(left)


with Image.open("myface.jpg") as img:
    draw = ImageDraw.Draw(img)

    rectangle_coords = (left, top, right, bottom)

    draw.rectangle(rectangle_coords, outline="green", width=2)

    img.save("my_new_face.jpg")





"""for (top, right, bottom, left) in locations:
    cv2.rectangle(test_face, (left, top), (right, bottom), (0, 255, 0), 2)

cv2.imshow("Test", test_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
# Create a VideoCapture object
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
cv2.destroyAllWindows()
"""




