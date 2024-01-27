# MVT
ms = int(input("Enter the total memory available (in Bytes) -- "))
temp = ms
mp = []
n = 0
ch = 'y'

while ch == 'y':
    mp.append(
        int(input(f"Enter memory required for process {n+1} (in Bytes) -- ")))
    if mp[n] <= temp:
        print(f"Memory is allocated for Process {n+1}")
        temp -= mp[n]
    else:
        print("Memory is Full")
        break
    ch = input("Do you want to continue(y/n) -- ")
    n += 1

print(f"\nTotal Memory Available -- {ms}")
print("\n\tPROCESS\t\t MEMORY ALLOCATED ")
for i in range(n):
    print(f"\t{i+1}\t\t{mp[i]}")

print(f"\nTotal Memory Allocated is {ms - temp}")
print(f"Total External Fragmentation is {temp}", "\n\n")