# Banker's Algorithm

# USE OF FUNCTIONS.

def algo():
    # P0, P1, P2, P3, P4 are the Process names here
    n_Processes = 5  # Number of processes
    r_Total = 3  # Number of resources

    # Allocation Matrix
    alloc = [[0, 1, 0],
             [2, 0, 0],
             [3, 0, 2],
             [2, 1, 1],
             [0, 0, 2]]

    # MAX Matrix
    max = [[7, 5, 3],
           [3, 2, 2],
           [9, 0, 2],
           [2, 2, 2],
           [4, 3, 3]]

    avail = [2, 13, 22]  # Available Resources

    f = [0] * n_Processes
    ans = [0] * n_Processes
    ind = 0
    for k in range(n_Processes):
        f[k] = 0

    need = [[0 for i in range(r_Total)] for i in range(n_Processes)]
    for i in range(n_Processes):
        for j in range(r_Total):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0
    for k in range(5):
        for i in range(n_Processes):
            if (f[i] == 0):
                flag = 0
                for j in range(r_Total):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break

                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(r_Total):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    print("THE SAFE SEQUENCE IS: ")

    for i in range(n_Processes - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n_Processes - 1], sep="")


# DRIVER CODE OR MAIN CODE.
algo()
