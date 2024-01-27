from os import name


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.type = "file"
        
class Directory:
    def __init__(self, name):


    self.name = name
    self.type = "directory"
    self.files = []
    self.subdirectories = []
    class Node:
    def __init__(self, name, type):


    self.name = name
    self.type = type
    self.children = []


def add_file(root_node, file_name, file_size, dir_path):


    # traverse the path to get the parent directory
    path_parts = dir_path.split("/")
    parent_dir = root_node
    for part in path_parts[:-1]:
        for child in parent_dir.children:
            if child.type == "directory" and child.name == part:
                parent_dir = child
                break
    else:
        # if the directory doesn't exist, create it
        new_dir = Directory(part)
        parent_dir.children.append(new_dir)
        parent_dir = new_dir
        # add the file to the parent directory
        parent_dir.files.append(File(file_name, file_size))
        print(f"\nFile {file_name} added to directory {dir_path}")


def add_directory(root_node, dir_path):


    # traverse the path to get the parent directory
path_parts = dir_path.split("/")
parent_dir = root_node
for part in path_parts[:-1]:
for child in parent_dir.children:
if child.type == "directory" and child.name == part:
parent_dir = child
break
else:
    # if the directory doesn't exist, create it
new_dir = Directory(part)
parent_dir.children.append(new_dir)
parent_dir = new_dir
# create the new directory object with the given name
new_dir = Directory(path_parts[-1])
# add the new directory to the parent directory
parent_dir.children.append(new_dir)
print(f"\nDirectory {path_parts[-1]} added to directory {dir_path}")


def display(root_node, level=0):


    # display the name and type of the current node
print(" "*level, end="")
print(root_node.name, root_node.type)
# recursively display the children of the current node
for child in root_node.children:
if child.type == "directory":
display(child, level+1)
else:
print(" "*(level+1), end="")
print(child.name, child.size, "bytes")


def main():


    # create the root node
root = Node("/", "directory")
# add some files and directories
add_file(root, "file1.txt", 1000, "/")
add_file(root, "file2.txt", 2000, "/dir1")
add_file(root, "file3.txt", 3000, "/dir1/subdir1")
add_file(root, "file4.txt", 4000, "/dir2")
add_directory(root, "/dir1/subdir1/newdir")
# display the directory structure
display(root)
if __name__ == "__main__":
main()
