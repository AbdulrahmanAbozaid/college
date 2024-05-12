"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = util.Stack()
    visited = set()

    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        current_state, actions = stack.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)

            for successor, action, _ in successors:
                if successor not in visited:
                    stack.push((successor, actions + [action]))
    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    # paths = util.PriorityQueue()
    visited = dict()

    queue.push((problem.getStartState(), [], 0))

    while not queue.isEmpty():
        current_state, actions, cost = queue.pop()

        if problem.isGoalState(current_state):
            return actions
            # paths.push(actions, cost)
            # continue

        if current_state not in visited or cost < visited[current_state]:
            visited[current_state] = cost
            successors = problem.getSuccessors(current_state)

            for successor, action, step_cost in successors:
                total_cost = cost + step_cost
                if successor not in visited or total_cost < visited[successor]:
                    queue.push((successor, actions + [action], total_cost))
    # if paths.isEmpty():
    util.raiseNotDefined()
    # else:
    # return paths.pop()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the path that has the lowest combined cost and heuristic first."""
    paths = util.PriorityQueue()
    paths.push((problem.getStartState(), []), 0)
    visited = set()

    while not paths.isEmpty():
        (current_state, actions) = paths.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state in visited:
            continue

        visited.add(current_state)

        for successor, action, cost in problem.getSuccessors(current_state):
            if successor not in visited:
                paths.push(
                    (successor, actions + [action]),
                    cost + heuristic(successor, problem),
                )
    return False


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
