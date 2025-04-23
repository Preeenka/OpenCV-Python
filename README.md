OpenCV-Python Color and Shape Detection Project

This project demonstrates the use of OpenCV and Python for detecting colors and shapes from a live video stream. The program captures the video using a webcam, processes each frame to identify specific colors, and also recognizes basic shapes (circle, rectangle, and triangle) based on contours.

Features:

Color Detection: Detects specific colors in real-time using HSV color space.
Shape Recognition: Identifies and classifies shapes like circles, rectangles, and triangles based on contour analysis.
Real-time Display: The processed video with detected shapes and colors is displayed on the screen.
Technologies Used:

OpenCV: For computer vision tasks like color detection, shape recognition, and video processing.
Python: The programming language used for implementing the project.
Numpy: For handling image arrays and performing operations like masking.
Requirements:

Python 3.x (Recommended version: 3.7 or higher)
OpenCV: Install via pip install opencv-python
Numpy: Install via pip install numpy
Optional:
Virtual Environment (recommended to manage dependencies):
python -m venv venv
source venv/bin/activate (for macOS/Linux)
venv\Scripts\activate (for Windows)
Installation Instructions:

Clone the repository:
git clone https://github.com/Preeenka/OpenCV-Python.git
cd OpenCV-Python
Install dependencies:
pip install -r requirements.txt
Run the project:
python origin.py
Use the program:
The program will open a webcam feed and start processing it.
It will detect the colors defined in the myColors list and draw the corresponding shapes on the video feed.
Press q to exit the program.
Code Walkthrough:

1. Color Detection:
The program uses the HSV (Hue, Saturation, Value) color space for detecting specific colors in the live video. The colors are defined in the myColors array with lower and upper HSV values. The program processes the frame, applies a mask for each color, and detects contours.

2. Shape Detection:
After detecting the colors, the program detects the shapes by analyzing the contours of each detected object. The shapes are identified as:

Circle: Detected if the contour has no straight edges.
Rectangle: Detected if there are 4 vertices.
Triangle: Detected if there are 3 vertices.
3. Drawing on Canvas:
Once a shape is detected, the program draws a circle around it on the frame using the corresponding color.