# Problem 02

# Write code to populate an array with the size n with numbers from 0 to n-1. 
# Next, shuffle (randomly reorder or rearrange)  the numbers in the array.
# Finally, provide the Big O notation for both the average and worst case time complexities of your code.
# Avoid using shuffle() method/function. However, feel free to use the built-in random() function.

import random

# define n
n = 100

# populate numbers array from 0 to n-1
numbers = [x for x in range(n)]
print(numbers)

# loop through numbers array and swap numbers[index] with numbers[random_int]
for number in numbers:
  random_int = random.randint(0,n-1)
  temp = numbers[number]
  numbers[number] = numbers[random_int]
  numbers[random_int] = temp
  
print(numbers)

# Time complexity:
# For creating the array, the time complexity is O(n).
# For shuffling the numbers in the array, the time complexity is O(n), both average and worst case.
# When these operations are combined, O(n + n) = O(2n) = O(n)