import customtkinter as ctk
import solver


# This class creates the GUI with the Sudoku grid using custom tkinter
class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.grid = []

        cell_size = 50
        padding = 2

        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = ctk.CTkEntry(self.root, width=cell_size, height=cell_size, font=("Arial", 18), justify='center',
                                     corner_radius=5)
                entry.grid(row=row, column=col, padx=padding, pady=padding)
                row_entries.append(entry)
            self.grid.append(row_entries)

        # Creates the label for the error message that occurs when an invalid input is detected in the grid
        self.error_label = ctk.CTkLabel(self.root, text="", text_color="red", font=("Arial", 12))
        self.error_label.grid(row=9, column=0, columnspan=9)

        # Creates the button used to collect user input values
        self.submit_button = ctk.CTkButton(self.root, text="Submit Puzzle", command=self.user_input)
        self.submit_button.grid(row=10, column=0, columnspan=9, pady=10)

        # Creates the button used to solve the puzzle
        self.solve_button = ctk.CTkButton(self.root, text="Solve Puzzle", command=self.solve_puzzle)
        self.solve_button.grid(row=11, column=0, columnspan=9, pady=10)

        # Creates the button that can clear the grid of all values
        self.clear_button = ctk.CTkButton(self.root, text="Clear Puzzle", command=self.clear_puzzle)
        self.clear_button.grid(row=12, column=0, columnspan=9, pady=10)

        self.draw_bold_lines(cell_size, padding)

    # This function creates the bold lines on the GUI and evenly spaces them apart
    def draw_bold_lines(self, cell_size, padding):
        line_thickness = .6
        offset = padding // 2

        i = 3.1
        while i < 9.3:
            # This draws the vertical lines
            line_x = i * (cell_size + padding) - offset
            ctk.CTkCanvas(self.root, width=line_thickness, height=9.6 * cell_size, bg="black").place(x=line_x, y=1.25)

            # This draws the horizontal lines
            line_y = i * (cell_size + padding) - offset
            ctk.CTkCanvas(self.root, width=9.6 * cell_size, height=line_thickness, bg="black").place(x=1.25, y=line_y)
            i += 3.1

    # This function collects the user input and stores it in a 2D list
    def user_input(self):
        self.sudoku_input = []
        self.error_label.configure(text="")

        for row in range(9):
            row_data = []
            for col in range(9):
                entry_value = self.grid[row][col].get()
                if entry_value.isdigit():
                    num = int(entry_value)
                    row_data.append(num)
                else:
                    row_data.append(0)
            self.sudoku_input.append(row_data)

        for row in range(9):
            for col in range(9):
                num = self.sudoku_input[row][col]
                if num != 0:
                    if num < 1 or num > 9:
                        self.error_label.configure(text="Please double check your typing.")
                        return

                    if num in self.sudoku_input[row][:col]:
                        self.error_label.configure(text="Please double check your typing.")
                        return

                    for r in range(9):
                        if self.sudoku_input[r][col] == num and r != row:
                            self.error_label.configure(text="Please double check your typing.")
                            return

                    # Check for duplicates in the 3x3 subgrid
                    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
                    for r in range(start_row, start_row + 3):
                        for c in range(start_col, start_col + 3):
                            if self.sudoku_input[r][c] == num and (r != row or c != col):
                                self.error_label.configure(text="Please double check your typing.")
                                return

        print("Collected Sudoku Puzzle:")
        for row in self.sudoku_input:
            print(row)

    # This function solves the puzzle by calling the solver function from solver.py and updates the grid.
    def solve_puzzle(self):
        board = [row[:] for row in self.sudoku_input]

        if solver.solver(board):
            self.update_puzzle(board)
            print("Puzzle solved! Great job!")
        else:
            print("No solution exists! Please verify you typed the given numbers in their correct position on the grid.")

    # This function updates the grid
    def update_puzzle(self, board):
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                self.grid[row][col].delete(0, 'end')
                if value != 0:
                    self.grid[row][col].insert(0, str(value))

    # This function clears the grid and resets the user input
    def clear_puzzle(self):
        self.sudoku_input = [[0 for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                self.grid[row][col].delete(0, 'end')
