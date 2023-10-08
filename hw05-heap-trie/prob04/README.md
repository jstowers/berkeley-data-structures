# __Shortest Unique Prefix__

## Description

Given an array of words, write a function that returns the shortest
unique prefix of each word.

For readable results, the words in the input array must
be sorted.


## Example

words = ['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit'] 

    'apple' returns 'a'
    'banana' returns 'b'
    'cherry' returns 'ch'
    'cranberry' returns 'cr'
    'grape' returns 'grape'
    'grapefruit' returns 'grapef'
 
result:

    ['a', 'b', 'ch', 'cr', 'grape', 'grapef']


## Test Cases

1. `['apple', 'banana', 'cherry', 'cranberry', 'grape', 'grapefruit']`

    shortest prefix = `['a', 'b', 'ch', 'cr', 'grape', 'grapef']`
--------------------------------------------------------------

2. `['apple', 'banana', 'cherry', 'grape', 'opals', 'orange']`

    shortest prefix = `['a', 'b', 'c', 'g', 'op', 'or']`
--------------------------------------------------------------

3. `['apparatus', 'appetite', 'apple', 'appliance']`

   shortest prefix = `['appa', 'appe', 'apple', 'appli']`
--------------------------------------------------------------

4. `['apple', 'banana', 'orange', 'peach']`

   shortest prefix = `['a', 'b', 'o', 'p']`
--------------------------------------------------------------

5. `['lemon', 'lemongrass', 'licorice', 'lime', 'lychee']`

   shortest prefix = `['lemon', 'lemong', 'lic', 'lim', 'ly']`
--------------------------------------------------------------

6. `['lime', 'limeberry', 'lingonberry']`

   shortest prefix = `['lime', 'limeb', 'lin']`
--------------------------------------------------------------

7. `['grape', 'grapefruit', 'grapes', 'grapple']`

   shortest prefix = `['grape', 'grapef', 'grapes', 'grapp']`
--------------------------------------------------------------