def dfs(initialNode):
    solutionPath = []
    minSteps = 0;
    statesVisited = []
    initialNode.visited = True
    statesVisited.append(initialNode.state)
    if initialNode.isSolution():
        solutionPath.append(initialNode)
        return solutionPath

    children = initialNode.getChildren()
    for x in range(len(children)):
        found = dfsRec(children[x], statesVisited, solutionPath)
        if found:
            solutionPath.append(initialNode)
            return solutionPath


def dfsRec(node, statesVisited, solutionPath):
    if node.state in statesVisited:
        return False
    if node.board.isDeadlock():
        return False
    statesVisited.append(node.state)
    if node.isSolution():
        solutionPath.append(node)
        return True
    children = node.getChildren()
    for x in range(len(children)):
        found = dfsRec(children[x], statesVisited, solutionPath)
        if found:
            solutionPath.append(node)
            return True
