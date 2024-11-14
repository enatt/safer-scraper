import re
import os

def file_parser(f_path):
    """
    Function to help read in all of the .jpg files from a directory

    Args:
        f_path(str): (relative) path for folder we're reading from (e.g., "./safer")

    Returns (list): a list of file names
    """
    # Get all files in t
    dir_list = sorted(os.listdir(f_path))
    
    # Re-sorting into the original file order
    filenames_as_tuples = [(f, re.findall(r'\d+',f)) for f in dir_list]
    ordered_filenames = sorted(filenames_as_tuples, key=lambda x: int(x[1][-1]))

    root = f_path[2:] + "/"
    file_names = [root+k for k,v in ordered_filenames]
    return file_names
