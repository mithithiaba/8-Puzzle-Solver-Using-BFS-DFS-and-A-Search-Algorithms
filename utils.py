import random

def manhattan_distance(board):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = board[i][j]

            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3

                distance += abs(i - goal_x) + abs(j - goal_y)

    return distance


def reconstruct_path(state):
    path = []

    while state:
        path.append(state.board)
        state = state.parent

    return path[::-1]


def is_solvable(board):
    flat = [num for row in board for num in row if num != 0]

    inversions = 0

    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1

    return inversions % 2 == 0


def generate_random_board():
    nums = list(range(9))

    while True:
        random.shuffle(nums)

        board = [
            nums[0:3],
            nums[3:6],
            nums[6:9]
        ]

        if is_solvable(board):
            return board