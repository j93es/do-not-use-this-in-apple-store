from PIL import Image
import numpy as np

# ASCII characters used to build the output text
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_grayscale(image):
    """Converts the image to grayscale."""
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    """Maps each pixel to an ASCII character based on its intensity."""
    pixels = np.array(image)
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Converts an image to an ASCII art string."""
    # Load the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {image_path}.")
        print(e)
        return

    # Resize image
    image = scale_image(image, new_width)

    # Convert image to grayscale
    image = convert_grayscale(image)

    # Convert pixels to ASCII
    ascii_str = ""
    width, height = image.size
    for y in range(height):
        row_pixels = np.array(image)[y]
        ascii_str += map_pixels_to_ascii(row_pixels) + "\n"

    return ascii_str

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ascii_art.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    ascii_art = image_to_ascii(image_path)

    # Print the ASCII art to terminal
    print(ascii_art)

