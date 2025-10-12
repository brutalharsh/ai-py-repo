import os
import shutil
from pathlib import Path

class FileSystemUtility:
    """
    A utility class for file system operations.
    """

    @staticmethod
    def create_directory(path):
        """
        Create a new directory at the specified path. If the directory already exists, it does nothing.
        
        :param path: The path to the new directory.
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            print(f"Directory created at: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot create directory at {path}")
        except OSError as e:
            print(f"OS error: {e}")

    @staticmethod
    def list_files(path):
        """
        List all files in the specified directory.
        
        :param path: The path to the directory.
        :return: A list of filenames.
        """
        try:
            return [f for f in os.listdir(path) if Path(path, f).is_file()]
        except FileNotFoundError:
            print(f"Directory not found: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot list files in {path}")
        except OSError as e:
            print(f"OS error: {e}")
        return []

    @staticmethod
    def copy_file(source, destination):
        """
        Copy a file from source to destination. Overwrites the destination file if it exists.
        
        :param source: The path to the source file.
        :param destination: The path to the destination file.
        """
        try:
            shutil.copy2(source, destination)
            print(f"File copied from {source} to {destination}")
        except FileNotFoundError:
            print(f"Source file not found: {source}")
        except PermissionError:
            print(f"Permission denied: Cannot copy file to {destination}")
        except OSError as e:
            print(f"OS error: {e}")

    @staticmethod
    def move_file(source, destination):
        """
        Move a file from source to destination. Overwrites the destination file if it exists.
        
        :param source: The path to the source file.
        :param destination: The path to the destination file.
        """
        try:
            shutil.move(source, destination)
            print(f"File moved from {source} to {destination}")
        except FileNotFoundError:
            print(f"Source file not found: {source}")
        except PermissionError:
            print(f"Permission denied: Cannot move file to {destination}")
        except OSError as e:
            print(f"OS error: {e}")

    @staticmethod
    def delete_file(path):
        """
        Delete the specified file.
        
        :param path: The path to the file to be deleted.
        """
        try:
            os.remove(path)
            print(f"File deleted: {path}")
        except FileNotFoundError:
            print(f"File not found: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot delete file: {path}")
        except OSError as e:
            print(f"OS error: {e}")

    @staticmethod
    def get_file_size(path):
        """
        Get the size of the specified file.
        
        :param path: The path to the file.
        :return: The size of the file in bytes.
        """
        try:
            return os.path.getsize(path)
        except FileNotFoundError:
            print(f"File not found: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot get size of file: {path}")
        except OSError as e:
            print(f"OS error: {e}")
        return 0

    @staticmethod
    def create_file(path, content=""):
        """
        Create a new file with the specified content.
        
        :param path: The path to the new file.
        :param content: The content to write to the file.
        """
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"File created at: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot create file at {path}")
        except OSError as e:
            print(f"OS error: {e}")

    @staticmethod
    def read_file(path):
        """
        Read the content of the specified file.
        
        :param path: The path to the file.
        :return: The content of the file.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot read file: {path}")
        except OSError as e:
            print(f"OS error: {e}")
        return ""

    @staticmethod
    def list_directories(path):
        """
        List all directories in the specified path.
        
        :param path: The path to the directory.
        :return: A list of directory names.
        """
        try:
            return [d for d in os.listdir(path) if Path(path, d).is_dir()]
        except FileNotFoundError:
            print(f"Directory not found: {path}")
        except PermissionError:
            print(f"Permission denied: Cannot list directories in {path}")
        except OSError as e:
            print(f"OS error: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    FileSystemUtility.create_directory('/path/to/new_directory')

    files = FileSystemUtility.list_files('/path/to/directory')
    print(files)

    FileSystemUtility.copy_file('/path/to/source_file.txt', '/path/to/destination_file.txt')

    FileSystemUtility.move_file('/path/to/source_file.txt', '/path/to/destination_file.txt')

    FileSystemUtility.delete_file('/path/to/file_to_delete.txt')

    size = FileSystemUtility.get_file_size('/path/to/file.txt')
    print(f"Size: {size} bytes")

    FileSystemUtility.create_file('/path/to/new_file.txt', 'Hello, World!')

    content = FileSystemUtility.read_file('/path/to/new_file.txt')
    print(f"Content: {content}")

    directories = FileSystemUtility.list_directories('/path/to/')
    print(directories)