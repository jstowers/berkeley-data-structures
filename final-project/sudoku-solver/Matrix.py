from Cell import Cell

class Matrix:

    def __init__(self):
        # standard 9 x 9 sudoku grid
        self.col_count = 9
        self.row_count = 9
        self.box_count = 9
        self.cell_count = self.col_count * self.row_count
        
        # ht for cols and rows
        self.cols = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        self.rows = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}

        # update rows {} to add nested hash tables for values 1 -> 9
        self.__update_rows()

        # update cols {} to add nested hash tables for values 1 -> 9
        self.__update_cols()
  
        # 2D 9x9 matrix
        self.matrix = self.__create_matrix()


    # __update_rows creates a nested hash table {} to hold values from 1 -> 9
    def __update_rows(self):

        for key in self.rows:
            index = 0 
            while index < self.row_count:
                if (index + 1) not in self.rows[key]:
                    self.rows[key][index + 1] = {
                        "is_clue": False,
                        "is_present": False
                    }
                index += 1

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

                # if clue, update booleans in rows {}
                if c.value != 0 and c.is_clue:
                    self.rows[i][c.value]['is_clue'] = True
                    self.rows[i][c.value]['is_present'] = True

    # check_clue_status returns true if the value is a given clue, 
    # false if it is not.
    def check_clue_status(self, value):
        if value != 0:
            return True
        return False
    
    def value(self, i, j):
        return self.matrix[i][j]
    
    # __create_matrix creates a 9 x 9 matrix with empty Cell() objects
    def __create_matrix(self):

        # initialize empty 2D matrix
        return  [[Cell() for j in range(self.col_count)] for i in range(self.row_count)]
    
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
        if i == self.row_count and j == self.col_count:
            return
        
        # print / process current cell
        print("i =", i, " j =", j, " [", i, "][", j, "] =", self.matrix[i][j].value)

        # traverse current row, column by column
        if j < self.row_count - 1:
            self.traverse(i, j+1)
        
        # if last column reached, move to next row
        elif i < self.col_count - 1:
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


