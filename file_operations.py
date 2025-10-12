import os
import shutil
import fnmatch

def list_directory_contents(path):
    """
    List the contents of a directory.

    :param path: Directory path to list contents of.
    :return: List of directory contents.
    :raises ValueError: If the path is not a valid directory.
    """
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")
    return os.listdir(path)

def copy_file(src, dst):
    """
    Copy a file from source to destination.

    :param src: Source file path.
    :param dst: Destination file path.
    :raises ValueError: If the source path is not a valid file.
    """
    if not os.path.isfile(src):
        raise ValueError(f"The source path '{src}' is not a valid file.")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

def move_file(src, dst):
    """
    Move or rename a file from source to destination.

    :param src: Source file path.
    :param dst: Destination file path.
    :raises ValueError: If the source path is not a valid file.
    """
    if not os.path.isfile(src):
        raise ValueError(f"The source path '{src}' is not a valid file.")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)

def delete_path(path):
    """
    Delete a file or directory.

    :param path: Path to the file or directory.
    :raises ValueError: If the path does not exist.
    """
    if not os.path.exists(path):
        raise ValueError(f"The path '{path}' does not exist.")
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)

def check_disk_usage(path):
    """
    Check the disk usage of a directory.

    :param path: Directory path to check disk usage.
    :return: Dictionary with total, used, and free space in bytes.
    :raises ValueError: If the path is not a valid directory.
    """
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")
    total, used, free = shutil.disk_usage(path)
    return {'total': total, 'used': used, 'free': free}

def search_files(directory, pattern):
    """
    Search for files matching a pattern in a directory.

    :param directory: Directory path to search in.
    :param pattern: Pattern to match files.
    :return: List of matching files with their full paths.
    :raises ValueError: If the directory is not valid.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The directory '{directory}' is not valid.")
    return [os.path.join(root, name) for root, _, files in os.walk(directory) for name in fnmatch.filter(files, pattern)]

if __name__ == "__main__":
    # Example usage
    try:
        contents = list_directory_contents('/path/to/directory')
        print("Directory Contents:", contents)
    except Exception as e:
        print(f"Error listing directory contents: {e}")

    try:
        copy_file('/path/to/source/file.txt', '/path/to/destination/file.txt')
        print("File copied successfully.")
    except Exception as e:
        print(f"Error copying file: {e}")

    try:
        move_file('/path/to/source/file.txt', '/path/to/new/location/file.txt')
        print("File moved/renamed successfully.")
    except Exception as e:
        print(f"Error moving/renaming file: {e}")

    try:
        delete_path('/path/to/file_or_directory')
        print("File or directory deleted successfully.")
    except Exception as e:
        print(f"Error deleting file or directory: {e}")

    try:
        usage = check_disk_usage('/path/to/directory')
        print("Disk Usage:", usage)
    except Exception as e:
        print(f"Error checking disk usage: {e}")

    try:
        files = search_files('/path/to/directory', 'pattern*')
        print("Matching Files:", files)
    except Exception as e:
        print(f"Error searching for files: {e}")