

import os
import shutil
from datetime import datetime, timedelta

# Get the current date
now = datetime.now()

# Path of the download folder
download_folder = 'C:\\Users\\User\\Downloads'

# Path of the to-delete folder
to_delete_folder = 'C:\\Users\\User\\Downloads\\to-delete'

# Go through the download folder
for file in os.listdir(download_folder):
    # Get the path of the file
    file_path = os.path.join(download_folder, file)
    # Get the modification time of the file
    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
    # Calculate the difference between current date and modification time of the file
    diff = now - mtime
    # If the difference is greater than 30 days
    if diff.days > 10:
        # Move the file to the to-delete folder
        shutil.move(file_path, to_delete_folder)