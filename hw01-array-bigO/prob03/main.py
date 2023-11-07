# Problem 3
  
# Write an insert function/method that accepts an array and a value. It should insert the value and 
# maintain the array's sorted order. Write it in such a way to be as efficient as possible.
# Also, write the O notation of the average/worst case of your solution.

# define a sorted array
cars = ["BMW", "Chevrolet", "Ford", "Mercedes", "Tesla", "Volvo"]

# define a target value
newCar = "Ferrari"

# Insert accepts a target value and an array and inserts the
# target into the array while maintaining the array's sorted order. 
# Insert uses binary search to improve performance.
def insert(target, array):
  index = binarySearch(target, array)

  left = array[0:index]
  left.append(target)
  right = array[index:]

  return left + right

def binarySearch(target, array):

  # set start
  start = 0

  # set end
  end = len(array) - 1

  # while loop
  while start <= end:
    middle = int((start + end) / 2)

    if array[middle] == target:
      return middle

    elif array[middle] > target:
      end = middle - 1

    elif array[middle] < target:
      start = middle + 1

  # target does not exist in array
  return start

result = insert(newCar, cars)
print(result)

# Best time complexity: O(1) => the target value equals the first midpoint value
# Average time complexity: O(log n)
# Worst time complexity: O(log n)