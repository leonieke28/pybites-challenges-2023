import os


def count_dirs_and_files(directory="."):
    """Count the number of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """
    num_files = 0
    num_dirs = 0
    for root, dirs, files in os.walk(directory):
        num_files += len(files)
        num_dirs += len(dirs)
    return num_dirs, num_files
