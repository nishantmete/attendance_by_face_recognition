# this script is for recogninizing the faces in an image and then make a boundry around the faces, this works with the help of face_recognition python library 

#importing all the necessary libraries
import cv2
import face_recognition
from mtcnn.mtcnn import MTCNN
#from insightface import FaceAnalysis
import numpy as np
from numpy import asarray
from PIL import Image, ImageDraw
import imageio



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

#########                          VIDEO                                #######

# Load the known face encodings
known_face_encodings = [...]  # Replace with your known face encodings
known_face_names = [...]  # Replace with the corresponding names


# Load the video file
input_video = imageio.get_reader('video_of_people_walking.mp4')

# Create a new video writer
output_video = imageio.get_writer('modified_video_of_people_walking.mp4')

for frame in input_video:
    # Convert the frame to RGB format
    rgb_frame = frame[:, :, ::-1]

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Convert the frame to a Pillow Image
    pil_image = Image.fromarray(rgb_frame)
    draw = ImageDraw.Draw(pil_image)

    # Loop through the detected faces
    for face_location in face_locations:
        # Draw a rectangle around the face
        top, right, bottom, left = face_location
        draw.rectangle(((left, top), (right, bottom)), outline=(9, 249, 59), width=2)

    # Convert the Pillow Image back to a numpy array
    processed_frame = np.asarray(pil_image)

    # Write the processed frame to the output video
    output_video.append_data(processed_frame[:, :, ::-1])

# Close the video writers
input_video.close()
output_video.close()