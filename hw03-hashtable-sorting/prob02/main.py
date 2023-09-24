# HW 3
# Problem No. 2

# Insertion Sort
# --------------------
# Implement the insertion sort function.


array = [10, 2, 4, 5, -1, 3, 0, 24, 1, 15, 17, 11, -23]

def insertion_sort(array):

    print(array)

    for i in range(1, len(array)):

        # set temp value at current index
        temp = array[i]

        # starting index for each value that will be compared
        position = i-1

        # inner while loop for backward comparison of the sorted values
        while position >= 0:
            # temp is smaller so swap values
            if array[position] > temp:
                array[position + 1] = array[position]
                position -= 1

            # break while loop: value at position >= temp
            else:
                break
        
        # move temp value into gap
        array[position+1] = temp
        print(array)

    return array

result = insertion_sort(array)
print("result =", result)