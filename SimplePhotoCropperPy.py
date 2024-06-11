import cv2
import os
import sys

def crop_image(image_path, x, y, width, height, output_dir, output_format="same"):
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Failed to load image: {image_path}")
        return
    
    # Crop the image
    cropped_image = image[y:y+height, x:x+width]
    
    # Generate output filename dynamically
    output_filename = generate_output_filename(image_path, output_dir, output_format)
    
    # Save the cropped image
    cv2.imwrite(output_filename, cropped_image)
    
    print("Image cropped and saved successfully as:", output_filename)

def generate_output_filename(input_filename, output_dir, output_format="same"):
    # Extract filename and extension
    filename, ext = os.path.splitext(os.path.basename(input_filename))
    
    # Determine the format for the output file
    if output_format == "same":
        output_format = ext.lstrip(".")  # Use the original extension
    
    # Generate output filename with iteration number
    output_filename = f"{filename}_cropped.{output_format}"
    output_filepath = os.path.join(output_dir, output_filename)
    
    i = 1
    while os.path.exists(output_filepath):
        output_filename = f"{filename}_cropped_{i}.{output_format}"
        output_filepath = os.path.join(output_dir, output_filename)
        i += 1
    
    return output_filepath

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Usage: python crop_photo.py <input_folder> <output_folder> <x> <y> <width> <height> [<output_format>]")
        sys.exit(1)
    
    try:
        # Parse command-line arguments
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        x, y, width, height = map(int, sys.argv[3:7])
        output_format = sys.argv[7] if len(sys.argv) >= 8 else "same"
        
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Process each image file in the input folder
        for filename in os.listdir(input_folder):
            input_image_path = os.path.join(input_folder, filename)
            if os.path.isfile(input_image_path):
                crop_image(input_image_path, x, y, width, height, output_folder, output_format)
    except ValueError as e:
        print(f"Error: {e}")
        print("Ensure that x, y, width, and height are integers and the output format is a string.")

        if os.path.isfile(input_image_path):
            crop_image(input_image_path, x, y, width, height, output_folder, output_format)

