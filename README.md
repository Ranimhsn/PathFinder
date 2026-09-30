A Python application that visualizes and compares three pathfinding algorithms: **BFS, Dijkstra, and A\***.
## Features
- Interactive grid
- Create obstacles
- Set a starting point and an arrival point
- Visualize explored nodes
- Visualize the final path
- Compare BFS, Dijkstra and A*
- Display the number of explored nodes and path length
- Reset the grid
## Algorithms
### BFS
Breadth-First Search explores the grid level by level and finds a shortest path when all movements have the same cost.
### Dijkstra
Dijkstra's algorithm finds the shortest path by exploring the nodes with the smallest distance from the starting point.
### A*
A* uses both the distance already travelled and a heuristic to guide the search towards the destination.
## Technologies
- Python
- Pygame
## Controls
- **B** → Select BFS
- **D** → Select Dijkstra
- **A** → Select A*
- **E + Left Click** → Set arrival point
- **Left Click** → Create an obstacle
- **Right Click** → Set starting point
- **SPACE** → Run the selected algorithm
- **R** → Reset the grid
## Visualization
- 🟢 Green → Starting point
- 🔴 Red → Arrival point
- ⚫ Dark → Obstacle
- 🔵 Blue → Explored nodes
- 🟡 Yellow → Final path
## Objective
The objective of this project is to understand and visualize how different pathfinding algorithms explore a grid and find a path between two points.