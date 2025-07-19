import customtkinter as ctk
import sudoku_app


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    app = sudoku_app.SudokuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
