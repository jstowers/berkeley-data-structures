# HW 3
# Problem No. 2

# Insertion Sort
# --------------------
# Implement the insertion sort function.


array = [10, 2, 4, 5, -1, 3, 0, 24, 1, 15, 17, 11, -23]

def insertion_sort(array):

    for i in range(1, len(array)):
        print("i =", i, "ele =", array[i])

        temp = array[i]

        if array[i-1] > temp:
            array[i]
            array[i-1] = temp
            array[i]



result = insertion_sort(array)
print("result =", result)