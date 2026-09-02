import random

floors = [1, 2, 3, 4, 5]

# Actor chooses an action
actions = ["Up", "Down", "Stop"]

# Critic stores values
state_values = {}

for floor in floors:
    state_values[floor] = 0

print("Smart Elevator using Actor-Critic")
print("---------------------------------")

for episode in range(10):

    current_floor = random.choice(floors)

    # Actor selects action
    action = random.choice(actions)

    # Simulated passenger waiting time
    waiting_time = random.randint(1, 10)

    # Reward: less waiting time gives better reward
    reward = 10 - waiting_time

    # Critic updates state value
    state_values[current_floor] = (
        state_values[current_floor]
        + 0.1 * reward
    )

    print(
        "Floor:", current_floor,
        "| Action:", action,
        "| Waiting Time:", waiting_time,
        "| Reward:", reward
    )

print("\nState Values:")

for floor in floors:
    print(
        "Floor",
        floor,
        ":",
        round(state_values[floor], 2)
    )