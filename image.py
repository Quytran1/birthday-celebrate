from PIL import Image


def resize_image(input_path, output_path, size):
    """
    Resize an image to the specified size.

    Parameters:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        size (tuple): The desired size as a tuple (width, height).
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            # Save the resized image
            img_resized.save(output_path)
            print(f"Image successfully resized and saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")


# Example usage
input_image_path = "D:\BirthdayCelebration\src\images\congai3.jpg"
output_image_path = "D:\BirthdayCelebration\src\images\congai3_resize.jpg"
desired_size = (1920, 1080)  # Width, Height in pixels

resize_image(input_image_path, output_image_path, desired_size)
