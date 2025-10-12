from PIL import Image
import os

def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    """
    Resize an image to the given width and height.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        width (int): The desired width of the resized image.
        height (int): The desired height of the resized image.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the width or height is not positive.

    Example:
        resize_image("input.jpg", "output.jpg", 800, 600)
    """
    # Check if input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"No such file: '{input_path}'")
    
    # Check if width and height are positive
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers")

    # Open the input image
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((width, height))
        # Save the resized image to the output path
        resized_img.save(output_path)

if __name__ == "__main__":
    # Example usage
    try:
        resize_image("input.jpg", "output.jpg", 800, 600)
        print("Image resized successfully.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")