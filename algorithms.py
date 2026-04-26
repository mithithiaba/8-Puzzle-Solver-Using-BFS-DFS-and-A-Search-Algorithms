import time
import heapq
from collections import deque

from state import PuzzleState
from constants import GOAL_STATE
from utils import manhattan_distance, reconstruct_path


def bfs(start_board):

    start_time = time.time()

    start = PuzzleState(start_board)

    queue = deque([start])

    visited = set([start])

    nodes = 0

    while queue:

        current = queue.popleft()

        nodes += 1

        if current.board == GOAL_STATE:
            return reconstruct_path(current), nodes, time.time() - start_time

        for child in current.generate_children():

            if child not in visited:
                visited.add(child)
                queue.append(child)

    return None, nodes, time.time() - start_time


def dfs(start_board, max_depth=50):

    start_time = time.time()

    start = PuzzleState(start_board)

    stack = [start]

    visited = set([start])

    nodes = 0

    while stack:

        current = stack.pop()

        nodes += 1

        if current.board == GOAL_STATE:
            return reconstruct_path(current), nodes, time.time() - start_time

        if current.depth < max_depth:

            for child in current.generate_children():

                if child not in visited:
                    visited.add(child)
                    stack.append(child)

    return None, nodes, time.time() - start_time


def astar(start_board):

    start_time = time.time()

    start = PuzzleState(start_board)

    start.cost = manhattan_distance(start.board)

    open_list = []

    heapq.heappush(open_list, start)

    visited = set()

    nodes = 0

    while open_list:

        current = heapq.heappop(open_list)

        nodes += 1

        if current.board == GOAL_STATE:
            return reconstruct_path(current), nodes, time.time() - start_time

        visited.add(current)

        for child in current.generate_children():

            if child in visited:
                continue

            g = child.depth
            h = manhattan_distance(child.board)

            child.cost = g + h

            heapq.heappush(open_list, child)

    return None, nodes, time.time() - start_time