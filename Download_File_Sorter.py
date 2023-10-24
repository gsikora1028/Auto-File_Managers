# ********************************************************************************************
# Program: File Sorter
# Author: Gabe Sikora
# Date: 5/2/2023
# Function: Automatically sort files into specific folders based on file extension/file names
# ********************************************************************************************

import os
import shutil
from pathlib import Path

# Define the folders for different file types with the file extensions
file_extension_library = {
    #Audio
    ".adt" : "Audio", ".adts" : "Audio", ".aac" : "Audio", ".m4a" : "Audio", ".aifc" : "Audio", ".aiff" : "Audio", ".aif" : "Audio", ".avi" : "Audio", ".cda" : "Audio", ".m4a" : "Audio", ".wav" : "Audio",
    #Documents
    ".csv" : "Documents", ".dif" : "Documents", ".doc" : "Documents", ".docm" : "Documents", ".docx" : "Documents", ".dot" : "Documents", ".dotx" : "Documents", ".pdf" : "Documents", ".pot" : "Documents", ".potm" : "Documents", 
    ".potx" : "Documents", ".ppam" : "Documents", ".pps" : "Documents", ".ppsm" : "Documents", ".ppsx" : "Documents", ".ppt" : "Documents", ".pptm" : "Documents", ".pptx" : "Documents", ".wp5" : "Documents", ".wpd" : "Documents", 
    ".xla" : "Documents", ".xlam" : "Documents", ".xll" : "Documents", ".xlm" : "Documents", ".xls" : "Documents", ".xlsm" : "Documents", ".xlsx" : "Documents", ".xlt" : "Documents", ".xltm" : "Documents", ".xltx" : "Documents", 
    ".xps" : "Documents", ".sldm" : "Documents", ".sldx" : "Documents", ".tmp" : "Documents", ".txt" : "Documents",
    #Email
    ".eml" : "Email", ".pst" : "Email",
    #Images
    ".gif" : "Images", ".iso" : "Images", ".jpeg" : "Images", ".jpg" : "Images", ".psd" : "Images", ".png" : "Images", ".tiff" : "Images", ".tif" : "Images", ".heic" : "Images",
    #MISC
    ".vsd" : "MISC", ".vsdm" : "MISC", ".vsdx" : "MISC", ".vss" : "MISC", ".vssm" : "MISC", ".vst" : "MISC", ".vstm" : "MISC", ".vstx" : "MISC", ".zip" : "MISC", ".step" : "MISC", ".bin" : "MISC", ".bmp" : "MISC", ".exe" : "MISC", ".dmg": "MISC",
    #Videos
    ".flv" : "Videos", ".mov" : "Videos", ".mp3" : "Videos", ".mp4" : "Videos", ".mpg" : "Videos", ".vob" : "Video",
    #Webpages
    ".aspx" : "Webpages", ".html" : "Webpages",".htm" : "Webpages",
}

# Loop through the files in the downloads folder
print("\nLooping through Downloads Folder...")
for filename in os.listdir("/Users/gsikora/Downloads"):
    ext = os.path.splitext(filename)[1].lower()
    folder = file_extension_library.get(ext)

    # If the file extension is in the dictionary, move the file to the corresponding folder
    if folder is not None:
        destination_folder = Path("/Users/gsikora/Downloads") / folder
        destination_folder.mkdir(parents=True, exist_ok=True)
        source_path = Path("/Users/gsikora/Downloads") / filename
        destination_path = destination_folder / filename
        shutil.move(str(source_path), str(destination_path))

    # Check if "_TRF_" is present in the filename and move it to the TRF_Files folder
    if "_TRF_" in filename:
        trf_folder = "/Users/gsikora/Desktop/GH/1-DV/TRF_Files"
        trf_destination = Path(trf_folder) / filename
        shutil.move(os.path.join("/Users/gsikora/Downloads/Documents", filename), str(trf_destination))

# Define the list of directories where you want to search for files with .xls extension
directories = ['/Users/gsikora/Downloads/Documents', '/Users/gsikora/Desktop']

# Define the file extension you want to search for
extension = '.xls'

# Define the destination folder where you want to move the files
dest_folder = '/Users/gsikora/Desktop/GH/XLS_delete'

print("Moving .xls files to deletion folder")
# Define a function to find files with the specified extension and move them to the destination folder
def find_xls_files(directories, extension, dest_folder):
    for directory in directories:
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(subdir, file)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"{file} was moved to {dest_folder}.")

# call the find_xls_files function
find_xls_files(directories, extension, dest_folder)

screenshot_folder = "/Users/gsikora/Desktop/Screenshots"
screen_recording_folder = "/Users/gsikora/Desktop/Screen Recordings"

# Function to add screenshots/screen recordings to different screenshots folder
def move_screen_recordings_and_screenshots_to_new_folders(screenshot_folder, screen_recording_folder):
    for filename in os.listdir("/Users/gsikora/Desktop"):
        if "Screenshot" in filename:
            shutil.move(os.path.join("/Users/gsikora/Desktop", filename), str(screenshot_folder))
            print(f"Moved {filename} to {screenshot_folder}")

        if "Screen Recording" in filename:
            shutil.move(os.path.join("/Users/gsikora/Desktop", filename), str(screen_recording_folder))
            print(f"Moved {filename} to {screen_recording_folder}")

# call the screenshot sorting function
move_screen_recordings_and_screenshots_to_new_folders(screenshot_folder, screen_recording_folder)
