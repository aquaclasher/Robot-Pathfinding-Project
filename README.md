# Robot Pathfinding to Goal

## Overview
This project simulates a robot navigating through a maze to reach the goal, represented by the number `2`. The robot explores the grid using a breadth-first search algorithm, marking its path as it travels. The simulation uses Python's `turtle` graphics for visualization.

## Features
- **Grid Representation**: The grid is represented using a 2D list where:
  - `0` represents obstacles (black cells).
  - `1` represents open paths (white cells).
  - `2` represents the black box (red cell).

- **Pathfinding Algorithm**: The robot employs a breadth-first search (BFS) algorithm to find the shortest path to the black box.

- **Visualization**:
  - The grid is visually represented using turtle graphics.
  - The robot's exploration path is shown in blue.
  - The final path to the black box is displayed in green.
  - The black box remains visible during and after the robot's movement.

## Known Issues
  - The robot explores the grid very inefficently.
  - In the turtle representation, the back tracking of the robot is not clearly visible so it looks like its teleporting to other cells.

## How to run
  - Works in Pycharm after just copy pasting the code.
