import cv2
import numpy as np

# We need to calibrate below-mentioned parameters for the camera 
focal_length = 700  # in pixels
baseline = 0.1  # baseline is distance between the two cameras in meters


"""
Now, we need two important function
1. Calulation of distance - this will help when we will observe the disparity in the Video Frames
2. Speed Estimation - after calculting the distance, when we will compare the 
total distance covered in each frame/second, Hence providing us the solution to the same.
"""

# First - Function to calculate distance based on disparity in each image

"""
Distance(m) = (Focal Length * Baseline) / Disparity

Case of no detection or very far object - The disparity is zero, it returns infinity
"""

def calculate_distance(disparity, focal_length, baseline):
    if disparity == 0:
        return float('inf')
    return (focal_length * baseline) / disparity


"""
Speed (m/s)= Change in Distance / Time Elapsed 

"""
# Second - Function to estimate speed based on the total distance covered
def estimate_speed(previous_distance, current_distance, time_elapsed):
    return abs(current_distance - previous_distance) / time_elapsed



# Atlast, The Main function
def track_drone():
    # Initializing the video capture from two cameras (Stereo)
    cap_left = cv2.VideoCapture(0)
    cap_right = cv2.VideoCapture(1)

    previous_distance = None
    previous_time = None

    # StereoBM algorithm for disparity map
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    while True:
        # Capturing the frames from both cameras
        ret_left, frame_left = cap_left.read()
        ret_right, frame_right = cap_right.read()

        if not ret_left or not ret_right:
            print("Error: Unable to capture video")
            break

        # Converting the frames to grayscale as we dont need color in this calculation
        # and this will also save the memory
        gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
        gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

        # Computing the disparity map i.e (stereo vision)
        disparity = stereo.compute(gray_left, gray_right).astype(np.float32) / 16.0
        disparity_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)

        # Calculating the distance 
        mean_disparity = np.mean(disparity)
        distance = calculate_distance(mean_disparity, focal_length, baseline)

        # Now, we need to get the current time
        current_time = cv2.getTickCount() / cv2.getTickFrequency()

        if previous_distance is not None and previous_time is not None:
            # Estimate speed
            time_elapsed = current_time - previous_time
            speed = estimate_speed(previous_distance, distance, time_elapsed)
            print(f"Speed: {speed:.2f} m/s")

        print(f"Distance: {distance:.2f} meters")

        # Updation of previous values
        previous_distance = distance
        previous_time = current_time

        # Displaying the frames and disparity map
        cv2.imshow('Left Camera', frame_left)
        cv2.imshow('Right Camera', frame_right)
        cv2.imshow('Disparity Map', disparity_normalized)

        # Breaking loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap_left.release()
    cap_right.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_drone()
