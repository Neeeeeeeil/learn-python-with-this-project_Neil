import cv2
import numpy as np

def load_and_display_image(image_path):
    """Load an image and display it."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image. Please check the file path.")
        return None
    
    cv2.imshow("Original Blueprint", image)
    cv2.waitKey(0)
    return image

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Blueprint", grayscale)
    cv2.waitKey(0)
    return grayscale

def detect_edges(image):
    """Apply Canny Edge Detection to an image."""
    edges = cv2.Canny(image, 50, 150)
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    return edges

def find_and_draw_contours(image, edges):
    """Find contours in an image and draw them on the original image."""
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a copy of the original image to draw contours
    contoured_image = image.copy()
    
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 100:  # Filter out small contours
            cv2.drawContours(contoured_image, [contour], -1, (0, 255, 0), 2)
            print(f"Contour {i}: Area = {area:.2f} square pixels")

    cv2.imshow("Outlined Blueprint", contoured_image)
    cv2.waitKey(0)
    return contoured_image, contours

def main():
    print("Blueprint Analyzer with OpenCV")
    image_path = input("Enter the path to the blueprint image: ")

    # Load and display the image
    image = load_and_display_image(image_path)
    if image is None:
        return

    # Convert to grayscale
    grayscale_image = convert_to_grayscale(image)

    # Detect edges
    edges = detect_edges(grayscale_image)

    # Find and draw contours
    find_and_draw_contours(image, edges)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
