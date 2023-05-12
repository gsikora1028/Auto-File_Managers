import os
import shutil
from pathlib import Path
import datetime
import time

# Define the folders for different file types
folders = {
    # Images
    ".JPG": "Images", ".png": "Images", ".jpg": "Images", ".JPEG": "Images", 
    ".jpeg": "Images", ".HEIC": "Images",".heic": "Images", ".svg": "Images",
    
    # Documents
    ".xlsx": "Documents", ".xls": "Documents", ".pptx": "Documents", 
    ".docx": "Documents", ".pdf": "Documents",
    
    # Videos
    ".mp4": "Videos",
    
    # MISC
    ".dmg": "MISC", ".btw": "MISC", ".zip": "MISC"
}

# Loop through the files in the downloads folder
for filename in os.listdir("/Users/gsikora/Downloads"):
    # Check if "_TRF_" is present in the filename
    if "_TRF_" in filename:
        folder = "TRF_Files"  # Specify the folder for TRF files
    else:
        # Get the file extension and corresponding folder
        ext = os.path.splitext(filename)[1]
        folder = folders.get(ext)

    # If the file extension is in the dictionary, move the file to the corresponding folder
    if folder is not None:
        destination_folder = Path("/Users/gsikora/Downloads") / folder
        destination_folder.mkdir(parents=True, exist_ok=True)
        source_path = Path("/Users/gsikora/Downloads") / filename
        destination_path = destination_folder / filename
        shutil.move(str(source_path), str(destination_path))


# define the list of directories where you want to search for files with .xls extension
directories = ['/Users/gsikora/Downloads/Documents', '/Users/gsikora/Desktop']

# define the file extension you want to search for
extension = '.xls'

# define the destination folder where you want to move the files
dest_folder = '/Users/gsikora/Desktop/XLS_delete'

# define a function to find files with the specified extension and move them to the destination folder
def find_files(directories, extension, dest_folder):
    for directory in directories:
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(subdir, file)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"{file} was moved to {dest_folder}.")

# call the find_files function
find_files(directories, extension, dest_folder)

# # specify the directory where the new folder should be created
# directory = "/path/to/directory"

# # get the current time and date
# now = datetime.datetime.now()

# # check if the current time is 8am
# while now.hour != 8:
#     time.sleep(60) # wait 60 seconds and check again
#     now = datetime.datetime.now()

# # create a new folder with the current date as the name
# folder_name = now.strftime("%m.%d-%Y")
# folder_path = os.path.join(directory, folder_name)
# os.mkdir(folder_path)

# print(f"New folder '{folder_name}' created at {now}")
