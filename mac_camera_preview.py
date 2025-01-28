import cv2
import os
import sys

# Get the absolute path to the project directory
if getattr(sys, 'frozen', False):
    project_dir = sys._MEIPASS
else:
    project_dir = os.path.abspath(os.path.dirname(__file__))

def get_available_cameras():
    available_cameras = []
    for index in range(10):
        camera = cv2.VideoCapture(index)
        if camera.isOpened():
            available_cameras.append(index)
        camera.release()
    return available_cameras

def start_camera_preview(camera_index=0):
    # Starts the preview for selected camera #
    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        print(f"Error: Could not access camera {camera_index}.")
        return
    print(f"Using camera {camera_index}. Press 'q' to close the preview.")

    while True:
        # Capture frame by frame #
        ret, frame = camera.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Add text to the frame #
        text = "Press 'q' to end preview."
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        font_scale = 0.5
        color = (255, 255, 255)  # White color in BGR
        thickness = 2
        frame = cv2.putText(frame, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

        # Display the resulting frame #
        cv2.imshow('Camera Preview', frame)

        # Press 'q' to exit the preview window #
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera_preview()