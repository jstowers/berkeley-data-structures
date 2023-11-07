# Problem 4

# Write binary search function to return the index of a word in an array of words 
# sorted in reverse alphabetical order.  
# Do not sort the array before you perform the search.  
# Also, write the O notation of the best case and worst case.

# define array
fruits = ["durian", "cherry", "avocado", "apple"]

# define target value
target = "avocado"

# RevBinarySearch returns the index of the target word
# from an array sorted in reverse alphabetical order.
def revBinarySearch(target, array):

  # set start
  start = len(array) - 1

  # set end
  end = 0

  # while loop
  while start >= end:
    middle = int((start + end) / 2)

    if array[middle] == target:
      return middle

    elif array[middle] < target:
      start = middle - 1

    elif array[middle] > target:
      end = middle + 1

  return -1

result = revBinarySearch(target, fruits)
print("result =", result)

# Best case time complexity: O(1) => the target value equals the first midpoint value
# Worst time complexity: O(log n)