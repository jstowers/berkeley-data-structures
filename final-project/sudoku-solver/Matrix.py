from Cell import Cell

import json

class Matrix:

    def __init__(self):
        # standard 9 x 9 sudoku grid
        self.row_count = 9
        self.col_count = 9
        self.box_count = 9
        self.cell_count = self.col_count * self.row_count
        
        # ht for rows, cols, boxes
        self.rows = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        self.cols = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        self.boxes = {"A":{}, "B":{}, "C":{}, "D":{}, "E":{}, "F":{}, "G":{}, "H":{}, "I":{}}

        # update rows {} to add nested hash tables for values 1 -> 9
        self.__update_ht(self.rows)

        # update cols {} to add nested hash tables for values 1 -> 9
        self.__update_ht(self.cols)

        # update boxes {} to add nested hash tables for values 1 -> 9
        self.__update_ht(self.boxes)
  
        # 2D 9x9 matrix
        self.matrix = self.__create_matrix()

    # Update_ht takes a hash table for rows, cols, or boxes and adds
    # a nested hash table to store values 1 -> 9
    def __update_ht(self, ht):
        for key in ht:
            index = 0 
            while index < self.row_count:
                if (index + 1) not in ht[key]:
                    ht[key][index + 1] = {
                        "is_clue": False,
                        "is_present": False
                    }
                index += 1

    # Create_from_array does the heavy lifting in creating a 2D 9 x 9 
    # Sudoku grid comprising 81 Cell objects.
    def create_from_array(self, rows_array):
        # check for empty array
        if len(rows_array) == 0:
            raise Exception("rows array is empty")
        
        # check for 9 rows
        if len(rows_array) != 9:
            raise Exception("rows array does not contain 9 rows")
        
        # loop over rows_array
        for i in range(len(rows_array)):

            # check for 9 columns (values) per row
            if len(rows_array[i]) != self.col_count:
                raise Exception("row does not contain 9 values")
            
            # loop over columns
            for j in range(len(rows_array[i])):
                c = Cell()
                c.i = i
                c.j = j
                c.value = rows_array[i][j]
                c.is_clue = self.check_clue_status(c.value)
                c.box_value = self.get_box_value(i, j)

                # assign Cell to matrix
                self.matrix[i][j] = c

                # if value is a clue, update booleans in hash tables
                if c.value != 0 and c.is_clue:
                    # update rows {}
                    self.rows[i][c.value]['is_clue'] = True
                    self.rows[i][c.value]['is_present'] = True

                    # update cols {}
                    self.cols[j][c.value]['is_clue'] = True
                    self.cols[j][c.value]['is_present'] = True

                    # update boxes {}
                    self.boxes[c.box_value][c.value]['is_clue'] = True
                    self.boxes[c.box_value][c.value]['is_present'] = True

    # Check_clue_status returns true if the value is a given clue, 
    # false if it is not.
    def check_clue_status(self, value):
        return value != 0
    
    # Get_box_value receives an i and j value and returns 
    # the box value, A -> I, for that coordinate.
    def get_box_value(self, i, j):
        # check for i values in range
        if i < 0 or i > 8:
            raise Exception("i value is out of range")
        
        # check for j values in range
        if j < 0 or j > 8:
            raise Exception("j value is out of range")

        if i <= 2:
            if j <= 2:
                return "A"
            elif j > 2 and j <= 5:
                return "B"
            else:
                return "C"
        elif i > 2 and i <= 5:
            if j <= 2:
                return "D"
            elif j > 2 and j <= 5:
                return "E"
            else:
                return "F"
        elif i > 5:
            if j <= 2:
                return "G"
            elif j > 2 and j <= 5:
                return "H"
            else:
                return "I"
    
    def value(self, i, j):
        return self.matrix[i][j].value
    
    # __create_matrix creates a 9 x 9 matrix with empty Cell() objects
    def __create_matrix(self):

        # initialize empty 2D matrix
        return  [[Cell() for j in range(self.col_count)] for i in range(self.row_count)]
    
    # solve starts the matrix traversal and processing
    def solve(self):
        # initialize top-left cell in grid
        cell = self.matrix[0][0]

        # initialize forward traversal
        direction = "forward"
        
        self.process_cell(cell, direction)
           
    # Process_cell applies the sudoku rules by row, column,
    # and box to find a possible correct value for that cell.
    def process_cell(self, cell, direction):
        print("inside process_cell")
        i = cell.i
        j = cell.j

        # skip cell if it is a clue
        if cell.is_clue:
            #print("skipping - cell is clue")
            if direction == "forward":
                self.traverse(i, j + 1, direction)
            elif direction == "backward":
                self.backtrack(i, j - 1, direction)

        temp_value = 1

        ## maybe just do one while loop
        while temp_value <= 9:
            current_box = cell.box_value
            if self.rows[i][temp_value]["is_present"] == True:
                print("row has temp_value ", temp_value)
                temp_value += 1
            elif self.cols[j][temp_value]["is_present"] == True:
                print("col has temp_value ", temp_value)
                temp_value += 1
            elif self.boxes[current_box][temp_value]["is_present"] == True:
                print("box has temp_value ", temp_value)
                temp_value += 1
            # if none of the three have it, exit the loop
            else:
                print("temp_value ", temp_value, "not in row, col, or box")
                break

        # # does row[i] have temp_value?
        # while temp_value <= 9 and self.rows[i][temp_value]["is_present"] == True:
        #     print("row temp_value =", temp_value)
        #     temp_value += 1
        
        # # does col[j] have temp value?
        # while temp_value <= 9 and self.cols[j][temp_value]["is_present"] == True:
        #     print("col temp_value =", temp_value)
        #     temp_value += 1

        # # does box holding [i][j] have temp_value?
        # current_box = cell.box_value
        # while temp_value <= 9 and self.boxes[current_box][temp_value]["is_present"] == True:
        #     print("boxes temp_value =", temp_value)
        #     temp_value += 1
        
        print("temp_value before assignment =", temp_value)
        # 1. Assign value
        if temp_value <= 9:
            cell.value = temp_value
            #print("i =", i, "j =", j, "temp_value =", temp_value)

            self.rows[i][temp_value]["is_present"] = True
            #print("self.rows[i][temp_value] =", self.rows[i][temp_value])

            self.cols[j][temp_value]["is_present"] = True
            self.boxes[current_box][temp_value]["is_present"] = True

            self.print()

            if j > 8:
                self.traverse(i+1, 0, "forward")
            else:
                self.traverse(i, j+1, "forward")
      
        # 2. Backtrack
        # TODO: somehow we need to revert the is_present properties
        # when we backtrack.
        else:
            self.print()
            if j < 0:
                self.backtrack(i-1, 8, "backward")
            else:
                self.backtrack(i, j-1, "backward")

    # Backtrack takes an i and j value and recursively
    # backtracks through the matrix until the beginning.
    def backtrack(self, i = None, j = None, direction = None):
        # initialize i value
        if i == None:
            i = 8
        
        # initialize j value
        if j == None:
            j = 8

        # initialize direction
        if direction == None:
            direction = "backward"

        # check for i values in range
        if i < 0 or i > 8:
            raise Exception("i value is out of range")
        
        # check for j values in range
        if j < 0 or j > 8:
            raise Exception("j value is out of range")

        # print / process current cell
        # print("i =", i, " j =", j, " [", i, "][", j, "] =", self.matrix[i][j].value)
        cell = self.matrix[i][j]
        print("i =", i, " j =", j, " [", i, "][", j, "] =", cell.value)
        self.process_cell(cell, direction)

        # base case: upper-left corner of matrix
        if i == 0 and j == 0:
            return
        
        # backtrack current row, column by column
        if j > 0:
            self.backtrack(i, j-1, direction)
        
        # if first column reached, move up to next row
        elif i > 0:
            self.backtrack(i-1, 8, direction)

    # traverse takes an i and j value and recursively
    # traverses forward through the matrix until the end.
    def traverse(self, i = None, j = None, direction = None):

        # initialize i value
        if i == None:
            i = 0
        
        # initialize j value
        if j == None:
            j = 0

        # initialize direction
        if direction == None:
            direction = "forward"
        
        # check for i values in range
        if i < 0 or i > 8:
            raise Exception("i value is out of range")
        
        # check for j values in range
        if j < 0 or j > 8:
            raise Exception("j value is out of range")

        # base case: bottom-right corner of matrix
        if i == self.row_count and j == self.col_count:
            return
        
        # print / process current cell
        cell = self.matrix[i][j]
        print("i =", i, " j =", j, " [", i, "][", j, "] =", cell.value)
        self.process_cell(cell, direction)

        # traverse current row, column by column
        if j < self.row_count - 1:
            self.traverse(i, j+1, direction)
        
        # if last column reached, move to next row
        elif i < self.col_count - 1:
            self.traverse(i+1, 0, direction)

    def print(self):
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print()
        print("|----------------- j -----------------|")
        print("|                                     |")
        print(''.join(['{:4}'.format(index) for index in indices]))
        print("=======================================")
        print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) 
        for row in self.matrix]))
        print()

    # pretty print hash table in json format
    def pretty_print(self, ht, label):
        print(f"{label} =\n", json.dumps(ht, indent = 4), "\n")


