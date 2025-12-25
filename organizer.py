import os
import shutil

# Define the target directory (e.g., your messy downloads or project folder)
folder_path = "./my_project_files"

# Create the directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory '{folder_path}' created. Please add some files to it!")

def organize_files():
    """
    Scans the folder and organizes files into subfolders based on their extensions.
    """
    files_count = 0
    
    for filename in os.listdir(folder_path):
        # Full path to the file
        current_file_path = os.path.join(folder_path, filename)

        # Process only files, skip directories
        if os.path.isfile(current_file_path):
            # Extract extension and convert to lowercase
            name, extension = os.path.splitext(filename)
            extension = extension[1:].lower() # Remove the dot (e.g., '.jpg' -> 'jpg')

            if extension:
                # Create a subfolder named after the extension
                target_folder = os.path.join(folder_path, extension)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Move the file to its new home
                shutil.move(current_file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} -> Folder: {extension}")
                files_count += 1

    if files_count > 0:
        print(f"\nSuccess: {files_count} files organized successfully! 🔥")
    else:
        print("\nInfo: No files were found to organize.")

if __name__ == "__main__":
    print("🚀 Starting File Organizer...")
    organize_files()
    print("✨ Task Completed.")