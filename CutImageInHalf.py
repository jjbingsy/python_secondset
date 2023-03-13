from PIL import Image
from pathlib import Path

# Define the source directory containing the JPG files
############ WARNING!!!
#source_dir = Path("F:/trusti")

# Loop through all JPG files in the source directory and its subdirectories
for jpg_path in source_dir.glob("**/*.jpg"):
    with Image.open(jpg_path) as img:
        # Calculate the size of the right half of the image
        width, height = img.size
        half_width = width // 2
        right_half_size = (half_width, height)
        
        # Crop the right half of the image
        right_half = img.crop((half_width, 0, width, height))
        
        # Save the right half of the image to the original file path
        right_half.save(jpg_path)
        print (jpg_path)
