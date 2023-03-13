import os

# Directories containing media files
media_dirs = ["D:\\newtrust", "P:\\Jav", "O:\\Jav", "Q:\\Jav", "R:\\Jav"]

# Target directory for symlinks
link_dir = "C:\\Users\\bing\\Desktop\\link"

# File extensions for media files
media_exts = [".wmv", ".avi", ".mp4", ".mkv"]

# Create the link directory if it doesn't exist
if not os.path.exists(link_dir):
    os.mkdir(link_dir)

# Iterate through media directories
for media_dir in media_dirs:
    # Iterate through files in media directory
    for media_file in os.listdir(media_dir):
        # Check if file has a media file extension
        if os.path.splitext(media_file)[1] in media_exts:
            # Get base name and extension
            base_name, file_ext = os.path.splitext(media_file)
            # Initialize the number to be added to the filename
            number = 0
            # Create symlink in link directory
            while True:
                # Check if a file with the same name already exists
                link_path = os.path.join(link_dir, base_name + "-" + str(number) + file_ext)
                if not os.path.exists(link_path):
                    source_path = os.path.join(media_dir, media_file)
                    os.symlink(source_path, link_path)
                    break
                else:
                    number += 1
