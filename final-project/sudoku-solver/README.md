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

1. How do I populate an initial grid with clues?

    r1 = [2, 0, 8, 0, 0, 4, 3, 0, 0]
