import os

def create_file(file_path, content):
    """
    Creates a new file at the specified path with the given content. 
    If the file already exists, it overwrites it.
    
    Args:
        file_path (str): The path where the file will be created.
        content (str): The content to write to the file.
    
    Raises:
        OSError: If the directory doesn't exist or the file can't be created due to permission issues.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except OSError as e:
        print(f"Error creating file {file_path}: {e}")

def read_file(file_path):
    """
    Reads the content of the specified file and returns it as a string.
    
    Args:
        file_path (str): The path of the file to read.
    
    Returns:
        str: The content of the file.
    
    Raises:
        OSError: If the file doesn't exist or can't be read due to permission issues.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except OSError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def update_file(file_path, new_content):
    """
    Appends the given content to the specified file.
    
    Args:
        file_path (str): The path of the file to update.
        new_content (str): The content to append to the file.
    
    Raises:
        OSError: If the file doesn't exist or can't be updated due to permission issues.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(new_content)
    except OSError as e:
        print(f"Error updating file {file_path}: {e}")

def delete_file(file_path):
    """
    Deletes the specified file.
    
    Args:
        file_path (str): The path of the file to delete.
    
    Raises:
        OSError: If the file doesn't exist or can't be deleted due to permission issues.
    """
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")

def create_directory(directory_path):
    """
    Creates a new directory at the specified path.
    
    Args:
        directory_path (str): The path where the directory will be created.
    
    Raises:
        OSError: If the directory already exists or can't be created due to permission issues.
    """
    try:
        os.makedirs(directory_path)
    except OSError as e:
        print(f"Error creating directory {directory_path}: {e}")

def delete_directory(directory_path):
    """
    Deletes the specified directory.
    
    Args:
        directory_path (str): The path of the directory to delete.
    
    Raises:
        OSError: If the directory doesn't exist or can't be deleted due to permission issues.
    """
    try:
        os.rmdir(directory_path)
    except OSError as e:
        print(f"Error deleting directory {directory_path}: {e}")

if __name__ == "__main__":
    # Example usage
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