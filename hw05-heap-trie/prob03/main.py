# HW 5
# Problem No. 3

# Longest String Prefix
# -------------------------
#
# Given an array of words, write a function that returns the longest prefix.
# Write it so that it performs efficiently.
#
# ex) 
# words = ["apple", "appetite", "apparatus", "appliance"]
# solution => "app"

from Trie import Trie

# define Test class and instantiate test cases
class Test:
    def __init__(self, array = []):
        self.array = array
        self.trie = Trie()

test1 = Test(["apple", "appetite", "apparatus", "appliance"])
test2 = Test(["apple", "orange", "banana", "peach"])
test3 = Test(["lemon", "lime", "lemongrass", "lychee", "licorice"])
test4 = Test(["lime", "limeberry", "lingonberry"])
test5 = Test(["grape", "grapes", "grapefruit", "grapple"])

# define and execute test suite
test_suite = [
    test1,
    test2,
    test3,
    test4,
    test5,
]

for index, test in enumerate(test_suite):
    print()
    result = test.trie.longest_prefix_from_array(test.array)
    print(f'{index + 1}. {test.array}')
    print(f'   longest prefix = {result}')
    print()
    print("--------------------------------------------------------------")