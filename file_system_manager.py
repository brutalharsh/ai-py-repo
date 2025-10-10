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
from pathlib import Path
from typing import Union, List, Optional

def file_exists(file_path: Union[str, Path]) -> bool:
    """
    Check if a file exists at the specified path.

    Parameters:
    file_path (Union[str, Path]): The path to the file.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    return Path(file_path).is_file()


def create_directory(directory_path: Union[str, Path]) -> bool:
    """
    Create a directory at the specified path.

    Parameters:
    directory_path (Union[str, Path]): The path to the directory.

    Returns:
    bool: True if the directory was created successfully, False otherwise.
    """
    try:
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False


def write_to_file(file_path: Union[str, Path], content: str) -> bool:
    """
    Write content to a file.

    Parameters:
    file_path (Union[str, Path]): The path to the file.
    content (str): The content to write to the file.

    Returns:
    bool: True if writing to the file was successful, False otherwise.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def read_from_file(file_path: Union[str, Path]) -> Optional[str]:
    """
    Read content from a file.

    Parameters:
    file_path (Union[str, Path]): The path to the file.

    Returns:
    Optional[str]: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None


def delete_file(file_path: Union[str, Path]) -> bool:
    """
    Delete a file at the specified path.

    Parameters:
    file_path (Union[str, Path]): The path to the file.

    Returns:
    bool: True if the file was deleted successfully, False otherwise.
    """
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        print(f"Error deleting file: {file_path} not found")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False


def list_directory_contents(directory_path: Union[str, Path]) -> Optional[List[str]]:
    """
    List the contents of a directory.

    Parameters:
    directory_path (Union[str, Path]): The path to the directory.

    Returns:
    Optional[List[str]]: A list of the names of the entries in the directory, or None if an error occurred.
    """
    try:
        return os.listdir(directory_path)
    except FileNotFoundError:
        print(f"Error listing directory contents: {directory_path} not found")
        return None
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        return None


def move(src_path: Union[str, Path], dest_path: Union[str, Path]) -> bool:
    """
    Move a file or directory to a new location.

    Parameters:
    src_path (Union[str, Path]): The source path.
    dest_path (Union[str, Path]): The destination path.

    Returns:
    bool: True if the move was successful, False otherwise.
    """
    try:
        shutil.move(src_path, dest_path)
        return True
    except FileNotFoundError:
        print(f"Error moving: {src_path} not found")
        return False
    except Exception as e:
        print(f"Error moving: {e}")
        return False


def copy(src_path: Union[str, Path], dest_path: Union[str, Path]) -> bool:
    """
    Copy a file or directory to a new location.

    Parameters:
    src_path (Union[str, Path]): The source path.
    dest_path (Union[str, Path]): The destination path.

    Returns:
    bool: True if the copy was successful, False otherwise.
    """
    try:
        if Path(src_path).is_dir():
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
        return True
    except FileExistsError:
        print(f"Error copying: {dest_path} already exists")
        return False
    except FileNotFoundError:
        print(f"Error copying: {src_path} not found")
        return False
    except Exception as e:
        print(f"Error copying: {e}")
        return False


def directory_exists(directory_path: Union[str, Path]) -> bool:
    """
    Check if a directory exists at the specified path.

    Parameters:
    directory_path (Union[str, Path]): The path to the directory.

    Returns:
    bool: True if the directory exists, False otherwise.
    """
    return Path(directory_path).is_dir()


def delete_directory(directory_path: Union[str, Path]) -> bool:
    """
    Delete a directory at the specified path.

    Parameters:
    directory_path (Union[str, Path]): The path to the directory.

    Returns:
    bool: True if the directory was deleted successfully, False otherwise.
    """
    try:
        shutil.rmtree(directory_path)
        return True
    except FileNotFoundError:
        print(f"Error deleting directory: {directory_path} not found")
        return False
    except Exception as e:
        print(f"Error deleting directory: {e}")
        return False


def append_to_file(file_path: Union[str, Path], content: str) -> bool:
    """
    Append content to a file.

    Parameters:
    file_path (Union[str, Path]): The path to the file.
    content (str): The content to append to the file.

    Returns:
    bool: True if appending to the file was successful, False otherwise.
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False


def get_file_size(file_path: Union[str, Path]) -> Optional[int]:
    """
    Get the size of a file in bytes.

    Parameters:
    file_path (Union[str, Path]): The path to the file.

    Returns:
    Optional[int]: The size of the file in bytes, or None if an error occurred.
    """
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error getting file size: {e}")
        return None


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

    # Check if a directory exists
    print(fsm.directory_exists('new_directory'))

    # Delete a directory
    print(fsm.delete_directory('new_directory'))

    # Append to a file
    print(fsm.append_to_file('example.txt', 'Append this text.'))

    # Get file size
    print(fsm.get_file_size('example.txt'))