import os
import shutil
import astropy.io.fits as fits
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def scale_fits_file(args):
    filename, root, output_root, scale_value = args
    if filename.endswith('.fits') or filename.endswith('.fit'):
        # Open the input file
        with fits.open(os.path.join(root, filename)) as hdul:
            # Scale the data
            hdul[0].data *= scale_value

            # Create the output filename with "_m" appended to the stem
            filename_parts = os.path.splitext(filename)
            output_filename = os.path.join(output_root, filename_parts[0] + "_m" + filename_parts[1])

            # Save the scaled data to a new file in the output directory
            hdul.writeto(output_filename, overwrite=True)

def scale_fits_files(scale_value, folder_path):
    # Define the output directory path
    output_folder_path = os.path.join(os.path.dirname(folder_path), "scaled")

    # Loop over all files and directories within the input folder
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        # Create the corresponding output directory within the output folder
        output_root = os.path.join(output_folder_path, os.path.relpath(root, folder_path))
        os.makedirs(output_root, exist_ok=True)

        # Collect all FITS files in the current directory
        for filename in files:
            file_list.append((filename, root, output_root, scale_value))

    # Scale the FITS files using multiple processes
    with Pool(processes=cpu_count()) as pool:
        list(tqdm(pool.imap_unordered(scale_fits_file, file_list), total=len(file_list), desc="Scaling files"))

if __name__ == '__main__':
    # Prompt the user for the scale value and folder location
    scale_value = int(input("Enter scale integer value: "))
    folder_path = input("Enter folder location: ")

    scale_fits_files(scale_value, folder_path)

