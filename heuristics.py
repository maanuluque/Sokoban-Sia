import math
import constants

INIT = 1000

def reorganizeByBoxGoalDistance(node, childList, gameController):
    newChildList = []
    boxesPosition = node.board.whereAreBoxes()
    goalsPosition = node.board.whereAreGoals()
    closestBox = closestBoxFromPlayer(node.board, gameController)
    closestGoalBox = closestGoalFromBox(closestBox, goalsPosition)
    distance = math.dist(closestBox, closestGoalBox)

    # In every child, we calculate if distance between box and goal has reduced.
    for x in range(len(childList)):
        child = childList[x]
        boxesPosition = child.board.whereAreBoxes()
        goalsPosition = child.board.whereAreGoals()
        childClosestBox = closestBoxFromPlayer(child.board, gameController)
        childClosestGoalFromBox = closestGoalFromBox(closestBox, goalsPosition)
        childDistance = math.dist(childClosestBox, childClosestGoalFromBox)

        if childDistance <= distance:
            newChildList.insert(0, child)
        else:
            newChildList.append(child)

    return newChildList

def reorganizeByBoxPlayerDistance(node, childList, gameController):
    newChildList = []
    playerPosition = node.board.whereIsP()
    closestBox = closestBoxFromPlayer(node.board, gameController)
    distance = math.dist(closestBox, playerPosition)
    for x in range(len(childList)):
        child = childList[x]
        childClosestBox = closestBoxFromPlayer(child.board, gameController)
        childPlayerPosition = child.board.whereIsP()
        childDistance = math.dist(childClosestBox, childPlayerPosition)
        if childDistance <= distance:
            newChildList.insert(0, child)
        else:
            newChildList.append(child)

    return newChildList

def closestBoxFromPlayer(board, gameController):
    min = INIT
    boxesPosition = board.whereAreBoxes()
    playerPosition = board.whereIsP()
    closestBox = boxesPosition[0]
    for x in range(len(boxesPosition)):
        distance = math.dist(playerPosition, boxesPosition[x])
        if (distance < min) and (boxesPosition[x] not in gameController.goalsPosition):
            closestBox = boxesPosition[x]
    return closestBox

def closestGoalFromBox(boxPosition, goalsPosition):
    min = INIT;
    for x in range(len(goalsPosition)):
        distance = math.dist(boxPosition, goalsPosition[x])
        if distance < min:
            closestGoal = goalsPosition[x]
    return closestGoal
