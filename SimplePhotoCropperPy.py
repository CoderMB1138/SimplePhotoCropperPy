import cv2
import os
import sys

def crop_image(image_path, x, y, width, height, output_format="same"):
    # Read the image
    image = cv2.imread(image_path)
    
    # Crop the image
    cropped_image = image[y:y+height, x:x+width]
    
    # Generate output filename dynamically
    output_filename = generate_output_filename(image_path, output_format)
    
    # Save the cropped image
    cv2.imwrite(output_filename, cropped_image)
    
    print("Image cropped and saved successfully as:", output_filename)

def generate_output_filename(input_filename, output_format="same"):
    # Extract filename and extension
    filename, ext = os.path.splitext(input_filename)
    
    # Generate output filename with iteration number
    output_filename = f"{filename}_cropped"
    output_filename += f"_0.{output_format}" if output_format == "same" else f"_0.{output_format}"
    i = 1
    while os.path.exists(output_filename):
        output_filename = f"{filename}_cropped_{i}.{output_format}" if output_format == "same" else f"{filename}_cropped_{i}.{output_format}"
        i += 1
    return output_filename

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python crop_photo.py <input_image_path> <x> <y> <width> <height> [<output_format>]")
        sys.exit(1)
    
    # Parse command-line arguments
    input_image_path = sys.argv[1]
    x, y, width, height = map(int, sys.argv[2:6])
    output_format = sys.argv[6] if len(sys.argv) >= 7 else "same"
    
    # Crop the image
    crop_image(input_image_path, x, y, width, height, output_format)

