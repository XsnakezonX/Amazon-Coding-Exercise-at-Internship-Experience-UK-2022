from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
# 'pip install pathfinding' in the terminal for the library above
# Library: https://pypi.org/project/pathfinding/

import numpy as np
import random

matrix1 = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def addObstacles(grid, obstaclePos):
   
   """
   add Obstacles to the grid according to the list of coordinates
   """
   for pos in obstaclePos:
      x,y = pos
      grid[y][x] = 0
   return grid


def random20Obstacles(startPos, endPos):
   """ return a list of 20 random positions for obstacles coordinates"""
   randomCoordinates = []

   while len(randomCoordinates) != 20:
      x = random.randint(0,9)
      y = random.randint(0,9)
      pos = (x,y)
      # generates a random coordinate
      if pos not in randomCoordinates and pos != startPos and pos != endPos:
         # add it to a list if not repeat and not equal to start/end coordinates
         randomCoordinates.append(pos)
      
   return randomCoordinates

### Start ###
if __name__ == '__main__':
   startPos = (0,0)
   endPos = (9, 9)

   opt = input("Enter:\n(1) For default obstacles\n(2) For 20 random obstacles\n>>")

   # the list of default coordinates example
   # obstaclePos = [(7,7),(8,7),(9,7),(7,8)]
   while True:
      if opt == "1":
         obstaclePos = [(7,7),(8,7),(9,7),(7,8)]
         break
      elif opt == "2":
         obstaclePos = random20Obstacles(startPos, endPos)
         break
      elif opt == "0":
         obstaclePos = [(7,7),(8,7),(9,7),(7,8),(7,9)]
         break
      else:
         print('Invalid input! Please enter again!')
         exit(-1)


   matrix10 = addObstacles(matrix1,obstaclePos)

   print(f'Gird with the Obstacles:\n')
   print(np.reshape(matrix10,(-1,10))) # display grid with numpy
   print(f'\n\nCoordinates of the obstacles:\n{obstaclePos}\nNumber of Obstacles:\n{len(obstaclePos)}\n')

   ### settings ###
   x0, y0 = startPos
   x1, y1 = endPos

   grid = Grid(matrix=matrix10)
   start = grid.node(x0, y0)
   end = grid.node(x1, y1)

   ### Run path finding algorithm ###
   finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

   # result extraction
   path, runs = finder.find_path(start, end, grid)

   print(f'\nResults:\nPath coordinates:\n{path} \nSteps:\n{len(path)}\n')
   if len(path) == 0:
      print("No viable path is found!")
   else:
      print('Summary:\noperations:', runs, 'path length:', len(path))
      print(grid.grid_str(path=path, start=start, end=end))

   print("-Process terminated-")

### Read Me ###

# Running the python script

""" 
Go to the file location via terminal.
type "python main.py"

"""

# The flow of the A* algorithm
"""
flow:

  find_path
    init_find  # (re)set global values and open list
    check_neighbors  # for every node in open list
      next_node  # closest node to start in open list
      find_neighbors  # get neighbors
      process_node  # calculate new cost for neighboring node, f(n) = g(n) + h(n)

   Note:
   n is the given state/position
   f(n) is the cost estimation function using g(n) + h(n) 
   g(n) is the step needed to reach current state/position
   h(n) is the heuristic function of calculating the Manhattan distance between the current and goal position

      
"""