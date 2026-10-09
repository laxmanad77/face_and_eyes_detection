 # Facial Feature Detection and Annotation

This project is a Python-based computer vision script using OpenCV to dynamically detect and annotate facial features in a standard image. It was developed as a Computer Vision Portfolio Project. 

The script automatically scans an input image for human faces and eyes, applying geometric annotations (circles and bounding boxes) and text labels. To ensure cross-platform compatibility and prevent local environment errors, the script automatically downloads the necessary Haar Cascade models directly from the official OpenCV repository.

## Features
*   **Dynamic Facial Detection:** Uses OpenCV's `detectMultiScale` to find faces and eyes regardless of their size or location in the frame.
*   **Automated Model Fetching:** Automatically downloads `haarcascade_frontalface_default.xml` and `haarcascade_eye.xml` if they are not detected in the local directory, preventing the common `!empty()` assertion failure in OpenCV 5.0.0+.
*   **macOS SSL Bypass:** Includes a built-in unverified context wrapper for `urllib` to bypass the `CERTIFICATE_VERIFY_FAILED` error common in macOS Python environments.
*   **Automated Annotation:** 
    *   Draws a green circle around the detected face.
    *   Draws red bounding boxes around the detected eyes.
    *   Tags the detected face with a "this is me" text label.

## Prerequisites
*   Python 3.x
*   OpenCV for Python (`opencv-python`)

Install the required library via pip:

[bash]

pip install opencv-python

## Usage
1. Clone or download this repository to your local machine.

2. Take a clear, frontal photo of yourself.

3. Rename the photo to me.jpg and place it in the exact same directory as the Python script.

4. Run the script:

[Bash]

python portfolio_project.py

1. Press any key while the image window is active to close the program safely.

## Output
The script will display the annotated image in a new graphical window. Upon closing, it will automatically save a copy of the final annotated image to your working directory as annotated_me_dynamic.jpg.

## Troubleshooting
* **No face detected:** Ensure me.jpg is well-lit and your face is not heavily occluded by shadows, hair, or glasses. You can also adjust the scaleFactor or minNeighbors variables in the detectMultiScale function to increase the detection sensitivity.

* **Missing File Error:** If the script crashes immediately, ensure your input image is named exactly me.jpg (check that your OS isn't hiding a double extension like me.jpg.jpg).

## Author
Laxman Adhikari
