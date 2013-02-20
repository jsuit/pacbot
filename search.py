# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           
class SearchNode:
    
    def __init__(self, s, p=None, a=None, c=0, h=0):
        self.state = s
        self.parent = p
        self.action = a
        self.cost   = c
        self.hx     = h
    
    def __eq__(self, other):
        return self.state == other.state

    def __repr__(self): 
        return str(self.state)

class SearchStruct:
    
    def hasMore(self, node):
        util.raiseNotDefined()

    def push(self, node):
        util.raiseNotDefined()
        
    def pop(self, node):
        util.raiseNotDefined()

"""
  An implementation of a simple stack (LIFO), used to implement DFS with general graph search.
  This implementation maintains a visited list, to ensure the graph search is efficient.
"""
class SearchStack(SearchStruct):

    def __init__(self):
        self.stack = []
        self.visited = []
    
    def hasMore(self):
        return self.stack

    def push(self, node):
        if (node not in self.visited):
          self.stack.append(node)  
          "Add to the visited list here, because we use it above for deduplication"
          self.visited.append(node)

    def pop(self):
        node = self.stack.pop()
        return node

    def count(self):
        return len(self.stack)

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].
  
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
  
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    found = None
    struct = SearchStack()
    print struct.hasMore()
    struct.push(SearchNode(problem.getStartState()))
    while (struct.hasMore()):
        node = struct.pop()
        print "Checking ", node, " with cost ", node.cost, ", ", struct.count(), " left"
        if (problem.isGoalState(node.state)):
            print "Found goal state"
            found = node
            break
        else:
            successors = problem.getSuccessors(node.state)
            for successor, action, cost in successors:
                print "Adding node ", successor, " with path cost ", node.cost , " and step cost ", cost
                "Add the node to the structure with an accumulated cost"
                struct.push(SearchNode(successor, node, action, node.cost + cost))
                
    "Build the action list starting from the goal state"
    pathToGoal = []
    print found;
    "A parent of None indicates the start state"
    "NOTE: this builds the path backwards..."
    while (found.parent is not None):
        pathToGoal.append(found.action)
        found = found.parent
    
    "reverse before we return"
    pathToGoal.reverse();
    print "Found actions to goal: ", pathToGoal
    return pathToGoal

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch