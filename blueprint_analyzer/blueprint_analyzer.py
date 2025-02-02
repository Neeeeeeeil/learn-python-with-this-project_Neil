import cv2 as cv
import numpy as np
import os

def load_and_display_image():
    """Prompt user for image path, load and display the image with error handling."""
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp")

    while True:
        image_path = input("Enter the path to the blueprint image (or type 'exit' to quit): ").strip()

        if image_path.lower() == 'exit':
            print("Exiting program.")
            return None

        if not os.path.isfile(image_path):
            print("Error: The provided path is not a valid file. Try again.")
            continue

        if not image_path.lower().endswith(valid_extensions):
            print("Error: Unsupported file type. Use JPG, PNG, BMP, TIFF, or WEBP.")
            continue

        image = cv.imread(image_path)
        if image is None or image.shape[0] == 0 or image.shape[1] == 0:
            print("Error: The image is empty, corrupted, or could not be loaded. Try another file.")
            continue

        cv.imshow("Original Blueprint", image)
        if cv.waitKey(0) & 0xFF == ord('q'):
            cv.destroyAllWindows()
        return image

def preprocess_image(image):
    """Preprocess image for better room detection."""
    grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    inverted = cv.bitwise_not(grayscale)
    _, binary = cv.threshold(inverted, 200, 255, cv.THRESH_BINARY)

    # Close small gaps in walls
    kernel = np.ones((10, 10), np.uint8)
    dilated = cv.dilate(binary, kernel, iterations=2)

    # Remove exterior by flood-filling from the border
    flood_filled = dilated.copy()
    h, w = flood_filled.shape
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(flood_filled, mask, (0, 0), 255)  # Fill exterior starting from top-left corner

    # Invert the flood-filled result to get only interior rooms
    interior_only = cv.bitwise_not(flood_filled)

    cv.imshow("Preprocessed - Walls Closed & Exterior Removed", interior_only)
    if cv.waitKey(0) & 0xFF == ord('q'):
        cv.destroyAllWindows()
    
    return interior_only

def detect_rooms(image, processed_image, min_room_size=5000):
    """Detect and count rooms by flood-filling interior spaces."""
    room_count = 0
    labeled_image = image.copy()
    h, w = processed_image.shape
    mask = np.zeros((h+2, w+2), np.uint8)

    # Iterate through image to flood fill enclosed spaces
    for y in range(h):
        for x in range(w):
            if processed_image[y, x] == 0:  # Interior space
                # Create a new mask for each flood-fill operation
                temp_mask = np.zeros((h+2, w+2), np.uint8)
                
                # Measure the size of the area before filling
                area = cv.floodFill(labeled_image, temp_mask, (x, y), (0, 255, 0))[0]

                if area > min_room_size:  # Apply the minimum room size filter
                    room_count += 1

    if room_count == 0:
        print("Warning: No rooms detected. Adjust image contrast or quality.")

    print(f"Total Number of Rooms: {room_count}")

    cv.imshow("Rooms Detected", labeled_image)
    if cv.waitKey(0) & 0xFF == ord('q'):
        cv.destroyAllWindows()

    return labeled_image, room_count

def main():
    print("Blueprint Analyzer with OpenCV")

    image = load_and_display_image()
    if image is None:
        return

    processed_image = preprocess_image(image)
    detect_rooms(image, processed_image, min_room_size=5000)

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
