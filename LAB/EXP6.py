import random

# Grid size
grid_size = 5

# Starting and goal positions
robot = [0, 0]
goal = [4, 4]

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

print("Autonomous Robot Navigation")

steps = 0

while robot != goal and steps < 50:

    action = random.choice(actions)

    if action == "UP" and robot[0] > 0:
        robot[0] -= 1

    elif action == "DOWN" and robot[0] < grid_size - 1:
        robot[0] += 1

    elif action == "LEFT" and robot[1] > 0:
        robot[1] -= 1

    elif action == "RIGHT" and robot[1] < grid_size - 1:
        robot[1] += 1

    print("Action:", action, "| Position:", robot)

    steps += 1

if robot == goal:
    print("\nGoal Reached!")
    print("Total Steps:", steps)
else:
    print("\nGoal not reached within 50 steps.")