from PIL import Image
import os


def convert_image(input_path, output_path, output_format):
    """
    Convert an image from one format to another.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the converted image.
        output_format (str): Desired output image format (e.g., "JPEG", "PNG", "GIF").
    """
    try:
        with Image.open(input_path) as image:
            image.save(output_path, format=output_format)
        print(f"Image converted and saved as {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except OSError as e:
        print(f"Error: Failed to convert the image. {str(e)}")
    except ValueError:
        print(f"Error: Invalid output format '{output_format}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred. {str(e)}")


# Example usage:
input_image_path = "input_image.jpg"
output_image_path = "output_image.gif"
output_image_format = "GIF"

# Resolve full file paths
input_path = os.path.abspath(input_image_path)
output_path = os.path.abspath(output_image_path)

convert_image(input_path, output_path, output_image_format)
