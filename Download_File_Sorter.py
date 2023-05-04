import os
import shutil
from pathlib import Path

# Define the folders for different file types
folders = {
    ".JPG": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPEG": "Images",
    ".jpeg": "Images",
    ".HEIC": "Images",
    ".heic": "Images",
    ".svg": "Images",
    ".pdf": "1-trfs",
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".pptx": "Documents",
    ".docx": "Documents",
    ".mp4": "Videos",
    ".dmg": "MISC",
    ".btw": "MISC",
    ".zip": "MISC"
}

# Loop through the files in the downloads folder
for filename in os.listdir("/Users/gsikora/Downloads"):
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

folder_path = '/Users/gsikora/Desktop/GH/Formatted Docs'
extension = '.xls'
dest_folder = '/Users/gsikora/Desktop/GH/Formatted Docs/xls_files_to_delete'

def find_files(folder, extension, dest_folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(subdir, file)
                shutil.move(file_path, os.path.join(dest_folder, file))
                # print(f"{file} was moved to xls_files_to_delete folder")

find_files(folder_path, extension, dest_folder)

