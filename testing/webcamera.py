import cv2

sizew = 376
sizeh = 376

def main():
    # Open the default camera (usually the first one)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Get the dimensions of the frame
        height, width, _ = frame.shape

        # Calculate the starting point for the middle 400 pixels
        start_x = (width - sizew) // 2
        start_y = (height - sizeh) // 2

        # Extract the middle 400x400 pixels
        cropped_frame = frame[start_y:start_y + sizeh, start_x:start_x + sizew]

        # Display the cropped frame
        cv2.imshow("Live Feed", cropped_frame)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
