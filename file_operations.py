import os
import shutil
import fnmatch


def list_directory_contents(path):
    """
    List the contents of a directory.

    :param path: Directory path to list contents of.
    :return: List of directory contents.
    """
    if not os.path.isdir(path):
        raise ValueError(f"The path {path} is not a valid directory.")
    return os.listdir(path)


def copy_file(src, dst):
    """
    Copy a file from source to destination.

    :param src: Source file path.
    :param dst: Destination file path.
    """
    if not os.path.isfile(src):
        raise ValueError(f"The source path {src} is not a valid file.")
    shutil.copy(src, dst)


def move_file(src, dst):
    """
    Move or rename a file from source to destination.

    :param src: Source file path.
    :param dst: Destination file path.
    """
    if not os.path.isfile(src):
        raise ValueError(f"The source path {src} is not a valid file.")
    shutil.move(src, dst)


def delete_path(path):
    """
    Delete a file or directory.

    :param path: Path to the file or directory.
    """
    if not os.path.exists(path):
        raise ValueError(f"The path {path} does not exist.")
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


def check_disk_usage(path):
    """
    Check the disk usage of a directory.

    :param path: Directory path to check disk usage.
    :return: Disk usage statistics.
    """
    if not os.path.isdir(path):
        raise ValueError(f"The path {path} is not a valid directory.")
    total, used, free = shutil.disk_usage(path)
    return {'total': total, 'used': used, 'free': free}


def search_files(directory, pattern):
    """
    Search for files matching a pattern in a directory.

    :param directory: Directory path to search in.
    :param pattern: Pattern to match files.
    :return: List of matching files.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} is not valid.")
    return [os.path.join(root, name) for root, _, files in os.walk(directory) for name in fnmatch.filter(files, pattern)]


if __name__ == "__main__":
    # Example usage

    # List directory contents
    try:
        contents = list_directory_contents('/path/to/directory')
        print(contents)
    except Exception as e:
        print(f"Error: {e}")

    # Copy a file
    try:
        copy_file('/path/to/source/file.txt', '/path/to/destination/file.txt')
    except Exception as e:
        print(f"Error: {e}")

    # Move or rename a file
    try:
        move_file('/path/to/source/file.txt', '/path/to/new/location/file.txt')
    except Exception as e:
        print(f"Error: {e}")

    # Delete a file or directory
    try:
        delete_path('/path/to/file_or_directory')
    except Exception as e:
        print(f"Error: {e}")

    # Check disk usage
    try:
        usage = check_disk_usage('/path/to/directory')
        print(usage)
    except Exception as e:
        print(f"Error: {e}")

    # Search for files
    try:
        files = search_files('/path/to/directory', 'pattern*')
        print(files)
    except Exception as e:
        print(f"Error: {e}")