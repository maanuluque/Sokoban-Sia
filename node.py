import constants
from board import Board
from state import State

class Node:
    def __init__(self, board, player):
        self.visited = False
        self.board = board
        self.player = player
        self.state = State(self.board.whereIsP(), self.board.whereAreBoxes())

    def getChildren(self):
        children = []
        if not self.board.ilegalMove(constants.UP):
            upBoard = Board(self.board.makeMove(constants.UP))
            upNode = Node(upBoard, upBoard.whereIsP())
            children.append(upNode)
        if not self.board.ilegalMove(constants.DOWN):
            downBoard = Board(self.board.makeMove(constants.DOWN))
            downNode = Node(downBoard, downBoard.whereIsP())
            children.append(downNode)
        if not self.board.ilegalMove(constants.LEFT):
            leftBoard = Board(self.board.makeMove(constants.LEFT))
            leftNode = Node(leftBoard, leftBoard.whereIsP())
            children.append(leftNode)
        if not self.board.ilegalMove(constants.RIGHT):
            rightBoard = Board(self.board.makeMove(constants.RIGHT))
            rightNode = Node(rightBoard, rightBoard.whereIsP())
            children.append(rightNode)

        return children

    def isSolution(self):
        goalFound = False
        for x in range(self.board.rows):
            for y in range(self.board.cols):
                if self.board.board[x][y] == constants.OBJECTIVE:
                    goalFound = True
                if goalFound:
                    return False
        return True
