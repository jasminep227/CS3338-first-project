# Import the OpenCV library
import cv2

# Load an image from file
image = cv2.imread('example.jpg')

# Display the image in a window
cv2.imshow('Loaded Image', image)

# Wait until a key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()