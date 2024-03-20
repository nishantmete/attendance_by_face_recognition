# this script is for recogninizing the faces in an image and then make a boundry around the faces, this works with the help of face_recognition python library 

#importing all the necessary libraries
import cv2
from mtcnn.mtcnn import MTCNN
from insightface.app import FaceAnalysis
import numpy as np
from numpy import asarray
from PIL import Image

# Initializing FaceNet model
model = FaceAnalysis(allowed_modules=['insightface'])
model.prepare(ctx_id=0, det_size=(640, 640))

# Load an image
image = cv2.imread('path/to/image.jpg')

# Detect faces and get encodings
faces = model.get(image)
encodings = [face.normed_encoding for face in faces]

test_file = face_recognition.load_image_file("multiplePeople.jpg", mode="RGB") #always need to load the file first before face recognition
test_face = cv2.imread("multiplePeople.jpg") #this opens up a new window showcasing the image specfied

locations = face_recognition.face_locations(test_file) #gives the co-ordinates of each face in a seperate tuple in a main list
print(locations) #printing the locations to verify the number of faces


with Image.open("multiplePeople.jpg") as img:
    draw = ImageDraw.Draw(img)

    #running a for loop to let the system draw rectangles on all the faces
    for coordinate, value in enumerate(locations):
        #specifying the rectangle co-ordinates as they are 4 each in a list of tuple(s).
        #the co-ordinate here should be in the order of left, top, right, bottom
        rectangle_coords = (locations[coordinate][3], locations[coordinate][0], locations[coordinate][1], locations[coordinate][2])
        #draw.rectangle is a function used to draw rectangles, the function needs co-ordinates, outline color, and width as parameters
        draw.rectangle(rectangle_coords, outline="green", width=2)

    img.save("multiple_new_detected.jpg")



