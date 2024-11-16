import picamera
from time import sleep

# Initialize the camera
with picamera.PiCamera() as camera:
    # Give the camera some warm-up time
    sleep(2)
    
    # Capture an image
    camera.capture('/home/pi/image.jpg')

print("Image captured and saved as /home/pi/image.jpg")