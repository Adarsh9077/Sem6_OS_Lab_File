# Contiguous allocation
def contiguous_allocation(files, disk_size):
    blocks = int(disk_size / len(files))
    for i in range(len(files)):
        print("File:", files[i], " Start block:", i *
              blocks, " End block:", (i*blocks)+blocks-1)

# Indexed allocation


def indexed_allocation(files):
    for i in range(len(files)):
        print("File:", files[i], " Index block:", i)

# Linked allocation


def linked_allocation(files):
    for i in range(len(files)):
        blocks = int(input("Enter number of blocks for " + files[i] + ": "))
        print("File:", files[i], " Start block:", i, " End block:", i+blocks-1)
        for j in range(i+1, i+blocks):
            print("Block:", j, " Next block:", j+1)
        print("Block:", i+blocks-1, " Next block: -1")


# Main program
if __name__ == "__main__":
    files = ["file1", "file2", "file3"]
    disk_size = 30

    print("Contiguous Allocation")
    contiguous_allocation(files, disk_size)

    print("\nIndexed Allocation")
    indexed_allocation(files)

    print("\nLinked Allocation")
    linked_allocation(files)
