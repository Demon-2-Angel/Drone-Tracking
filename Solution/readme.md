# Drone Tracking System

This project involves real-time detection and tracking of a high-speed drone using stereo vision. The system uses two cameras to capture video frames, compute the disparity map, and estimate the drone's distance and speed.

## Features

- **Real-time tracking**: Uses two cameras to track the drone's movement.
- **Distance calculation**: Estimates the distance of the drone from the cameras.
- **Speed estimation**: Calculates the speed of the drone based on its movement.

## Requirements

- **Python**: Make sure Python is installed on your system.
- **OpenCV**: Install OpenCV for image processing and computer vision.

## Installation

1. **Install Dependencies**: Install the required Python packages using pip:
   ```bash
   pip install opencv-python

3. Prepare Cameras: Connect two USB cameras to your computer. The cameras should be recognized as device indices 0 and 1 by OpenCV.


## Code Details

### Overview

The script performs the following steps:
1. **Initialize Cameras**: Captures video from two cameras (left and right).
2. **Preprocess Frames**: Converts video frames to grayscale.
3. **Compute Disparity Map**: Uses the Stereo Block Matching algorithm to compute the disparity between the left and right images.
4. **Calculate Distance**: Calculates the distance of the drone using the disparity map.
5. **Estimate Speed**: Estimates the speed of the drone based on changes in distance over time.
6. **Display Results**: Shows video feeds and the disparity map, and prints the distance and speed in real-time.

### Key Functions

- **`calculate_distance(disparity, focal_length, baseline)`**:
  - Calculates the distance to the drone based on the disparity value, focal length, and baseline.
  - Formula: \(\text{Distance} = \frac{\text{Focal Length} \times \text{Baseline}}{\text{Disparity}}\)

- **`estimate_speed(previous_distance, current_distance, time_elapsed)`**:
  - Estimates the speed of the drone based on the change in distance over time.
  - Formula: \(\text{Speed} = \frac{\text{Change in Distance}}{\text{Time Elapsed}}\)

- **`track_drone()`**:
  - Main function that initializes camera capture, processes frames, computes disparity, calculates distance, estimates speed, and displays the results.

### Code Walkthrough

1. **Initialize Video Capture**
   ```
   cap_left = cv2.VideoCapture(0)
   cap_right = cv2.VideoCapture(1)
   ```

Opens video capture for the left and right cameras.

2. Capture Frames

    ```
    ret_left, frame_left = cap_left.read()
    ret_right, frame_right = cap_right.read()
    ```

Captures frames from both cameras.

3. Convert to Grayscale

    ```
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)
    ```

Converts frames to grayscale for disparity computation.

4. Compute Disparity Map

    ```
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(gray_left, gray_right).astype(np.float32) / 16.0
    ```

Computes the disparity map using the Stereo Block Matching algorithm.

5. Calculate Distance

    ```
    mean_disparity = np.mean(disparity)
    distance = calculate_distance(mean_disparity, focal_length, baseline)
    ```

Calculates the distance to the drone using the mean disparity.

6. Estimate Speed

    ```
    current_time = cv2.getTickCount() / cv2.getTickFrequency()
    if previous_distance is not None and previous_time is not None:
        time_elapsed = current_time - previous_time
        speed = estimate_speed(previous_distance, distance, time_elapsed)
    ```

Estimates the speed based on distance change over time.

7. Display Results
    ```
    cv2.imshow('Left Camera', frame_left)
    cv2.imshow('Right Camera', frame_right)
    cv2.imshow('Disparity Map', disparity_normalized)
    ```

Displays the video feeds and disparity map.


## Troubleshooting

1. No Camera Feed: Ensure that both cameras are connected and recognized by OpenCV. Check the camera indices (`0` and `1`) in the code and adjust if necessary.
2. Disparity Map Issues: If the disparity map appears incorrect, adjust the parameters for the StereoBM algorithm (`numDisparities` and `blockSize`).
3. Distance Calculation: Verify the focal_length and baseline values. You may need to calibrate your cameras to get accurate measurements.

## License
This project is licensed under the MIT License.


### Notes:

- **Adjust Focal Length and Baseline**: The `focal_length` and `baseline` constants should be calibrated for your specific camera setup. 
- **Camera Calibration**: For a more accurate system, consider adding instructions for camera calibration if your setup requires it.
- **License and Contact**: Customize the license and contact sections according to your preferences.

