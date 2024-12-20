# from PIL import Image


# def resize_image(input_path, output_path, size):
#     """
#     Resize an image to the specified size.

#     Parameters:
#         input_path (str): Path to the input image file.
#         output_path (str): Path to save the resized image.
#         size (tuple): The desired size as a tuple (width, height).
#     """
#     try:
#         # Open the image file
#         with Image.open(input_path) as img:
#             # Resize the image
#             img_resized = img.resize(size, Image.Resampling.LANCZOS)
#             # Save the resized image
#             img_resized.save(output_path)
#             print(f"Image successfully resized and saved to {output_path}")
#     except Exception as e:
#         print(f"Error resizing image: {e}")


# # Example usage
# input_image_path = "D:/birthday-web/src/images/congai4-removebg-preview.png"
# output_image_path = "D:/birthday-web/src/images/congai4-removebg-preview.png"
# desired_size = (200, 200)  # Width, Height in pixels

# resize_image(input_image_path, output_image_path, desired_size)

from PIL import Image


def mirror_image(input_path, output_path):
    """
    Create a mirrored version of an image (horizontal flip).

    Parameters:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the mirrored image.
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Mirror the image (horizontal flip)
            mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            # Save the mirrored image
            mirrored_img.save(output_path)
            print(f"Mirrored image successfully saved to {output_path}")
    except Exception as e:
        print(f"Error mirroring image: {e}")


# Example usage
input_image_path = "D:/birthday-web/src/images/congai4-removebg-preview.png"
output_image_path = "D:/birthday-web/src/images/congai4-removebg-preview_op.png"

mirror_image(input_image_path, output_image_path)
