# Longest Subarray with Sum K

A classic interview problem that requires a simple, but crafty mathematical
computation to get an efficient solution in O(n) time.

Reference:
https://www.youtube.com/watch?v=frf7qxiN2qU


## Brute Force Solution

The brute force method requires nested for loops.  These loops determine all possible subarrays
for the given array.  For each subarray, the algorithm calculates the sum and length.  If a
subarray sums to the target value, k, the subarray's length is compared to max_length, replacing
max_length if its length is greater.  At the end, the function returns max_length.

The time complexity is O(n^2).

```python
def longest_subarray_v2(array, target):

    max_length = 0

    for i in range(len(array)):

        # initialize sum for subarrays beginning at array[i]
        sum = 0

        for j in range(i, len(array)):
            sum += array[j]

            # determine max length of subarray
            if(sum == target):
                max_length = max(max_length, j - i + 1)
    
            #print("i =", i, "j =", j, "sum =", sum, "max_length =", max_length)

    return max_length
```



## Efficient Solution

The efficient solution employs a hash table to store the running sums and index values.

The time complexity is O(n).

### Algorithm

Imagine an array like this:

[ . . . . . . . ]

Now let's examine one point, *:

[ . . . . * . . ]

If this point is the last element in a sub-array, how many subarrays can there be?

[ * ]               l = 1

[ . * ]             l = 2

[ . . * ]           l = 3

[ . . . * ]         l = 4

[ . . . . * ]       l = 5

Let's assume that for one of these subarrays, the sum = k.  Maybe it's [ . . * ] such that:

k = [ . . * ]

And as we iterate over each element, we keep a running sum, x, such that:

[ . . . . * ] = x

By dividing terms, we get:

[ . . ] + [ . . * ] = x

[ . . ] + k = x

If we have a value such that x - k = [ . . ], then we know that the length of k will 
be the current index of * minus the index of that sum [ . . ].  This sum is the one that is
stored in the hash table.