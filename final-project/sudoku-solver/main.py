# Sudoku Solver
# New York Times - Easy
# Sunday, October 22, 2023

from Matrix import Matrix

# define each row with the given clues
# empty cells = 0
r0 = [2, 0, 8, 0, 0, 4, 3, 0, 0]
r1 = [3, 5, 6, 0, 0, 7, 0, 0, 8]
r2 = [4, 0, 0, 8, 3, 2, 0, 6, 0]
r3 = [0, 9, 0, 0, 0, 0, 2, 0, 1]
r4 = [8, 2, 4, 0, 5, 0, 0, 0, 0]
r5 = [0, 0, 0, 0, 4, 3, 0, 9, 0]
r6 = [0, 0, 0, 3, 7, 0, 6, 5, 0]
r7 = [0, 4, 5, 6, 0, 0, 9, 7, 0]
r8 = [6, 0, 7, 4, 9, 0, 0, 8, 0]

# define array of rows
rows = [r0, r1, r2, r3, r4, r5, r6, r7, r8]

# initialize matrix
m = Matrix()

# create matrix from rows []
m.create_from_array(rows)

# traverse matrix
# m.traverse(0,0)

# backtrack matrix
#m.backtrack(8,8)

# print matrix
m.print()

# print rows ht
m.pretty_print(m.rows, "rows")

# print cols ht
#m.pretty_print(m.cols, "cols")

# print boxes ht
#m.pretty_print(m.boxes, "boxes")

m.solve()
