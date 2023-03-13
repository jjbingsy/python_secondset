from bs4 import BeautifulSoup
from pathlib import Path
import re
import shutil

def copy_movie_images(source_dir, pics_dir, dest_dir):
    # Define source, pictures, and destination paths as Path objects
    source_path = Path(source_dir)
    pics_path = Path(pics_dir)
    dest_path = Path(dest_dir)
    
    # Define an empty set to keep track of copied file names
    copied_files = set()
    
    # Loop through all HTML files in the source directory
    for html_path in source_path.glob("*.html"):
        # Open the HTML file and parse it with Beautiful Soup
        with open (html_path, 'r', encoding="UTF-8") as requested:
            soup = BeautifulSoup (requested, "lxml")

            # Find all elements with class "findMovies"
            movie_elems = soup.find_all("a", class_="text-secondary group-hover:text-primary")
            
            
            for movie_elem in movie_elems:
                # Extract the value of the "src" attribute, which should contain the image file name
                img_src = extract_alphabets_and_numbers(str(movie_elem.string).strip()) + ".jpg"
                print (img_src)
                # If the image file has already been copied, skip it
                if img_src in copied_files:
                    continue
                # Construct the full path to the image file using the pictures directory
                img_path = pics_path / img_src
                # Construct the full path to the destination file using the destination directory
                dest_file_path = dest_path / img_src
                # Copy the image file to the destination directory
                if img_path.exists():
                    shutil.copy(img_path, dest_file_path)
                    # Add the file name to the set of copied file names
                    copied_files.add(img_src)
    
    # Convert the set of copied file names to a list and return it
    return list(copied_files)




def extract_alphabets_and_numbers(string):
    # Search for the first set of alphabet characters and numeric characters
    alphabets = re.search(r'[A-Za-z]+', string)
    numbers = re.search(r'\d+', string)
    
    # Check if both alphabets and numbers are found
    if alphabets and numbers:
        # Create the new string with alphabets, dash, and numbers
        new_string = alphabets.group() + '-' + numbers.group()
        return new_string
    else:
        # Return an empty string if either alphabets or numbers are not found
        return ''

# mypath = "D:/htmlsource/Idols/A.Miho-Tono/10.html"


# with open (mypath, 'r', encoding="UTF-8") as requested:
#     soup = BeautifulSoup (requested, "lxml")

# j = soup.find_all("a", class_="text-secondary group-hover:text-primary")
# for i in j:
#     movie_id = extract_alphabets_and_numbers(str(i.string).strip())


#copy_movie_images ("D:\htmlsource\Idols", "F:/data/trusti" , "F:/dumpidol")
pics_dir = Path("F:/trusti")
for source_dir in Path("F:/data/idols").glob("*"):
    if source_dir.is_dir():
        dest_dir = Path("F:/runner1/Idols") / source_dir.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        copied_files = copy_movie_images(source_dir, pics_dir, dest_dir)
        print(f"Copied {len(copied_files)} files to {dest_dir}")

for source_dir in Path("F:/data/Series").glob("*"):
    if source_dir.is_dir():
        dest_dir = Path("F:/runner1/Series") / source_dir.name
        dest_dir.mkdir(parents=True, exist_ok=True)
        copied_files = copy_movie_images(source_dir, pics_dir, dest_dir)
        print(f"Copied {len(copied_files)} files to {dest_dir}")


