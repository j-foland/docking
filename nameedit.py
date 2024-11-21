import os
from pathlib import Path


# Directory where the output files are located
output_dir = r"C:\Users\folan\Research\Aryl Hydrocarbon\Structures\QTfiles"

# List all files in the output directory
files = os.listdir(output_dir)
print("Files in output directory:", files)

# Process and rename files
for file_name in files:
    if file_name.endswith('.sdf.pdbqt'):
        # Remove '.sdf' and '.pdbqt'
        new_name = file_name.replace('.sdf.pdbqt', '.pdbqt')

        # Split filename on spaces
        parts = new_name.split(' ')

        # Remove the first word if there are multiple parts
        if len(parts) > 1:
            new_name = ' '.join(parts[1:])

        # Full path for old and new files
        old_file = os.path.join(output_dir, file_name)
        new_file = os.path.join(output_dir, new_name)

        # Rename file if the name has changed
        if old_file != new_file:
            os.rename(old_file, new_file)
            print(f"Renamed {file_name} to {new_name}")

print("Renaming complete.")


