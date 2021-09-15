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
           
class Node:
    #knows its parents (tuple)
    #knows itself

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
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  #initialize frontier and explored
  frontier = util.Stack() #initilize frontier structure
  successors = problem.getSuccessors(problem.getStartState()) #successor states ((x,y), 'N/S/E/W', 1) / (pos, act, cost)
  for s in successors:
      frontier.push(s) #add successors to frontier

  explored = {problem.getStartState : True} #initilize explored dictionary

  solution = util.Stack() #solution?

  while not frontier.isEmpty(): #while frontier not empty
      print "frontier: ", frontier.list
      node = frontier.pop()      # choose a leaf node and remove it from the frontier
      solution.push(node)
      print "solution so far: ", solution.list
      if problem.isGoalState(node):  # if the node contains a goal state
          #get rid of extraneous info
          return solution # return list of actions from start state to goal state
      explored[node[0]] = True # add the state key to the explored dictionary
      successors = problem.getSuccessors(node)
      # if len(successors) == 0:
      #     foo = solution.pop()
      #     if foo[1] is 'North':
      #         newcord = foo[0] + (0,-1)
      #         frontier.push(newcord)
      #     elif foo[1] is 'East':
      #         newcord = foo[0] + (-1, 0)
      #         frontier.push(newcord)
      #     elif foo[1] is 'South':
      #         newcord = foo[0] + (0, 1)
      #         frontier.push(newcord)
      #     elif foo[1] is 'West':
      #         newcord = foo[0] + (1, 0)
      #         frontier.push(newcord)

      for s in successors: # for each successor of the node state
          if not explored[s[0]] is True:
              frontier.push(s) #if the key of the successor state is not in explored add node of the successor onto the frontier


  return []

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
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