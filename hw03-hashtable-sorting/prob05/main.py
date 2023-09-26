# HW 3
# Problem No. 5

# Longest Subarray Length
# -----------------------------
# Given an array of integers and a target value, write a function that 
# returns the length of the longest subarray with a sum equal to the 
# target value.

# Note: while the sliding window technique is acceptable as a solution, 
# try solving this using a hash table.

# Example
# -----------------
# array = [3, 1, -1, 2, -1, 5, -2, 3]
# target = 3
# result = 5 => [-1, 2, -1, 5, -2]

def longest_subarray(array, target):
    sum = 0
    max_length = 0

    # hash table to store {sum : index}
    ht = {}

    for i in range(len(array)):
        sum += array[i]

        # set max_length as sum is calculated
        if(sum == target):
            max_length = max(max_length, i+1)
        
        # calculate difference between sum and target
        diff = sum - target

        # lookup difference in hash table
        # if it exists, calculate length of current index minus
        # index of diff
        if(ht.get(diff)):
            max_length = max(max_length, i - ht.get(diff))
    
        # add sum to hash table
        if sum not in ht:
            ht.update({sum: i})

    return max_length


# define Test class and instantiate test cases
class Test:
    def __init__(self, array, target):
        self.array = array
        self.target = target

test1 = Test([3, 1, -1, 2, -1, 5, -2, 3], 3)
test2 = Test([3, 1, -1, 2, -1, 5, -2, 3], 6)

test_suite = [
    test1,
    test2
]

for index, test in enumerate(test_suite):
    length = longest_subarray(test.array, test.target)
    print(f'{index + 1}. {str(test.array):25} target = {test.target} longest subarray = {length}')
    print("--------------------------------------------------------------")