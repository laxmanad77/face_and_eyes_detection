import cv2
import os
import urllib.request
import sys
import ssl  # Imported to handle the macOS certificate error


def download_cascade(url, filename):
    """
    Downloads the Haar Cascade XML files directly from the official OpenCV repo
    if they do not already exist in the local directory.
    """
    if not os.path.exists(filename):
        print(f"Downloading {filename} from OpenCV repository...")
        try:
            # Bypass the SSL certificate verification error
            ssl._create_default_https_context = ssl._create_unverified_context

            urllib.request.urlretrieve(url, filename)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
            sys.exit(1)


def main():
    # 1. Define filenames for the local XML files
    face_xml = "haarcascade_frontalface_default.xml"
    eye_xml = "haarcascade_eye.xml"

    # 2. Automatically download the required Haar Cascades to bypass environment errors
    face_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    eye_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml"

    download_cascade(face_url, face_xml)
    download_cascade(eye_url, eye_xml)

    # 3. Load the image
    filename = "me.jpg"
    img = cv2.imread(filename)

    if img is None:
        print(f"Error: Could not read '{filename}'.")
        print("Ensure your photo is named exactly 'me.jpg' and is in the same folder as this script.")
        return

    # 4. Initialize the Cascade Classifiers using the local files
    face_cascade = cv2.CascadeClassifier(face_xml)
    eye_cascade = cv2.CascadeClassifier(eye_xml)

    # Safety check to ensure the classifiers are no longer empty
    if face_cascade.empty() or eye_cascade.empty():
        print("CRITICAL ERROR: Failed to load the Cascade Classifiers. The XML files may be corrupted.")
        return

    # Convert the image to grayscale for the detection algorithm
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 5. Detect the face dynamically
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    if len(faces) == 0:
        print("No face detected! Try a clearer photo with better lighting.")
        return

    # 6. Loop through any detected faces and draw the required shapes
    for (x, y, w, h) in faces:
        # Draw a GREEN circle around the face (BGR format: 0, 255, 0)
        center = (x + w // 2, y + h // 2)
        radius = int(w / 1.7)
        cv2.circle(img, center, radius, (0, 255, 0), 3)

        # Tag the image with the text "this is me"
        cv2.putText(img, "this is me", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 7. Isolate the face region to search for eyes (Region of Interest)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # Detect eyes within the face bounding box
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))

        # Loop through detected eyes and draw RED bounding boxes (BGR format: 0, 0, 255)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # 8. Display and save the final annotated image
    cv2.imshow("Portfolio Project - Dynamic Feature Detection", img)

    output_name = "annotated_me_dynamic.jpg"
    cv2.imwrite(output_name, img)
    print(f"\nSuccess! Annotated image saved as '{output_name}'")

    print("Press any key on the image window to close the program.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()