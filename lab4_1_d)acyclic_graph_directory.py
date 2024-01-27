# Initialize the DAG with an empty root directory
dag = {'/': []}

# Function to add a new directory to the DAG


def add_dir(path):
    parts = path.split('/')
    node = dag
    for part in parts:
        if part not in node:
            node[part] = {}  # type: ignore
        node = node[part]
    node['/'] = []  # type: ignore

# Function to add a new file to the DAG


def add_file(path):
    parts = path.split('/')
    node = dag
    for part in parts[:-1]:
        if part not in node:
            node[part] = {}  # type: ignore
        node = node[part]
    node['/'].append(parts[-1])  # type: ignore

# Function to list all files in a directory and its subdirectories


def list_files(path):
    node = dag
    parts = path.split('/')
    for part in parts:
        node = node[part]
    queue = [node]
    files = []
    while queue:
        curr = queue.pop(0)
        for key, value in curr.items():  # type: ignore
            if key == '/':
                files += value
            else:
                queue.append(value)
    return files


# Demonstration of the Acyclic-Graph Directory implementation
add_dir('/usr')
add_dir('/usr/local')
add_dir('/usr/bin')
add_file('/usr/local/file1.txt')
add_file('/usr/local/file2.txt')
add_file('/usr/bin/file3.txt')
add_file('/usr/file4.txt')

print(list_files('/usr/local'))  # Output: ['file1.txt', 'file2.txt']
print(list_files('/usr/bin'))  # Output: ['file3.txt']
# Output: ['file4.txt', 'file1.txt', 'file2.txt', 'file3.txt']
print(list_files('/usr'))
