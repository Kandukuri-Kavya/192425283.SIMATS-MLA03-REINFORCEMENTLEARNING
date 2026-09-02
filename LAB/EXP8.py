import random

# Rooms
rooms = ["A", "B", "C"]

# Value of each room
values = {
    "A": 0.0,
    "B": 0.0,
    "C": 0.0
}

returns = {
    "A": [],
    "B": [],
    "C": []
}

episodes = 10

print("Monte Carlo Robot Vacuum Cleaner")

for episode in range(episodes):

    room = random.choice(rooms)

    # Reward for cleaning
    reward = random.randint(1, 10)

    # Energy consumption
    energy_cost = random.randint(1, 3)

    total_reward = reward - energy_cost

    returns[room].append(total_reward)

    # Monte Carlo value update
    values[room] = sum(returns[room]) / len(returns[room])

    print(
        "Episode:", episode + 1,
        "| Room:", room,
        "| Reward:", reward,
        "| Energy:", energy_cost,
        "| Total:", total_reward
    )

print("\nEstimated Room Values:")

for room in rooms:
    print(room, ":", round(values[room], 2))

best_room = max(values, key=values.get)

print("\nBest Room to Clean:", best_room)