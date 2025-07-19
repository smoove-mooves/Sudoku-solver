# Sudoku-solver
This program is a Sudoku puzzle solver that presents the user with a customtkinter GUI.

How to use the program:

-Step 1: Run the program's main.py file and enter the given numbers from the puzzle you are trying to solve into the grid.

-Step 2: Click "Submit Puzzle". This stores the given numbers into a 2D list.

-Step 3: Click "Solve Puzzle".

-Step 4: If you have another puzzle you would like to solve, click "Clear Puzzle" and start over at step 2.

# Contents of the files
main.py:
- main function to launch the program

solver.py:
- solver function which uses backtracking to solve the puzzle.
- check_validity function which is called by the solver function to verify that a proposed number does not violate the rules of sudoku.

sudoku_app.py:
- contains the SudokuApp class.
- the SudokuApp class has functions to create the GUI, store user input, display whether or not the puzzle has been solved, and to clear the grid.
- contains functionality to verify that the user does not type invalid numbers or valid numbers in an order that violates the rules of sudoku.
