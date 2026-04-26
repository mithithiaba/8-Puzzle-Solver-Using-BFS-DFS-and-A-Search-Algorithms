import copy

class PuzzleState:

    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __lt__(self, other):
        return self.cost < other.cost

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate_children(self):
        children = []
        x, y = self.get_blank_position()

        moves = {
            "Up": (x-1, y),
            "Down": (x+1, y),
            "Left": (x, y-1),
            "Right": (x, y+1)
        }

        for move, (nx, ny) in moves.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = copy.deepcopy(self.board)

                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

                children.append(
                    PuzzleState(new_board, self, move, self.depth + 1)
                )

        return children