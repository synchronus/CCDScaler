import os
from astropy.io import fits

# Prompt the user to enter a directory path
directory = input("Enter the directory path: ")

# Set the constant to multiply the FITS files by
constant = input("Enter an integer scale value: ")

# Initialize a list to store the modified file names
modified_files = []

# Recursively search through all subdirectories for FITS files
for root, dirs, files in os.walk(directory):
    # Check if any FITS files are present in the current directory
    if any(filename.lower().endswith('.fits') or filename.lower().endswith('.fit') for filename in files):
        # Construct the new root directory called "scaled"
        new_root = os.path.join(directory, "scaled")
        # Replicate the subdirectory structure of the original directory tree
        for dir_name in os.path.relpath(root, directory).split(os.sep):
            new_root = os.path.join(new_root, dir_name)
            os.makedirs(new_root, exist_ok=True)
        # Loop through all the FITS files in the current directory
        for filename in files:
            if filename.lower().endswith('.fits') or filename.lower().endswith('.fit'):
                # Open the FITS file
                with fits.open(os.path.join(root, filename)) as hdul:
                    # Get the data from the FITS file
                    data = hdul[0].data
                    # Multiply the data by the constant
                    data *= constant
                    # Save the modified data back to the FITS file
                    hdul[0].data = data
                    # Construct the new filename with "_m" appended
                    new_filename = filename[:-5] + '_m.fits' if filename.lower().endswith('.fits') else filename[:-4] + '_m.fits'
                    # Save the modified FITS file in the "scaled" directory
                    hdul.writeto(os.path.join(new_root, new_filename), overwrite=True)
                    # Add the new filename to the list of modified files
                    modified_files.append(os.path.join(new_root, new_filename))

# Print a list of the modified files
if modified_files:
    print("The following files were modified:")
    for filename in modified_files:
        print(filename)
else:
    print("No FITS files were found in the specified directory.")
