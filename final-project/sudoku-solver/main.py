# Sudoku Solver
# Joseph Stowers
# Tuesday, October 31, 2023
# COMPSCIX404.1-015 Final Project

from Matrix import Matrix

# New York Times - Easy
# Sunday, October 22, 2023
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

print("\nWelcome to Sudoku 数独 Solver!\n")
print("crafted with pride in Austin, Texas 🤠")
print("© Copyright Joseph Stowers 2023\n")

print("            Happy 🎃 Halloween!")

# print initial sudoku grid
print("\n**********  initial sudoku grid  ***********")
m.print()

print("***************  grid data  ***************\n")

# number of clues
print(f'  clues = {m.clues_count():-2}')

# number of empty cells
print("  empty =", m.empty_cells_count())

# total cells
print(f"  total = {m.cell_count}")

# print rows ht
#m.pretty_print(m.rows, "rows")

# print cols ht
#m.pretty_print(m.cols, "cols")

# print boxes ht
#m.pretty_print(m.boxes, "boxes")

# solve sudoku
print("\n***************  iterations  **************\n")
m.solve()

