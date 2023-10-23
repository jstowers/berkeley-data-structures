from Cell import Cell

class Matrix:
    def __init__(self):
        self.cols = 9
        self.rows = 9
        self.cell_count = self.cols * self.rows
        self.box_count = 9
        self.matrix = self.__create_matrix()

    def create_from_array(self, rows_array):
        # check for empty array
        if len(rows_array) == 0:
            raise Exception("rows array is empty")
        # check for 9 rows
        if len(rows_array) != 9:
            raise Exception("rows array does not contain 9 rows")
        
        # loop over rows_array
        for i in range(len(rows_array)):
            # check for 9 values
            if len(rows_array[i]) != 9:
                raise Exception("row does not contain 9 values")
            for j in range(len(rows_array[i])):
                c = Cell()
                c.i = i
                c.j = j
                c.value = rows_array[i][j]
                c.is_clue = self.check_clue_status(c.value)
                self.matrix[i][j] = c
        return self.matrix

    # check_clue_status returns true if the value is a given clue, 
    # false if it is not.
    def check_clue_status(self, value):
        if value != 0:
            return True
        return False
    
    def value(self, i, j):
        return self.matrix[i][j]
    
    # __create_matrix creates a 9 x 9 matrix array.  It fills each
    # cell with an integer from 1 to 81.
    def __create_matrix(self):

        # initialize empty 2D matrix
        self.matrix = [[0 for j in range(self.cols)] for i in range(self.rows)]

        # populate cells from 1 to 81
        z = 0
        while z < self.cell_count:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = z+1
                    z += 1
    
        return self.matrix
    
    # traverse takes an i and j value and recursively
    # traverses through the matrix till the end.
    def traverse(self, i = None, j = None):

        # initialize i value
        if i == None:
            i = 0
        
        # initialize j value
        if j == None:
            j = 0

        # base case: bottom-right corner of matrix
        if i == self.rows and j == self.cols:
            return
        
        # print / process current cell
        print("i =", i, " j =", j, " [", i, "][", j, "] =", self.matrix[i][j].value)

        # traverse current row, column by column
        if j < self.rows - 1:
            self.traverse(i, j+1)
        
        # if last column reached, move to next row
        elif i < self.cols - 1:
            self.traverse(i+1, 0)

    def print(self):
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print()
        print("---------------- j --------------------")
        print()
        print(''.join(['{:4}'.format(index) for index in indices]))
        print("---------------------------------------")
        print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) 
        for row in self.matrix]))
        print()


