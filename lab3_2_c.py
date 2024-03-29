# Implementation of LFU page replacement algorithm

from typing import List
from collections import defaultdict

def pageFaults(n, c, pages):
    count = 0

    # To store elements in memory of size c
    v = []
    # To store frequency of pages
    mp = defaultdict(int)

    for i in range(n):
        # Find if element is present in memory or not
        if pages[i] not in v:
            # If element is not present
            if len(v) == c:
                # If memory is full
                # Decrease the frequency
                mp[v[0]] -= 1
                # Remove the first element as it is least frequently used
                v.pop(0)

            # Add the element at the end of memory
            v.append(pages[i])
            # Increase its frequency
            mp[pages[i]] += 1

            # Increment the count
            count += 1
        else:
            # If element is present
            # Remove the element and add it at the end
            # Increase its frequency
            mp[pages[i]] += 1
            v.remove(pages[i])
            v.append(pages[i])

        # Compare frequency with other pages starting from the 2nd last page
        k = len(v) - 2

        # Sort the pages based on their frequency and time at which they arrive
        # if frequency is same then the page arriving first must be placed first
        while k >= 0 and mp[v[k]] > mp[v[k+1]]:
            v[k], v[k+1] = v[k+1], v[k]
            k -= 1

    return count

if __name__ == '__main__':
    pages = [1, 2, 3, 4, 2, 1, 5]
    n, c = 7, 3

    print(pageFaults(n, c, pages))
