import os

def delete_file(relative_path):
    try:
        os.remove(relative_path)
        print(f"File {relative_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting file {relative_path}: {e}")

# Example usage with a relative path
file_name = 'your_file.txt'
delete_file(file_name)