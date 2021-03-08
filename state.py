class State:
    def __init__(self, playerPosition, boxesPosition):
        self.playerPosition = playerPosition
        self.boxesPosition = boxesPosition
        self.boxesNumber = len(boxesPosition)

    def __eq__(self, state):
        if self.boxesNumber != state.boxesNumber:
            return False
        equalBoxes = True
        iter = 0
        while equalBoxes and (iter < self.boxesNumber):
            equalBoxes = equalBoxes and (self.boxesPosition[iter] == state.boxesPosition[iter])
            iter += 1

        return (self.playerPosition == state.playerPosition) and equalBoxes
