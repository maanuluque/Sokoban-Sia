from board import Board
from node import Node
from gameController import GameController
import constants
import numpy as np
from state import State

def testingBoard():
    return np.array([
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0", "0", "+", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "#", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "P", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
    ])

def testingBoard2():
    return np.array([
        ["1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0", "0", "+", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "#", "0", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "P", "0", "1"],
        ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
    ])

def gameSetup(board):
    return Node(board, board.whereIsP)

def main():
    hardcodedBoard = testingBoard2()
    hardcodedAlgorithm = constants.DFS
    gameBoard = Board(hardcodedBoard)

    # Print Board
    for x in range(len(gameBoard.board)):
        for y in range(len(gameBoard.board[x])):
            print(gameBoard.board[x][y], end = '')
        print()

    print("Number of boxes are: ", gameBoard.boxesNumber)
    print("Number of positions of boxes are: ", len(gameBoard.whereAreBoxes()))
    for x in gameBoard.whereAreBoxes():
        print(x)

    initialNode = gameSetup(gameBoard)
    gameController = GameController(initialNode)
    gameController.startGame(hardcodedAlgorithm)


if __name__ == "__main__":
    main()
