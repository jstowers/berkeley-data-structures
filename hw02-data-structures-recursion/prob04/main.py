# Problem 4

# Write a recursive binary search function to search for an element in an array. 
# Assume the elements in the array are sorted. It should return the 
# index of the element if found and return -1 if it is not found.

array = [2, 13, 17, 19, 20, 21, 27, 30, 34, 39, 42, 48, 50]

target = 102

# BinarySearch is implemented with recursion.  It receives a sorted
# array, a target value, and left and right array indices.
#
# If the target exists, it returns the index of that element.
# If the target does not exist, it returns -1.
def binarySearch(target, array, leftIndex, rightIndex):

  print("array =", array)
  print("leftIndex =", leftIndex, "rightIndex =", rightIndex)

  # base case - target not found
  if leftIndex > rightIndex:
    return -1

  # calculate midpoint of array
  middle = int((leftIndex + rightIndex) / 2)

  # base case - target found
  if array[middle] == target:
    return middle

  # target is left of of midpoint
  elif array[middle] > target:
    return binarySearch(target, array, leftIndex, middle - 1)

  # target is right of midpoint
  elif array[middle] < target:
    return binarySearch(target, array, middle + 1, rightIndex)

# initial index positions
leftIndex = 0
rightIndex = len(array) - 1

result = binarySearch(target, array, leftIndex, rightIndex)
print("result =", result)