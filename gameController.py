import dfs
import constants

class GameController:
    def __init__(self, initialNode):
        self.initialNode = initialNode
        self.solution = False
        self.goalsPosition = initialNode.board.whereAreGoals()

    def startGame(self, algorithm):
        print("Game Started :)")
        print()

        children = self.initialNode.getChildren(self)

        if algorithm == constants.DFS:
            # Pass GameController as parameter to provide dfs with information
            solutionPath = dfs.dfs(self.initialNode, self)
            if len(solutionPath) != 0:
                solutionPath.reverse()
                print("STEPS:")
                for x in range(len(solutionPath)):
                    solutionPath[x].board.print()
                    print()
                print("Results: Solution Found!")
                print("Number of Steps: ", len(solutionPath))
            else:
                print("No solution found :(")

    def isSolution(self, node):
        # for x in range(node.board.rows):
        #     for y in range(node.board.cols):
        #         if node.board.board[x][y] == constants.OBJECTIVE:
        #             return False
        # if node.board.whereIsP() not in self.goalsPosition:
        #             return False
        # return True
        success = True
        for iter in range(len(self.goalsPosition)):
            x = self.goalsPosition[iter][0]
            y = self.goalsPosition[iter][1]
            boxInGoal = node.board.board[x][y] == constants.BOX
            playerInGoal = node.board.whereIsP() in self.goalsPosition

            success = success and boxInGoal and not playerInGoal
        return success
