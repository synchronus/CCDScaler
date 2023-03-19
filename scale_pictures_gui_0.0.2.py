import os
from astropy.io import fits
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Scale

def get_directory():
    # Get the directory selected by the user
    directory = filedialog.askdirectory()

    # Get the selected scale factor from the slider
    scale_factor = scale.get()

    # Update the selected_folder_label widget with the selected folder
    selected_folder_label.config(text=directory)

    return directory

def run_scaling():
    # Get the selected folder and scale factor
    directory = selected_folder_label.cget("text")
    

    # Update the status_label widget to indicate the scaling process has started
    status_label.config(text="Scaling images...")
    
    # Scale the images in the selected folder
    scale_images(directory)

    # Update the status_label widget to indicate the scaling process has finished
    status_label.config(text="Finished scaling images.")

def scale_images(directory):
    

    # Initialize a list to store the modified file names
    modified_files = []
    scale_factor = scale.get()

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
                        # Multiply the data by the scale factor
                        data *= scale_factor
                        # Save the modified data back to the FITS file
                        hdul[0].data = data
                        # Construct the new filename with "_m" appended
                        new_filename = filename[:-5] + '_m.fits' if filename.lower().endswith('.fits') else filename[:-4] + '_m.fits'
                        # Save the modified FITS file in the "scaled" directory
                        hdul.writeto(os.path.join(new_root, new_filename), overwrite=True)
                        # Add the new filename to the list of modified files
                        modified_files.append(os.path.join(new_root, new_filename))
    
    # Print a message box with a list of the modified files
    if modified_files:
        modified_files_text = "\n".join(modified_files)
        msg = f"The following files were modified:\n{modified_files_text}"
    else:
        msg = "No FITS files were found in the specified directory."
    messagebox.showinfo(title="FITS Image Multiplier", message=msg)

# Create a Tkinter root window and add a button to run the utility
root = tk.Tk()
root.title("FITS Image Multiplier")
# Add a label for the scale factor
scale_label = tk.Label(root, text="Scale Factor:")
scale_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

# Add a scale widget for selecting the scale factor
scale = Scale(root, from_=1, to=32, resolution=1, orient=tk.HORIZONTAL)
scale.set(16)
scale.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Add a button to select a folder
folder_button = tk.Button(root, text="Select Folder", command=get_directory)
folder_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Add a button to run the scaling function
run_button = tk.Button(root, text="Run", command=run_scaling)
run_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# Add a label to display the status of the scaling process
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

#Add a label to display selected directory
selected_folder_label = tk.Label(root, text="")
selected_folder_label.grid(row=3,column=1, padx=10, pady=10, sticky=tk.E)

root.mainloop()
