import constants
from board import Board
from state import State

class Node:
    def __init__(self, board, player):
        self.visited = False
        self.board = board
        self.player = player
        self.state = State(self.board.whereIsP(), self.board.whereAreBoxes())

        # In case optimal DFS is needed
        self.solution = False
        self.deep = -1
        self.tail = None

    def getChildren(self, gameController):
        children = []
        if not self.board.ilegalMove(constants.UP):
            upBoard = Board(self.board.makeMove(constants.UP, gameController.goalsPosition))
            upNode = Node(upBoard, upBoard.whereIsP())
            children.append(upNode)
        if not self.board.ilegalMove(constants.DOWN):
            downBoard = Board(self.board.makeMove(constants.DOWN, gameController.goalsPosition))
            downNode = Node(downBoard, downBoard.whereIsP())
            children.append(downNode)
        if not self.board.ilegalMove(constants.LEFT):
            leftBoard = Board(self.board.makeMove(constants.LEFT, gameController.goalsPosition))
            leftNode = Node(leftBoard, leftBoard.whereIsP())
            children.append(leftNode)
        if not self.board.ilegalMove(constants.RIGHT):
            rightBoard = Board(self.board.makeMove(constants.RIGHT, gameController.goalsPosition))
            rightNode = Node(rightBoard, rightBoard.whereIsP())
            children.append(rightNode)

        return children
