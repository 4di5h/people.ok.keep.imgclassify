import os
import shutil
import cv2
import dlib

# Load pre-trained face detection model
detector = dlib.get_frontal_face_detector()


def is_face(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)

    # Check if a face is detected
    if faces:
        print(f"Face detected in {image_path}")
        return True
    else:
        print(f"No face detected in {image_path}")
        return False

# Specify the path to your album
album_path = '/PATH/'

# Print list of images
print("List of images:", os.listdir(album_path))

# Create a new folder for pictures with faces
only_faces_path = os.path.join(album_path, 'Only Faces')
os.makedirs(only_faces_path, exist_ok=True)

# Move images with faces to the new folder
for filename in os.listdir(album_path):
    if filename.endswith('.JPG') or filename.endswith('.PNG'):
        image_path = os.path.join(album_path, filename)
        print("Processing image:", image_path)

        # Check if is_face is being called
        print("Calling is_face for:", image_path)
        if is_face(image_path):
            shutil.move(image_path, os.path.join(only_faces_path, filename))

print("Script execution completed.")
