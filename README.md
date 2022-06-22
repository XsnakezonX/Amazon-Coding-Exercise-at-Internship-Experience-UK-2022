# Amazon-Coding-Exercise-at-Internship-Experience-UK-2022
## Overview: 
Thank you for choosing to take part in Amazon's Coding Challenge for Bright Network. 
We are very happy to have you  here. 
We hope you have as much fun implementing this challenge as we had creating it! In this challenge, you are going to implement Amazon’s pathfinding algorithm for Amazon’s self-driving delivery vehicles.  The self-driving vehicle will need to create a path on a 2D-grid that contains a starting point (x,y), a delivery point (x,y) and a number of obstacles. Your vehicle can navigate to any of the adjacent squares (even diagonally), as long as the  squares are inbound and do not contain an obstacle.

## Read Me

### Running the python script


- Go to the file location via terminal.
- type "python main.py"



### The flow of the A* algorithm
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
