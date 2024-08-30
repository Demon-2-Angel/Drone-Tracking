## Problem Statement
I need to develop a solution to detect and track a high-speed drone flying towards me. The drone, measuring `1m` in `length` and `0.5m` in `width`, starts from a `distance` of `2500m` with an `altitude` of `1000m` and is approaching you at a `speed` of `50-75 km/h`. My goal is to calculate the distance and speed of the drone in real time using one or more cameras.

## Proposed Solution
The proposed solution involves using a stereo camera setup (two cameras) to capture real-time footage of the drone. 
By analyzing the disparity between the images from the two cameras, the distance to the drone can be calculated. 
Using subsequent frames, the speed of the drone can also be determined. 


## Assumptions 

- Lighting Conditions: The environment is well-lit, allowing the cameras to capture the drone.
- Camera Calibration: The stereo cameras are pre-calibrated, with known intrinsic and extrinsic parameters.
- Background: The background is relatively static, with minimal clutter, ensuring that the drone can be easily isolated in the video frames.
- Processing Power: The system has sufficient processing power to handle real-time video processing and distance calculation.
- No Severe Occlusions: The drone remains visible in the camera's field of view throughout the flight, with no severe occlusions.

## Flowchart of the Proposed Solution
```
Start
|
|---> Initialize stereo camera setup
|
|---> Capture video frames from both cameras
|
|---> Preprocess frames (grayscale conversion, noise reduction)
|
|---> Detect and track a drone in both frames
|
|---> Compute disparity map using stereo vision techniques
|
|---> Calculate the distance of the drone using the disparity map and camera parameters
|
|---> Track drone over time to calculate speed
|
|---> Display/Log distance and speed in real time
|
|---> Stop when the drone reaches the observer
|
End
```

## Diagrams

<p style="text-align: center;">
    <img src="https://github.com/Demon-2-Angel/Drone-Tracking/blob/main/FlowChart/Drone%20Tracking%20Program%20Flow.png" alt="Drone Tracking Program Flow" style="width: 600px; height: 20px; max-width: 50%; height: auto;">
</p>

