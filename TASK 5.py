import cv2
import face_recognition

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load a pre-trained face recognition model (HOG-based)
# This model is not suitable for face identification across different images, but it can be replaced
# with more advanced models like Siamese networks or ArcFace for face recognition tasks.
# Here, we'll focus on detecting faces using the Haar Cascade and recognizing them using face_recognition.
known_faces_encodings = []
known_faces_names = []

# Load sample images and encode known faces
image_obama = face_recognition.load_image_file("obama.jpg")
encoding_obama = face_recognition.face_encodings(image_obama)[0]
known_faces_encodings.append(encoding_obama)
known_faces_names.append("Barack Obama")

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using the Haar Cascade
    faces_haar = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Detect faces using the face_recognition library
    faces_recognition = face_recognition.face_locations(frame)

    for (x, y, w, h) in faces_haar:
        # Draw a rectangle around the detected face using Haar Cascade
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for face_location in faces_recognition:
        # Draw a rectangle around the detected face using face_recognition
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Encode the face and compare with known faces
        face_encoding = face_recognition.face_encodings(frame, [face_location])[0]

        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_faces_names[first_match_index]

        # Display the name of the recognized face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the frame with faces detected
    cv2.imshow('Face Detection and Recognition', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
