import os
import shutil

class FileSystemUtility:
    """
    A utility class for file system operations.
    """

    @staticmethod
    def create_directory(path):
        """
        Create a new directory at the specified path.
        
        :param path: The path to the new directory.
        """
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory created at: {path}")
        except Exception as e:
            print(f"Error creating directory: {e}")

    @staticmethod
    def list_files(path):
        """
        List all files in the specified directory.
        
        :param path: The path to the directory.
        :return: A list of filenames.
        """
        try:
            files = os.listdir(path)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    @staticmethod
    def copy_file(source, destination):
        """
        Copy a file from source to destination.
        
        :param source: The path to the source file.
        :param destination: The path to the destination file.
        """
        try:
            shutil.copyfile(source, destination)
            print(f"File copied from {source} to {destination}")
        except Exception as e:
            print(f"Error copying file: {e}")

    @staticmethod
    def move_file(source, destination):
        """
        Move a file from source to destination.
        
        :param source: The path to the source file.
        :param destination: The path to the destination file.
        """
        try:
            shutil.move(source, destination)
            print(f"File moved from {source} to {destination}")
        except Exception as e:
            print(f"Error moving file: {e}")

    @staticmethod
    def delete_file(path):
        """
        Delete the specified file.
        
        :param path: The path to the file to be deleted.
        """
        try:
            os.remove(path)
            print(f"File deleted: {path}")
        except Exception as e:
            print(f"Error deleting file: {e}")

    @staticmethod
    def get_file_size(path):
        """
        Get the size of the specified file.
        
        :param path: The path to the file.
        :return: The size of the file in bytes.
        """
        try:
            size = os.path.getsize(path)
            return size
        except Exception as e:
            print(f"Error getting file size: {e}")
            return 0

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