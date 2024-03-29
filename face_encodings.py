import face_recognition
import numpy as np

def euclidean_distance(encoding1, encoding2):
    return np.linalg.norm(encoding1 - encoding2)


# making a face image ready for comaparison
# the image should be loaded via face_recognition.load_image(image_path) 
# calculate the encodings of the faces in an image 
# and then compare it 

image_path = "comparison/dhoni_1.jpg"
face_image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(face_image, model='cnn')
known_face_locations = [face_locations]  # Convert to a list of lists
encodings = face_recognition.face_encodings(face_image)

image_path_2 = "comparison/dhoni_11.jpg"
face_image_2 = face_recognition.load_image_file(image_path_2)
face_locations_2 = face_recognition.face_locations(face_image_2, model='cnn')
known_face_locations_2 = [face_locations_2]  # Convert to a list of lists
encodings_2 = face_recognition.face_encodings(face_image_2)

euclidean_distances = [euclidean_distance(enc1, enc2) for enc1, enc2 in zip(encodings, encodings_2)]

if euclidean_distances[0] < 0.6:
    print("Faces match!")
else:
    print("Faces do not match!")


encodings = np.array(encodings)  # Convert list to NumPy array
encodings_2 = np.array(encodings_2)  # Convert list to NumPy array
results = face_recognition.compare_faces([encodings], encodings_2) 

if results[0].any() == True:
    print("The faces match!")
else:
    print("The faces do not match.")


