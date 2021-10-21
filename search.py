# 1306190041 kerem inci
# 20/10/21

class Node:

    def __init__(self,state = [], depth = 0 ):
        self.state = state
        self.depth = depth
    
    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state
        

def printState(node):
    
    state = node.state
    for i in range(9):
        if i % 3 == 0:
            print("\n")
    print(state[i], end=" ")
        
    print("\n")
        



def createNode(state):
    return Node(state)


def move_up(state):
    new_state = state[:]
    index = new_state.index(-1)

    if index not in [0,1,2]:
        temp = new_state[index - 3] #bosluk ustunde
        new_state[index - 3] = -1
        new_state[index] = temp

        return new_state
    else :
        return None

def move_down(state):
    new_state = state[:]
    index = new_state.index(-1)

    if index not in [6,7,8]:
        temp = new_state[index + 3] #bosluk olmayan
        new_state[index + 3] = -1
        new_state[index] = temp

        return new_state
    else :
        return None


def move_right(state):
    new_state = state[:]
    index = new_state.index(-1)

    if index not in [2,5,8]:
        temp = new_state[index + 1] #bosluk olmayan
        new_state[index + 1] = -1
        new_state[index] = temp

        return new_state
    else :
        return None

def move_left(state):
    new_state = state[:]
    index = new_state.index(-1)

    if index not in [0,3,6]:
        temp = new_state[index - 1] #bosluk olmayan
        new_state[index - 1] = -1
        new_state[index] = temp

        return new_state
    else :
        return None

def inc_depth(nodes):
    for node in nodes:
        node.depth = node.depth + 1
    return nodes
    
def expand(node):
    depth = node.depth
    nodes = [createNode(move_up(node.state)), 
    createNode(move_down(node.state)),
    createNode(move_left(node.state)), 
    createNode(move_right(node.state))]

    for node in nodes:
        node.depth = depth + 1

    return [node for node in nodes if node.state != None]

    

def bfs(start, goal):
    queue = []
    queue.append(start)

    while len(queue) > 0:
        printState(queue[0])

        if queue[0].state == goal.state:
            return True #success 
        else:
            node = queue.pop(0)
            queue = queue + expand(node)


def dfs(start, goal):
    stack = []
    stack.append(start)

    while len(stack) > 0:
        printState(stack[0])

        if stack[0].state == goal.state:
            return True #success 
        else:
            node = stack.pop()
            stack =  expand(node) + stack



def dls(start, goal, depth):
    queue = []
    queue.append(start)

    while len(queue) > 0:
        printState(queue[0])

        if queue[0].depth > depth:
            return #stop 

        if queue[0].state == goal.state:
            return True #success 
        else:
            node = queue.pop(0)
            queue = queue + expand(node)


def iterative_deeping(start, goal, cutoff):
    depth = 0

    while depth < cutoff:

        if dls(start, goal, depth) == True:
            return True
        else:
            depth = depth + 1








start = Node([7, 2, 4, 5, -1, 6, 8, 3, 1])
goal = Node([-1, 1, 2, 3, 4, 5, 6, 7, 8])

# bfs(start, goal)
# dfs(start,goal, 5)
# iterative_deeping(start,goal, 5
# dls(start, goal, 5)