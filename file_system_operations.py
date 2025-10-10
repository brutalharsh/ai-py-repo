import os
import shutil
from typing import List, Optional

class FileSystemTool:
    """
    A class to provide various file system operations.
    """

    @staticmethod
    def list_directory_contents(path: str) -> Optional[List[str]]:
        """
        List the contents of the specified directory.

        :param path: The path to the directory to list contents of.
        :return: List of directory contents or None if an error occurs.
        """
        if not os.path.isdir(path):
            print(f"Error: {path} is not a valid directory.")
            return None
        try:
            return os.listdir(path)
        except OSError as e:
            print(f"Error listing directory contents: {e}")
            return None

    @staticmethod
    def create_file(path: str) -> None:
        """
        Create a new file at the specified path.

        :param path: The path where the new file should be created.
        """
        try:
            with open(path, 'x'):
                pass
        except FileExistsError:
            print(f"Error: File {path} already exists.")
        except OSError as e:
            print(f"Error creating file: {e}")

    @staticmethod
    def create_directory(path: str) -> None:
        """
        Create a new directory at the specified path.

        :param path: The path where the new directory should be created.
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}")

    @staticmethod
    def delete_file(path: str) -> None:
        """
        Delete the file at the specified path.

        :param path: The path of the file to be deleted.
        """
        if not os.path.isfile(path):
            print(f"Error: {path} is not a valid file.")
            return
        try:
            os.remove(path)
        except OSError as e:
            print(f"Error deleting file: {e}")

    @staticmethod
    def delete_directory(path: str) -> None:
        """
        Delete the directory at the specified path.

        :param path: The path of the directory to be deleted.
        """
        if not os.path.isdir(path):
            print(f"Error: {path} is not a valid directory.")
            return
        try:
            shutil.rmtree(path)
        except OSError as e:
            print(f"Error deleting directory: {e}")

    @staticmethod
    def read_file(path: str) -> Optional[str]:
        """
        Read the contents of the file at the specified path.

        :param path: The path of the file to be read.
        :return: Contents of the file or None if an error occurs.
        """
        if not os.path.isfile(path):
            print(f"Error: {path} is not a valid file.")
            return None
        try:
            with open(path, 'r') as file:
                return file.read()
        except OSError as e:
            print(f"Error reading file: {e}")
            return None

    @staticmethod
    def write_file(path: str, content: str) -> None:
        """
        Write the specified content to the file at the specified path.

        :param path: The path of the file to write to.
        :param content: The content to write to the file.
        """
        try:
            with open(path, 'w') as file:
                file.write(content)
        except OSError as e:
            print(f"Error writing to file: {e}")

    @staticmethod
    def append_to_file(path: str, content: str) -> None:
        """
        Append the specified content to the file at the specified path.

        :param path: The path of the file to append to.
        :param content: The content to append to the file.
        """
        try:
            with open(path, 'a') as file:
                file.write(content)
        except OSError as e:
            print(f"Error appending to file: {e}")

    @staticmethod
    def move_file(src: str, dest: str) -> None:
        """
        Move the file from the source path to the destination path.

        :param src: The source path of the file.
        :param dest: The destination path of the file.
        """
        if not os.path.isfile(src):
            print(f"Error: {src} is not a valid file.")
            return
        try:
            shutil.move(src, dest)
        except OSError as e:
            print(f"Error moving file: {e}")

    @staticmethod
    def copy_file(src: str, dest: str) -> None:
        """
        Copy the file from the source path to the destination path.

        :param src: The source path of the file.
        :param dest: The destination path of the file.
        """
        if not os.path.isfile(src):
            print(f"Error: {src} is not a valid file.")
            return
        try:
            shutil.copy(src, dest)
        except OSError as e:
            print(f"Error copying file: {e}")

    @staticmethod
    def check_path_exists(path: str) -> bool:
        """
        Check if a given path exists.

        :param path: The path to check.
        :return: True if the path exists, False otherwise.
        """
        return os.path.exists(path)
    
    @staticmethod
    def get_file_size(path: str) -> Optional[int]:
        """
        Get the size of the file at the specified path.

        :param path: The path of the file.
        :return: Size of the file in bytes or None if an error occurs.
        """
        if not os.path.isfile(path):
            print(f"Error: {path} is not a valid file.")
            return None
        try:
            return os.path.getsize(path)
        except OSError as e:
            print(f"Error getting file size: {e}")
            return None

    @staticmethod
    def get_directory_size(path: str) -> Optional[int]:
        """
        Get the size of the directory at the specified path.

        :param path: The path of the directory.
        :return: Size of the directory in bytes or None if an error occurs.
        """
        if not os.path.isdir(path):
            print(f"Error: {path} is not a valid directory.")
            return None
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size
        except OSError as e:
            print(f"Error getting directory size: {e}")
            return None

if __name__ == "__main__":
    fs_tool = FileSystemTool()

    # List directory contents
    contents = fs_tool.list_directory_contents('/path/to/directory')
    print(contents)

    # Create a new file
    fs_tool.create_file('/path/to/directory/new_file.txt')

    # Create a new directory
    fs_tool.create_directory('/path/to/directory/new_directory')

    # Delete a file
    fs_tool.delete_file('/path/to/directory/file_to_delete.txt')

    # Delete a directory
    fs_tool.delete_directory('/path/to/directory/directory_to_delete')

    # Read from a file
    content = fs_tool.read_file('/path/to/directory/file_to_read.txt')
    print(content)

    # Write to a file
    fs_tool.write_file('/path/to/directory/file_to_write.txt', 'Hello, World!')

    # Append to a file
    fs_tool.append_to_file('/path/to/directory/file_to_append.txt', 'Appended content')

    # Move a file
    fs_tool.move_file('/path/to/directory/file_to_move.txt', '/new/path/to/directory')

    # Copy a file
    fs_tool.copy_file('/path/to/directory/file_to_copy.txt', '/new/path/to/directory')

    # Check if a path exists
    exists = fs_tool.check_path_exists('/path/to/directory')
    print(f"Path exists: {exists}")

    # Get file size
    file_size = fs_tool.get_file_size('/path/to/directory/file_to_check.txt')
    print(f"File size: {file_size} bytes")

    # Get directory size
    dir_size = fs_tool.get_directory_size('/path/to/directory')
    print(f"Directory size: {dir_size} bytes")