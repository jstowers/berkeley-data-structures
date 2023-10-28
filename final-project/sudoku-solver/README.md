# __Sudoku Solver__


## Terminology

1. column - a vertical section consisting of 9 cells, with each cell holding an integer from 1 to 9

2. row - a horizontal section consisting of 9 cells, wich each cell holding an integer from 1 to 9

3. cell - an individual square with a value from 1 to 9.

4. box - a 3 x 3 square containing 9 cells, with each cell holding an integer from 1 to 9


## Algorithm

TODO:

1. Create a Matrix class to traverse, reference, and print a 9 x 9 matrix, filled by (9) 3x3 boxes.

    a. create a 9 x 9 matrix

    b. fill it with values

    c. reference individual values

    d. write a recursive traversal method

2. Create a Cell class with the following properties

    a. i coordinate

    b. j coordinate

    c. value

    d. is_clue

3. Create hash tables for each row, column, and box:

        r0 = {}

        c1 = {}

        b4 = {}


    ```python

        r0 = {
            1 : {
                i:
                j:
                is_clue: True
            },
            2: {

            }
        }
    ```

    A row, column, or box is successfully completed when it contains all 9 integers.

    When all rows, columns, and boxes are filled, the game is won.



2. Keep track of guesses and given clues.  If I need to backtrack, I can't delete a clue.  I can only delete the guesses.

3. Keep track of the clues and guess in each row, column, and box.


## Questions

1. How do I populate an initial grid with clues?  DONE 10/22/23

    r1 = [2, 0, 8, 0, 0, 4, 3, 0, 0]


2. How do I start the iteration process?


3. How do I create the hash tables?  DONE 10/23/23

--- 

Wednesday, October 25, 2023
8:30 pm CDT
flying to Albuquerque

TODO:

1. Create 9 boxes, A - I, with range values for the rows and columns

        Box A                   Box B                   Box C
                 j                       j                      j
        -------------------     -------------------     -------------------
        | 0,0   0,1   0,2 |     | 0,3   0,4   0,5 |     | 0,6   0,7   0,8 |
      i | 1,0   1,1   1,2 |     | 1,3   1,4   1,5 |     | 1,6   1,7   1,8 |
        | 2,0   2,1   2,2 |     | 2,3   2,4   2,5 |     | 2,6   2,7   2,8 |
        -------------------     -------------------     -------------------

    Box   i_lo   i_hi   j_lo   j_hi
    -------------------------------
    A     0      2      0      2
    B     0      2      3      5
    C     0      2      6      8
    D     3      5      0      2
    E     3      5      3      5

    NOTE: all brackets are inclusive values

    [0, 2] : [0, 2] => A 
             [3, 5] => B
             [6, 8] => C



    [3, 5] : 


    Now, what if I shorten the structure to just the first value and
    use a comparison.  In order for this to work, I have to know the current comparison value and the next.

    0:
        0:  A
        3:  B       >= 3 and < 6 (the next key)
        6:  C

    3:
        0:  D
        3:  E
        6:  F

    6:
        0   G
        3   H
        6   I

    








    Box A       i <= 2 AND j <=2

    Box B       i <= 2 AND j > 2 AND j <= 5

    Box C       i <= 2 AND j > 5

    Box D       i > 2 AND i <= 5 AND j <= 2

    Box E       i > 2 AND i <= 5 AND j > 2 AND j <= 5

    Box F       i > 2 AND i <= 5 AND j > 5

    Box G       i > 5 AND j <= 2

    Box H       i > 5 AND j > 2 AND j <= 5

    BOX I       i > 5 AND j > 5

#
def getBox(cell):
    i = cell.i
    j = cell.j

    return box_ht[i][j]


ex) Cell(3, 3, 8, True)

    What if I have a ht or array with lo and hi values?

    i = {
        0: ["A", "B", "C"]
        1: A, B, C
        2: A, B, C
        3: D, E, F
        4: D, E, F
        5: D, E, F
        6: G, H, I
        7: G, H, I
        8: G, H, I
    }

    j = {
        0: A, D, G
        1: A, D, G
        2: A, D, G
        3: B, E, H
        4: B, E, H
        5: B, E, H
        6: C, F, I
        7: C, F, I
        8: C, F, I
    }

    What if I generate a HT of the Boxes based on coordinates

    {
        0: {
            0: A
            1: A
            2: A
            3: B
            4:
        }
    }


    What Box is Cell(3, 3) in?

        i =  D, E, F
        j =  B, E, H
 
    The only Box that fits is E.  So how do I pick that off quickly.




    box_range = { 

        2: 



        A : {
            i_lo: 0,
            i_hi: 2,
            j_lo: 0,
            j_hi: 2
        } 


    }


2. I need to write a function that receives a Cell and determines what Box it is in.  From there, I need to have a hash table of Cells within the Box. => DONE!

The Cell object has a property called `box_value` that stores the Box value.

I also created a boxes hash table to store the values 1 -> 9 for each Box A -> I.




# Backtracking Algorithm

1. Start at cell in upper left corner, i = 0, j = 0

2. Does that cell have a clue?
   
    cell = self.matrix[i][j].is_clue

    YES: 
        # forward
        skip cell and go forward to next cell
            traverse(i, j + 1)

        # backtrack
        skip cell and go backward to previous cell
            traverse(i, j - 1)

    NO: set temp_value = 1

        # does row[i] have temp_value?
        while self.rows[i][temp_value][is_present] == True:

            YES: increment temp_value by 1
            temp_value += 1

        # does col[j] have temp value?
        while sels.cols[j][temp_value][is_present] == True:

                YES: increment temp_value by 1
                temp_value += 1

        # does box holding [i][j] have temp_value?
        current_box = matrix[i][j].box_value
        while self.boxes[current_box][temp_value][is_present] == True:
                
                YES: increment temp_value by 1
                temp_value += 1

        # 1. Assign Value
        # temp_value <= 9 so assign cell the temp value
        if temp_value <= 9
            self.matrix[i][j].value = temp_value
            traverse(i, j+1)

        # 2. Backtrack
        # temp_value == 10
        # indicates a violation and need to backtrack
            backtrack(i, j-1)





In col 7, I have my first conflict:

    temp = 7, 9

    col = x7, x8, x9

So I have to go backward and change 1 or more of
my guesses:
            Can Be    Guess1    Guess2
    col1     1, 7       1         7
    col3     1, 5, 9    5
    col4     1, 6       6
    col7     1          ?         1





