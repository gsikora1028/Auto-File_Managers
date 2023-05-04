import os
import time
import glob

def main():
    deleted_files_count = 0
    file_directories = [
        "/Users/gsikora/Downloads/1-trfs",
        "/Users/gsikora/Desktop/GH/Formatted Docs/xls_files_to_delete",
    ]
    days_elapsed = 0.00000001
    seconds = time.time() - (days_elapsed * 24 * 60 * 60)

    for file_directory in file_directories:
        if os.path.isfile(file_directory):
            if seconds >= os.path.getctime(file_directory):
                remove_file(file_directory)
                deleted_files_count += 1
        elif os.path.isdir(file_directory):
            for file_path in glob.glob(f"{file_directory}/**/*", recursive=True):
                if os.path.isfile(file_path) and seconds >= os.path.getctime(file_path):
                    try:
                        remove_file(file_path)
                        deleted_files_count += 1
                    except Exception as e:
                        print(f"Unable to delete {file_path}: {e}")
        else:
            print(f'"{file_directory}" is not found')

    print(f"Total files deleted: {deleted_files_count}")

def remove_file(path):
    try:
        os.remove(path)
        print(f"{path} was removed successfully")
    except Exception as e:
        print(f"Unable to delete {path}: {e}")

if __name__ == '__main__':
    main()
