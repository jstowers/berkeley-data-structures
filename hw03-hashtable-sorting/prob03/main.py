# HW 3
# Problem No. 3

# Find Missing Numbers
# --------------------
# Write a function that accepts an array of size n containing random numbers 
# ranging from 0 to n-1. This array may contain duplicates, and the numbers are 
# not arranged in any particular order. 

# This function should return a new array that consists of any missing numbers 
# within the range from 0 to n-1.  This function must have a time complexity 
# of O(n) to get full credit.

# Example
# -----------------
# array = [0, 3, 6, 7, 3, 3, 0, 4]
# n = 8
# expected missing: [ 1, 2, 5 ]

# Solution
# -----------------

# FindMissing receives an array of random numbers from range 0 to n-1
# and returns a new array of any numbers missing from within that range.
def find_missing_numbers(array):
    
    # define missing and existing dictionaries (hash tables)
    missing = {}
    existing = {}

    for i in range (len(array)):

        # does value, array[i], exist in existing?
        # if no, add value to existing
        if not existing.get(array[i]):
            existing.update({array[i]:1})
        
        # does index, i, exist in existing?
        # if no, add index to missing
        if not existing.get(i):
            missing.update({i:1})

        # does value, array[i], exist in missing?
        # if yes, pop value from missing
        if missing.get(array[i]):
            missing.pop(array[i])

    return list(missing.keys())

arrayList = [
    [0, 3, 6, 7, 3, 3, 0, 4],
    [0, 0, 1, 3],
    [0, 1, 2, 5, 5, 5, 4],
    [0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0],
    [1, 2, 0, 3, 5, 4],
    [4, 4, 4, 4, 4, 4],
    [4, 3, 3, 5, 1]
]

for index, array in enumerate(arrayList):
    missingValues = find_missing_numbers(array)
    print("--------------------------------------------------------------")
    print(f'{index + 1}. {str(array):25} missing values = {missingValues}')    
