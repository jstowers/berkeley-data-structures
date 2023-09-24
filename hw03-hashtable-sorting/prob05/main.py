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


array = [3, 1, -1, 2, -1, 5, -2, 3]

target = 3

def longest_subarray(array, target):
    ht = {}

    for i, num in enumerate(array):
        sum = num
        length = 1

        if (sum == target and ht.get(sum) == None):
            ht.update({sum: length})

        pointer = i+1

        while (pointer < len(array)):
            sum += array[pointer]
            length += 1

            #print("i =", i, " pointer =", pointer, " sum =", sum, " length =", length)

            if sum  == target:
                if ht.get(sum) == None or length > ht.get(sum):
                    ht.update({sum: length})
            pointer += 1

        print("ht=", ht)

    return ht[target]


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
    print("--------------------------------------------------------------")
    print(f'{index + 1}. {str(test.array):25} target = {test.target} longest subarray = {length}')  

