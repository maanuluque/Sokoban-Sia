import constants
import numpy as np

class Board:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.boxesNumber = 0
        for x in range(self.rows):
            for y in range(self.cols):
                if board[x][y] == '#':
                    self.boxesNumber += 1


    def whereIsP(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 'P':
                    return x, y
        return 0,0

    def whereAreBoxes(self):
        if self.boxesNumber == 0:
            return 0,0
        boxesPosition = []
        for x in range(self.rows):
            for y in range(self.cols):
                if self.board[x][y] == '#':
                    boxesPosition.append((x,y))
        return boxesPosition

    def print(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.board[x][y], end = '')
            print()

    def isDeadlock(self):
        boxesPosition = self.whereAreBoxes()
        for x in range(self.boxesNumber):
            if self.countWallsAround(boxesPosition[x]) >= 2:
                return True
        return False

    def countWallsAround(self, position):
        row = position[0]
        col = position[1]
        up, down, left, right = False, False, False, False
        ones = 0
        if self.board[row - 1][col] == constants.WALL:
            ones += 1
            up = True
        if self.board[row + 1][col] == constants.WALL:
            ones += 1
            down = True
        if self.board[row][col - 1] == constants.WALL:
            ones += 1
            left = True
        if self.board[row][col + 1] == constants.WALL:
            ones += 1
            right = True
        if (left and right) and (not (up and down)):
            return 0
        if (up and down) and (not (left and right)):
            return 0
        return ones

    # def numberOfBoxes(self):
    #     boxesNumber = 0;
    #     for x in range(len(self.board)):
    #         for y in tange(len(self.board[x])):
    #             if board[x][y] == '#':
    #                 ++boxesNumber
    #     return boxesNumber



    def ilegalMove(self, direction):
        row, col = self.whereIsP()

        if direction == constants.UP:
            if(row - 1 < 0) or (self.board[row - 1][col] == constants.WALL):
                return True
            elif (self.board[row - 1][col] == constants.BOX) and ((row - 2 < 0) or self.board[row - 2][col] == constants.WALL):
                return True
            else: return False
        if direction == constants.DOWN:
            if(row + 1 >= self.rows) or (self.board[row + 1][col] == constants.WALL):
                return True
            elif (self.board[row + 1][col] == constants.BOX) and ((row + 2 >= self.rows) or self.board[row + 2][col] == constants.WALL):
                return True
            else: return False
        if direction == constants.LEFT:
            if(col - 1 < 0) or (self.board[row][col - 1] == constants.WALL):
                return True
            elif (self.board[row][col - 1] == constants.BOX) and ((col - 2 < 0) or self.board[row][col - 2] == constants.WALL):
                return True
            else: return False
        if direction == constants.RIGHT:
            if(col + 1 >= self.cols) or (self.board[row][col + 1] == constants.WALL):
                return True
            elif (self.board[row][col + 1] == constants.BOX) and ((col + 2 >= self.cols) or self.board[row][col + 2] == constants.WALL):
                return True
            else: return False

        return True

    def makeMove(self, direction):
        xPlayer, yPlayer = self.whereIsP()
        nextRow = xPlayer
        nextCol = yPlayer
        newBoard = np.copy(self.board)

        if direction == constants.UP:
            nextRow -= 1
            if self.board[nextRow][nextCol] == constants.EMPTY:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
            if self.board[nextRow][nextCol] == constants.BOX:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
                newBoard[nextRow - 1][nextCol] = constants.BOX
            return newBoard

        if direction == constants.DOWN:
            nextRow += 1
            if self.board[nextRow][nextCol] == constants.EMPTY:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
            if self.board[nextRow][nextCol] == constants.BOX:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
                newBoard[nextRow + 1][nextCol] = constants.BOX
            return newBoard

        if direction == constants.LEFT:
            nextCol -= 1
            if self.board[nextRow][nextCol] == constants.EMPTY:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
            if self.board[nextRow][nextCol] == constants.BOX:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
                newBoard[nextRow][nextCol - 1] = constants.BOX
            return newBoard

        if direction == constants.RIGHT:
            nextCol += 1
            if self.board[nextRow][nextCol] == constants.EMPTY:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
            if self.board[nextRow][nextCol] == constants.BOX:
                newBoard[xPlayer][yPlayer] = constants.EMPTY
                newBoard[nextRow][nextCol] = constants.PLAYER
                newBoard[nextRow][nextCol + 1] = constants.BOX
            return newBoard
