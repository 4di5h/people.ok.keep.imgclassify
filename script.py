import os
import shutil
import cv2
import face_recognition

# Function to check if a face is present in the image
def is_face(image_path):
    # Load the image
    img = face_recognition.load_image_file(image_path)

    # Resize the image for efficiency
    small_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # Find all face locations in the image
    face_locations = face_recognition.face_locations(small_img)

    # Check if a face is detected
    if face_locations:
        print(f"Face detected in {image_path}")
        return True
    else:
        print(f"No face detected in {image_path}")
        return False

# Specify the path to your album
album_path = 'C:/Users/bigti/Desktop/Kashmir Pics'

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
