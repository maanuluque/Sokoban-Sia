import heuristics

def dfs(initialNode, gameController):
    solutionPath = []
    minSteps = 0;
    statesVisited = []
    initialNode.visited = True
    statesVisited.append(initialNode.state)
    if gameController.isSolution(initialNode):
        solutionPath.append(initialNode)
        return solutionPath

    children = initialNode.getChildren(gameController)
    # TESTING (HEURISTICS)
    children = heuristics.reorganizeByBoxPlayerDistance(initialNode, children, gameController)

    # END TESTING
    for x in range(len(children)):
        found = dfsRec(children[x], statesVisited, solutionPath, gameController)
        if found:
            solutionPath.append(initialNode)
            return solutionPath


def dfsRec(node, statesVisited, solutionPath, gameController):
    if node.state in statesVisited:
        return False
    if node.board.isDeadlock():
        return False
    statesVisited.append(node.state)
    if gameController.isSolution(node):
        solutionPath.append(node)
        return True
    children = node.getChildren(gameController)
    # TESTING (HEURISTICS)
    children = heuristics.reorganizeByBoxPlayerDistance(node, children, gameController)

    # END TESTING
    for x in range(len(children)):
        found = dfsRec(children[x], statesVisited, solutionPath, gameController)
        if found:
            solutionPath.append(node)
            return True
