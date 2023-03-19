# CCDScaler
A python tool to scale 12 and 14-bit FITS files to fit into their 16-bit containers

Some Touptek model cameras don't have a firmware-level scalar to extend their 12-bit and 14-bit images to fill the entirety of brightness values available in a 16-bit FITS container. While N.I.N.A. and Astrophotography tool do this automatically, KStars/Ekos does not due to a preference of caution when modifying files after capture, which I respect. In the spirit of that, this tool WILL NOT overwrite original data, instead creating an entirely new folder tree identical to the folder setup of the original files, with each new scaled file having '_m' appended on the filename (indicating "modified").

## Prerequisites
This tool uses the AstroPy library for both command-line and GUI tools. If AstroPy is not installed, you can do so by using PIP

```user@localhost:~$ pip install AstroPy```

The GUI tool makes use of the TKinter library, which is not ideal but functional.

```user@localhost:~$ pip install tkinter```

## The CMD tool

The CMD tool should just run by calling it from a python prompt

```user@localhost:~$ python scale_pictures.py```

Which will then prompt for a directory path

```Enter the directory path: C:\Users\User1\Pictures\M74\```

followed by a prompt for the scale value

```Enter an integer scale value: 16```

Which will then scale all FITS images in that folder by the number entered. Once done, the prompt will display a list of the locations of all new FITS files that were created.

TODO: Some form of progress indicator, try/catch for mistyped directory paths
