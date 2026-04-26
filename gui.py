import tkinter as tk
from tkinter import messagebox

from algorithms import bfs, dfs, astar
from utils import is_solvable, generate_random_board


class PuzzleGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("8 Puzzle Solver")

        self.entries = []
        self.solution_path = None

        self.create_grid()
        self.create_buttons()

        self.result_label = tk.Label(
            root,
            text="Enter numbers 0-8 (0 = blank)",
            font=("Arial", 12)
        )

        self.result_label.grid(row=7, column=0, columnspan=3, pady=10)

    def create_grid(self):

        for i in range(3):

            row = []

            for j in range(3):

                entry = tk.Entry(
                    self.root,
                    width=5,
                    font=("Arial", 22),
                    justify="center"
                )

                entry.grid(row=i, column=j, padx=5, pady=5)

                row.append(entry)

            self.entries.append(row)

    def create_buttons(self):

        tk.Button(self.root, text="Solve BFS", command=self.solve_bfs, bg="lightgreen", width=12).grid(row=3, column=0)
        tk.Button(self.root, text="Solve DFS", command=self.solve_dfs, bg="lightblue", width=12).grid(row=3, column=1)
        tk.Button(self.root, text="Solve A*", command=self.solve_astar, bg="orange", width=12).grid(row=3, column=2)

        tk.Button(self.root, text="Random", command=self.random_board, bg="yellow", width=12).grid(row=4, column=0)
        tk.Button(self.root, text="Show Steps", command=self.show_steps, bg="lightgray", width=12).grid(row=4, column=1)
        tk.Button(self.root, text="Reset", command=self.reset_board, bg="lightcoral", width=12).grid(row=4, column=2)

    def get_board(self):

        board = []

        try:
            for i in range(3):
                row = []
                for j in range(3):
                    val = int(self.entries[i][j].get())

                    if val < 0 or val > 8:
                        raise ValueError

                    row.append(val)

                board.append(row)

            return board

        except:
            messagebox.showerror("Error", "Enter valid numbers 0-8")
            return None

    def fill_board(self, board):

        for i in range(3):
            for j in range(3):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, board[i][j])

    def solve_bfs(self):

        board = self.get_board()
        if not board:
            return

        if not is_solvable(board):
            messagebox.showinfo("Result", "Puzzle not solvable")
            return

        path, nodes, t = bfs(board)

        if path:
            self.solution_path = path
            self.result_label.config(text=f"BFS | Steps:{len(path)-1} | Nodes:{nodes} | Time:{round(t,3)}s")

    def solve_dfs(self):

        board = self.get_board()
        if not board:
            return

        if not is_solvable(board):
            messagebox.showinfo("Result", "Puzzle not solvable")
            return

        path, nodes, t = dfs(board)

        if path:
            self.solution_path = path
            self.result_label.config(text=f"DFS | Steps:{len(path)-1} | Nodes:{nodes} | Time:{round(t,3)}s")

    def solve_astar(self):

        board = self.get_board()
        if not board:
            return

        if not is_solvable(board):
            messagebox.showinfo("Result", "Puzzle not solvable")
            return

        path, nodes, t = astar(board)

        if path:
            self.solution_path = path
            self.result_label.config(text=f"A* | Steps:{len(path)-1} | Nodes:{nodes} | Time:{round(t,3)}s")

    def random_board(self):

        board = generate_random_board()
        self.fill_board(board)
        self.result_label.config(text="Random board generated")

    def show_steps(self):

        if not self.solution_path:
            messagebox.showinfo("Info", "Solve puzzle first")
            return

        window = tk.Toplevel(self.root)
        window.title("Solution Steps")

        text = tk.Text(window, width=25, height=25, font=("Courier", 14))
        text.pack()

        for step, board in enumerate(self.solution_path):

            text.insert(tk.END, f"Step {step}\n")

            for row in board:
                text.insert(tk.END, f"{row}\n")

            text.insert(tk.END, "\n")

    def reset_board(self):

        for i in range(3):
            for j in range(3):
                self.entries[i][j].delete(0, tk.END)

        self.result_label.config(text="Board reset")