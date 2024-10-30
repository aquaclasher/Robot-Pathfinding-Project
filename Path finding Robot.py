import turtle
from collections import deque

# Function to find the path to the goal
def find_goal_path(grid, start_pos):
    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]  # Right, Up, Down, Left
    queue = deque([start_pos])  # Use deque for efficient popping from the front
    visited = set()  # Set to track visited positions
    visited.add(tuple(start_pos))  # Convert to tuple for hashing
    parent = {tuple(start_pos): None}  # To reconstruct the path
    all_visited = []  # To keep track of all visited positions

    goal_position = (7, 9)  # Goal position
    grid[goal_position[0]][goal_position[1]] = 2

    while queue:
        current_pos = queue.popleft()  # Get the front position
        all_visited.append(current_pos)  # Record all visited positions

        # Check if the current position has reached the goal
        if current_pos == goal_position:
            print("Goal detected at:", current_pos)
            break  # Exit once the goal is found

        # Explore all possible directions
        for direction in directions:
            new_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]

            # Check if the new position is valid and not visited
            if (0 <= new_pos[0] < len(grid) and
                    0 <= new_pos[1] < len(grid[0]) and
                    grid[new_pos[0]][new_pos[1]] != 0 and  # Can move to 1
                    tuple(new_pos) not in visited):
                visited.add(tuple(new_pos))  # Mark as visited
                parent[tuple(new_pos)] = tuple(current_pos)  # Keep track of the path as tuples
                queue.append(new_pos)  # Add to the queue for exploration

    # Reconstruct the path to the goal
    path_to_goal = []
    path_pos = tuple(current_pos)  # Ensure it's a tuple for the lookup
    while path_pos is not None:
        path_to_goal.append(path_pos)
        path_pos = parent[path_pos]

    path_to_goal.reverse()  # Reverse the path to get it from start to end
    return path_to_goal, all_visited

# Draw the grid for visualization
def preload_grid(grid):
    turtle.speed(0)  # Fastest drawing
    turtle.penup()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Set the fill color based on the grid value
            if grid[row][col] == 1:
                turtle.fillcolor("white")
            elif grid[row][col] == 0:
                turtle.fillcolor("black")
            elif grid[row][col] == 2:
                turtle.fillcolor("red")

            # Draw the cell
            turtle.goto(-200 + (col * 40), 200 - (row * 40))
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(40)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

def draw_goal():
    """Draw the goal position to ensure its visibility."""
    goal_position = (7, 9)  # Goal position
    turtle.goto(-200 + (goal_position[1] * 40), 200 - (goal_position[0] * 40))
    turtle.pendown()
    turtle.fillcolor("red")  # Goal color
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def draw_robot(x, y, color):
    """Draw the robot at the specified position with the given color."""
    turtle.penup()
    turtle.goto(x, y - 20)  # Center the robot
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(20)  # Draw a circle for the robot
    turtle.end_fill()

def move_robot(path, color):
    """Move the robot along the specified path with the given color."""
    for step in path:
        next_x = -200 + (step[1] * 40) + 20  # Center in the cell
        next_y = 200 - (step[0] * 40) - 20  # Center in the cell
        draw_robot(next_x, next_y, color)

def overdraw_dry_run(path):
    """Overdraw the dry run path to clean the grid"""
    for step in path:
        next_x = -200 + (step[1] * 40)  # Top-left corner of the cell
        next_y = 200 - (step[0] * 40)  # Top-left corner of the cell
        turtle.penup()
        turtle.goto(next_x, next_y)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(40)
            turtle.right(90)
        turtle.end_fill()

# Complex grid example
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start_position = [1, 2]  # Starting position

# Find the path to the goal
path_to_goal, all_visited = find_goal_path(grid, start_position)
print("Path to goal:", path_to_goal)

# Set up the turtle graphics
turtle.title("Robot Path to Goal")
turtle.setup(width=800, height=600)
preload_grid(grid)

# Move robot for dry run (showing all visited positions)
if all_visited:
    move_robot(all_visited, "blue")  # Draw the dry run in blue
    overdraw_dry_run(all_visited)  # Overdraw dry run path in white

# Draw the goal to ensure it remains visible
draw_goal()

# Move robot for wet run (showing the fastest path)
if path_to_goal:
    move_robot(path_to_goal, "green")  # Draw the wet run in green

# Finish the turtle graphics
turtle.done()
