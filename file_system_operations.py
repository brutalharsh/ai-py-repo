import os
import shutil

class FileSystemTool:
    """
    A class to provide various file system operations.
    """

    def list_directory_contents(self, path):
        """
        List the contents of the specified directory.
        
        :param path: The path to the directory to list contents of.
        :return: List of directory contents or None if an error occurs.
        """
        try:
            contents = os.listdir(path)
            return contents
        except Exception as e:
            print(f"Error listing directory contents: {e}")
            return None

    def create_file(self, path):
        """
        Create a new file at the specified path.
        
        :param path: The path where the new file should be created.
        """
        try:
            with open(path, 'w'):
                pass
        except Exception as e:
            print(f"Error creating file: {e}")

    def create_directory(self, path):
        """
        Create a new directory at the specified path.
        
        :param path: The path where the new directory should be created.
        """
        try:
            os.makedirs(path)
        except Exception as e:
            print(f"Error creating directory: {e}")

    def delete_file(self, path):
        """
        Delete the file at the specified path.
        
        :param path: The path of the file to be deleted.
        """
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error deleting file: {e}")

    def delete_directory(self, path):
        """
        Delete the directory at the specified path.
        
        :param path: The path of the directory to be deleted.
        """
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"Error deleting directory: {e}")

    def read_file(self, path):
        """
        Read the contents of the file at the specified path.
        
        :param path: The path of the file to be read.
        :return: Contents of the file or None if an error occurs.
        """
        try:
            with open(path, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def write_file(self, path, content):
        """
        Write the specified content to the file at the specified path.
        
        :param path: The path of the file to write to.
        :param content: The content to write to the file.
        """
        try:
            with open(path, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def move_file(self, src, dest):
        """
        Move the file from the source path to the destination path.
        
        :param src: The source path of the file.
        :param dest: The destination path of the file.
        """
        try:
            shutil.move(src, dest)
        except Exception as e:
            print(f"Error moving file: {e}")

    def copy_file(self, src, dest):
        """
        Copy the file from the source path to the destination path.
        
        :param src: The source path of the file.
        :param dest: The destination path of the file.
        """
        try:
            shutil.copy(src, dest)
        except Exception as e:
            print(f"Error copying file: {e}")

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

    # Move a file
    fs_tool.move_file('/path/to/directory/file_to_move.txt', '/new/path/to/directory')

    # Copy a file
    fs_tool.copy_file('/path/to/directory/file_to_copy.txt', '/new/path/to/directory')