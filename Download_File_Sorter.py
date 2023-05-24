#Program: Download File Sorter
#Author: Gabriel Sikora
#Creation Date: 5/2/2023
#---------------------------------------------------
import os
import shutil
from pathlib import Path

# Define the folders for different file types
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
    ".gif" : "Images", ".iso" : "Images", ".jpeg" : "Images", ".jpg" : "Images", ".psd" : "Images", ".png" : "Images", ".tiff" : "Images", ".tif" : "Images",
    #MISC
    ".vsd" : "MISC", ".vsdm" : "MISC", ".vsdx" : "MISC", ".vss" : "MISC", ".vssm" : "MISC", ".vst" : "MISC", ".vstm" : "MISC", ".vstx" : "MISC", ".zip" : "MISC", ".step" : "MISC", ".bin" : "MISC", ".bmp" : "MISC", ".exe" : "MISC", 
    #Videos
    ".flv" : "Videos", ".mov" : "Videos", ".mp3" : "Videos", ".mp4" : "Videos", ".mpg" : "Videos", ".vob" : "Video",
    #Webpages
    ".aspx" : "Webpages", ".html" : "Webpages",".htm" : "Webpages",
}

# Loop through the files in the downloads folder
for filename in os.listdir("/Users/gsikora/Downloads"):
    # Check if "_TRF_" is present in the filename
    if "_TRF_" in filename:
        folder = "TRF_Files"  # Specify the folder for TRF files
    else:
        # Get the file extension and corresponding folder
        ext = os.path.splitext(filename)[1].lower()
        folder = file_extension_library.get(ext)

    # If the file extension is in the dictionary, move the file to the corresponding folder
    if folder is not None:
        destination_folder = Path("/Users/gsikora/Desktop/GH/1-DV") / folder
        destination_folder.mkdir(parents=True, exist_ok=True)
        source_path = Path("/Users/gsikora/Downloads") / filename
        destination_path = destination_folder / filename
        shutil.move(str(source_path), str(destination_path))

# define the list of directories where you want to search for files with .xls extension
directories = ['/Users/gsikora/Downloads/Documents', '/Users/gsikora/Desktop']

# define the file extension you want to search for
extension = '.xls'

# define the destination folder where you want to move the files
dest_folder = '/Users/gsikora/Desktop/GH/XLS_delete'

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