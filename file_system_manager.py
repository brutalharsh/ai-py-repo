# File: file_system_manager.py

"""
file_system_manager.py

A reusable Python module for file system operations and management with comprehensive error handling.

This module includes functionality for:
- Checking if a file or directory exists
- Creating files and directories
- Reading from and writing to files
- Deleting files and directories
- Listing contents of directories
- Moving and copying files and directories

All functions include comprehensive error handling and follow the PEP 8 style guide.

Example usage:
    import file_system_manager as fsm

    # Check if a file exists
    fsm.file_exists('example.txt')

    # Create a new directory
    fsm.create_directory('new_directory')

    # Write to a file
    fsm.write_to_file('example.txt', 'Hello, World!')

    # Read from a file
    content = fsm.read_from_file('example.txt')

    # Delete a file
    fsm.delete_file('example.txt')

    # List contents of a directory
    files = fsm.list_directory_contents('.')

    # Move a file
    fsm.move('example.txt', 'new_directory/example.txt')

    # Copy a file
    fsm.copy('new_directory/example.txt', 'example_copy.txt')

"""

import os
import shutil


def file_exists(file_path):
    """
    Check if a file exists at the specified path.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    try:
        return os.path.isfile(file_path)
    except Exception as e:
        print(f"Error checking if file exists: {e}")
        return False


def create_directory(directory_path):
    """
    Create a directory at the specified path.

    Parameters:
    directory_path (str): The path to the directory.

    Returns:
    bool: True if the directory was created successfully, False otherwise.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False


def write_to_file(file_path, content):
    """
    Write content to a file.

    Parameters:
    file_path (str): The path to the file.
    content (str): The content to write to the file.

    Returns:
    bool: True if writing to the file was successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def read_from_file(file_path):
    """
    Read content from a file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None


def delete_file(file_path):
    """
    Delete a file at the specified path.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    bool: True if the file was deleted successfully, False otherwise.
    """
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False


def list_directory_contents(directory_path):
    """
    List the contents of a directory.

    Parameters:
    directory_path (str): The path to the directory.

    Returns:
    list: A list of the names of the entries in the directory, or None if an error occurred.
    """
    try:
        return os.listdir(directory_path)
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        return None


def move(src_path, dest_path):
    """
    Move a file or directory to a new location.

    Parameters:
    src_path (str): The source path.
    dest_path (str): The destination path.

    Returns:
    bool: True if the move was successful, False otherwise.
    """
    try:
        shutil.move(src_path, dest_path)
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


def copy(src_path, dest_path):
    """
    Copy a file or directory to a new location.

    Parameters:
    src_path (str): The source path.
    dest_path (str): The destination path.

    Returns:
    bool: True if the copy was successful, False otherwise.
    """
    try:
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False


if __name__ == "__main__":
    import file_system_manager as fsm

    # Example usage:
    
    # Check if a file exists
    print(fsm.file_exists('example.txt'))

    # Create a new directory
    print(fsm.create_directory('new_directory'))

    # Write to a file
    print(fsm.write_to_file('example.txt', 'Hello, World!'))

    # Read from a file
    print(fsm.read_from_file('example.txt'))

    # Delete a file
    print(fsm.delete_file('example.txt'))

    # List contents of a directory
    print(fsm.list_directory_contents('.'))

    # Move a file
    print(fsm.move('example.txt', 'new_directory/example.txt'))

    # Copy a file
    print(fsm.copy('new_directory/example.txt', 'example_copy.txt'))