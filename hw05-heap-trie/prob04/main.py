# HW 5
# Problem No. 4

# Shortest Unique Prefix
# -------------------------
#
# Given an array of words, write a function that returns the shortest
# unique prefix of each word.
#
# ex) 
# words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 
#
# 'apple' returns 'a'
# 'banana' returns 'b'
# 'cherry' returns 'ch'
# 'cranberry' returns 'cr'
# 'grape' returns 'grape'
# 'grapefruit' returns 'grapef'
# 
# returns: ['a', 'b', 'ch', 'cr', 'grape', 'grapef']

from Trie import Trie

words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 
trie = Trie()

# longest prefix
longest_prefix = trie.longest_prefix_from_array(words)
print("longest_prefix =", longest_prefix)

# search
target = "cranberry"
search_result = trie.search(target)
print("search found =", search_result)



# define Test class and instantiate test cases
class Test:
    def __init__(self, array = []):
        self.array = array
        self.trie = Trie()

#test1 = Test(['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'])
test2 = Test(['apple', 'banana', 'cherry', 'grape', 'orange', 'opals'])

# define and execute test suite
test_suite = [
    test2,
]

for index, test in enumerate(test_suite):
    print()
    result = test.trie.shortest_prefix_from_array(test.array)
    print(f'{index + 1}. {test.array}')
    print(f'   shortest prefix = {result}')
    print()
    print("--------------------------------------------------------------")