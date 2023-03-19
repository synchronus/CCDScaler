# CCDScaler
A python tool to scale 12 and 14-bit FITS files to fit into their 16-bit containers

Some Touptek model cameras don't have a firmware-level scalar to extend their 12-bit and 14-bit images to fill the entirety of brightness values available in a 16-bit FITS container. While N.I.N.A. and Astrophotography tool do this automatically, KStars/Ekos does not due to a preference of caution when modifying files after capture, which I respect. In the spirit of that, this tool WILL NOT overwrite original data, instead creating an entirely new folder tree identical to the folder setup of the original files, with each new scaled file having '_m' appended on the filename (indicating "modified").

## Prerequisites
This tool uses the AstroPy and tqdm libraries for both command-line and GUI tools. If either are not installed, you can do so by using PIP

```user@localhost:~$ pip install AstroPy```

```user@localhost:~$ pip install tqdm```


The GUI tool makes use of the TKinter library, which is not ideal but functional.

```user@localhost:~$ pip install tkinter```

## The CMD tool

The CMD tool should just run by calling it from a python prompt

```user@localhost:~$ python scale_pictures.py```

Which will then prompt for a directory path

```Enter the directory path: C:\Users\User1\Pictures\M74\```

followed by a prompt for the scale value

```Enter an integer scale value: 16```

Which will then scale all FITS images in that folder by the number entered. The CMD tool uses multithreading to speed things up tremendously.

TODO: Try/catch for directory misreads


## The GUI Tool
NOTE: This tool is very much early stages and I have not tested every possible use case or issue (i.e., checks for available storage, corrupted FITS handling, etc.)

<img width="170" alt="Screenshot 2023-03-19 125100" src="https://user-images.githubusercontent.com/16050999/226191803-a0911495-47f7-4d84-8bc8-64d60caa6e86.png">

The tool is very simple. You pick a scale factor (from 1 to 32), select a directory containing your FITS files, and the utility goes to work. There is a rudimentary status indicator at the bottom to indicate progress, but it's extremely buggy and rarely works properly until the tool is finished its scaling process. Once done, the tool will display a list of all modified files and their respective locations

<img width="309" alt="Screenshot 2023-03-19 125537" src="https://user-images.githubusercontent.com/16050999/226192103-391de697-8e2a-489d-966a-507da8155e04.png">

At some point, I'd like to change the layout so that instead of asking for a scale factor, it asks for the bit-depth of the camera used, or maybe pull the information from the FITS container of the first light frame. I'd also like to add some kind of progress bar, as this tool can take some time on large batches of files.
