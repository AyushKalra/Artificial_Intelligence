import numpy as np
import time

quizzes = np.zeros((1000000, 81), np.int32)
solutions = np.zeros((1000000, 81), np.int32)
for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:300]):
    quiz, solution = line.split(",")
    for j, q_s in enumerate(zip(quiz, solution)):
        q, s = q_s
        quizzes[i, j] = q
        solutions[i, j] = s
quizzes = quizzes.reshape((-1, 9, 9))
solutions = solutions.reshape((-1, 9, 9))

# print(quizzes[0])
# print(solutions[0])
board = quizzes[0]


# ----------------------------------------------
# Check if the board follow the rule of sudoku
# ----------------------------------------------
def is_possible(_board, row, col, val):
    for _j in range(0, 9):
        if _board[row][_j] == val:
            return False

    for _i in range(0, 9):
        if _board[_i][col] == val:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(0, 3):
        for _j in range(0, 3):
            if _board[startRow + i][startCol + _j] == val:
                return False

    return True


def solve():
    _sol = board
    for _i in range(0, 9):
        for _j in range(0, 9):
            if board[_i][_j] == 0:
                for val in range(1, 10):
                    if is_possible(board, _i, _j, val):
                        board[_i][_j] = val
                        solve()

                        # Bad choice, make it blank and go back
                        board[_i][_j] = 0
                return
    # print(board)


start = time.time()

for index in range(0, 200):
    board = quizzes[index]
    solve()
    # print(sol)
    # print('------------')
    # print(solutions[index])

end = time.time()
time_spent = end - start

print("The average time to solve a single sudoku is:", time_spent / 200)
