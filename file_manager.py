import os

def create_file(file_path, content, overwrite=True):
    """
    Creates a new file at the specified path with the given content. 
    If the file already exists, it overwrites it if overwrite is True.
    
    Args:
        file_path (str): The path where the file will be created.
        content (str): The content to write to the file.
        overwrite (bool): Whether to overwrite the file if it exists.
    
    Raises:
        FileNotFoundError: If the directory doesn't exist.
        PermissionError: If the file can't be created due to permission issues.
    """
    mode = 'w' if overwrite else 'x'
    try:
        with open(file_path, mode) as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Directory does not exist for file {file_path}")
        raise
    except PermissionError:
        print(f"Permission denied to create file {file_path}")
        raise
    except FileExistsError:
        print(f"File {file_path} already exists and overwrite is set to False")
        raise

def read_file(file_path):
    """
    Reads the content of the specified file and returns it as a string.
    
    Args:
        file_path (str): The path of the file to read.
    
    Returns:
        str: The content of the file.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        PermissionError: If the file can't be read due to permission issues.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} does not exist")
        raise
    except PermissionError:
        print(f"Permission denied to read file {file_path}")
        raise

def update_file(file_path, new_content):
    """
    Appends the given content to the specified file.
    
    Args:
        file_path (str): The path of the file to update.
        new_content (str): The content to append to the file.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        PermissionError: If the file can't be updated due to permission issues.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(new_content)
    except FileNotFoundError:
        print(f"File {file_path} does not exist")
        raise
    except PermissionError:
        print(f"Permission denied to update file {file_path}")
        raise

def delete_file(file_path):
    """
    Deletes the specified file.
    
    Args:
        file_path (str): The path of the file to delete.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        PermissionError: If the file can't be deleted due to permission issues.
    """
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File {file_path} does not exist")
        raise
    except PermissionError:
        print(f"Permission denied to delete file {file_path}")
        raise

def create_directory(directory_path, exist_ok=True):
    """
    Creates a new directory at the specified path.
    
    Args:
        directory_path (str): The path where the directory will be created.
        exist_ok (bool): Whether to raise an error if the directory already exists.
    
    Raises:
        PermissionError: If the directory can't be created due to permission issues.
    """
    try:
        os.makedirs(directory_path, exist_ok=exist_ok)
    except PermissionError:
        print(f"Permission denied to create directory {directory_path}")
        raise

def delete_directory(directory_path):
    """
    Deletes the specified directory.
    
    Args:
        directory_path (str): The path of the directory to delete.
    
    Raises:
        FileNotFoundError: If the directory doesn't exist.
        PermissionError: If the directory can't be deleted due to permission issues.
        OSError: If the directory is not empty.
    """
    try:
        os.rmdir(directory_path)
    except FileNotFoundError:
        print(f"Directory {directory_path} does not exist")
        raise
    except PermissionError:
        print(f"Permission denied to delete directory {directory_path}")
        raise
    except OSError:
        print(f"Directory {directory_path} is not empty")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        create_file('example.txt', 'Hello, World!')
        content = read_file('example.txt')
        if content:
            print(content)
        update_file('example.txt', '\nThis is an update.')
        content = read_file('example.txt')
        if content:
            print(content)
        delete_file('example.txt')
        create_directory('example_dir')
        delete_directory('example_dir')
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Operation failed: {e}")