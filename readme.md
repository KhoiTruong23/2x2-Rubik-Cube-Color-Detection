
# [Python]2x2 Rubik Cube Color Detection (Only OpenCV and Numpy)
---
### Introduction
Here is my demonstration of the program.
<p align="center">
  <img src="demo/demonstration.gif" width=800><br/>
  <i>Demonstration</i>
</p>

My program is designed to introduce computer vision beginners to fundamental concepts like generating images, working with color channels, and detecting colors.

*Note that the BGR values in the code may need slight adjustment when generating reference colors due to the effects of ambient lighting and the differences between individual Rubik's Cubes.

-----
### How it works
- It captures video from a camera and processes the images to obtain a warped image of each square on the Rubik's Cube.
- It defines color samples for each of the six colors on the Rubik's Cube and converts them to the HSV color space for improved color detection.
- It uses the check function to compare each warped square to the color samples and outputs the color of each square on the image using the output_color function.
- The code runs in a continuous loop to capture and process each frame from the camera in real-time.
