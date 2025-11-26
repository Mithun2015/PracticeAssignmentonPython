import os
import sys
import shutil
from datetime import datetime

# Check if correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python backup.py <source_dir> <destination_dir>")
    sys.exit(1)

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

# Validate source directory
if not os.path.isdir(source_dir):
    print(f"Error: Source directory does not exist: {source_dir}")
    sys.exit(1)

# Create destination directory if not exists
if not os.path.isdir(dest_dir):
    try:
        os.makedirs(dest_dir)
        print(f"Destination directory created: {dest_dir}")
    except Exception as e:
        print(f"Error creating destination directory: {e}")
        sys.exit(1)

def get_unique_filename(dest_dir, filename):
    """Return a unique file name if conflict exists."""
    base_name, ext = os.path.splitext(filename)
    dest_path = os.path.join(dest_dir, filename)

    if not os.path.exists(dest_path):
        return dest_path
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{base_name}_{timestamp}{ext}"
    return os.path.join(dest_dir, new_filename)

print(f"Starting backup from {source_dir} to {dest_dir}...\n")

# Copy files
for item in os.listdir(source_dir):
    src_path = os.path.join(source_dir, item)

    if os.path.isfile(src_path):
        try:
            dest_path = get_unique_filename(dest_dir, item)
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {item}")
        except Exception as e:
            print(f"Failed to copy {item}: {e}")

print("\nBackup completed successfully!")
