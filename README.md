# Labyrinth Generator and Visualizer

## Description
This project is a Python-based labyrinth generator and visualizer. It uses graph theory to represent a grid-like maze, allowing for random generation of walls and paths. The labyrinth is displayed using Turtle Graphics, and the solution path from the start to the goal is highlighted.

## Features
- **Graph Representation**: 
  - Cells are represented as nodes.
  - Walls are represented as edges, with states (open or closed).
- **Random Labyrinth Generation**: 
  - Generates a solvable labyrinth by connecting neighboring cells with random open/closed walls.
- **Pathfinding**: 
  - Implements Breadth-First Search (BFS) and Depth-First Search (DFS) to find paths.
  - Ensures the maze has a valid solution from a start to a goal.
- **Visualization**: 
  - Displays the labyrinth and solution path using the Turtle Graphics library.

## Requirements
- Python 3.x
- Turtle Graphics (default in Python)

## How to Run
1. Ensure you have Python 3.x installed.
2. Save the project code to a `.py` file (e.g., `labyrinth.py`).
3. Run the file in a Python environment.
4. A Turtle Graphics window will display the generated labyrinth and solution.

## Customization
- You can modify the `l` (rows) and `c` (columns) variables in the script to change the labyrinth size.
- Adjust the randomization logic to create different types of mazes.

## Example Usage
- Generate a 10x10 labyrinth and visualize the solution path.

## File Structure
- **`graphe.py`**: Contains the graph implementation for the labyrinth.
- **Turtle Visualization**: Uses Turtle Graphics to draw and fill the maze based on the graph.

## Contribution
Feel free to submit issues or pull requests to enhance the functionality or visualization of this project.

## License
This project is open-source and free to use under the MIT License.
