import cv2
import time

def capture_and_crop_image():
    '''
    
    Take a picture from webcam 0 and resize to center 400 by 400 pixels 
    
    '''
    camera_index=0
    image_path="image.jpg" 
    crop_size=(360, 360)
    # Open the webcam
    cap = cv2.VideoCapture(camera_index)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Wait for 5 seconds
    print("Waiting for 1 second before capturing...")
    time.sleep(1)

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        cap.release()
        return

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the cropping region
    start_row = int((height - crop_size[0]) / 2)
    start_col = int((width - crop_size[1]) / 2)

    # Crop the image to the specified size
    frame_cropped = frame[start_row:start_row + crop_size[0], start_col:start_col + crop_size[1]]

    # Save the cropped frame as an image
    cv2.imwrite(image_path, frame_cropped)

    # Release the webcam
    cap.release()

    print(f"Image captured, center-cropped to {crop_size}, and saved as {image_path}")

if __name__ == "__main__":
    # Specify the index of the webcam (default is 0, which usually represents the built-in webcam)
    webcam_index = 0

    # Specify the path where you want to save the captured and cropped image
    save_path = "image.jpg"

    # Specify the desired crop size
    crop_size = (410, 410)

    # Capture the image and center-crop it
    capture_and_crop_image()
