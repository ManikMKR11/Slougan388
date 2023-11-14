import os
import shutil

def copy_jpeg_to_another_folder(source_folder, destination_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Iterate through each file
    for file in files:
        # Check if the file has a .jpeg extension
        if file.lower().endswith(".jpeg"):
            # Create the source and destination paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Copy the file to the destination folder
            shutil.copyfile(source_path, destination_path)
            print(f"Copied: {file} to {destination_path}")

# Specify your source and destination folders
source_folder_path = r'C:\Users\RanaUniverse\Desktop\111\SoulGen_ Free AI Image Generator to Create Art from Text Online_files'
destination_folder_path = r'C:\Users\RanaUniverse\Desktop\111'

# Call the function to copy files
copy_jpeg_to_another_folder(source_folder_path, destination_folder_path)















# import os

# def rename_jpg_to_jpeg(folder_path):
#     files = os.listdir(folder_path)
    
#     for file in files:
#         if file.lower().endswith(".jpg"):
#             new_name = os.path.join(folder_path, file.lower().replace(".jpg", ".jpeg"))
#             os.rename(os.path.join(folder_path, file), new_name)
#             print(f"Renamed: {file} to {new_name}")

# folder_path = r'C:\Users\RanaUniverse\Desktop\111'
# rename_jpg_to_jpeg(folder_path)
