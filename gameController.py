import dfs
import constants

class GameController:
    def __init__(self, initialNode):
        self.initialNode = initialNode
        self.isSolution = False

    def startGame(self, algorithm):
        print("Game Started :)")
        print()

        children = self.initialNode.getChildren()

        if algorithm == constants.DFS:
            solutionPath = dfs.dfs(self.initialNode)
            if len(solutionPath) != 0:
                print("Results: Solution Found!")
                print("Number of Steps: ", len(solutionPath))
                print("STEPS:")
                for x in range(len(solutionPath)):
                    solutionPath[x].board.print()
                    print()
            else:
                print("No solution found :(")
