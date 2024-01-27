import os


def create_folder(dir_name):
    current_dir = os.getcwd()
    dir_path = os.path.join(current_dir, dir_name)

    try:
        os.mkdir(dir_path)
        print("Folder '{}' created at {}".format(dir_name, dir_path))
    except FileExistsError:
        print("Folder '{}' already exists at {}".format(dir_name, dir_path))


def create_file(dir_name, file_name, content):
    current_dir = os.getcwd()
    dir_path = os.path.join(current_dir, dir_name)

    if not os.path.exists(dir_path):
        create_folder(dir_name)

    file_path = os.path.join(dir_path, file_name)

    with open(file_path, "w") as f:
        f.write(content)
    print("File '{}' created at {}".format(file_name, file_path))


def list_files(path):
    """List all the files in the specified path"""
    files = os.listdir(path)
    for file in files:
        print(file)


def delete_file(path, name):
    """Delete a file from the specified path"""
    file_path = os.path.join(path, name)
    os.remove(file_path)
    print(f"File '{name}' deleted from {path}")


def delete_folder(path, name):
    """Delete a folder and all its contents from the specified path"""
    folder_path = os.path.join(path, name)
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(folder_path)
    print(f"Folder '{name}' and its contents deleted from {path}")


# Create the root directory
root_path = os.getcwd()  # set root directory as current working directory
root_name = "root"
create_folder(root_path)

# Create a subdirectory
subdir_name = os.path.join("root", "subdir")
create_folder(root_name)

# Create files in the root and subdirectory
file1_name = "file1.txt"
file1_content = "This is file 1"
create_file(root_name, file1_name, file1_content)

file2_name = "file2.txt"
file2_content = "This is file 2"
create_file(subdir_name, file2_name, file2_content)

# List all the files in the root directory
print(f"\nFiles in {root_name}:")
list_files(root_name)

# Delete a file from the subdirectory
delete_file(subdir_name, file2_name)

# Delete the subdirectory and all its contents
delete_folder(root_name, "subdir")