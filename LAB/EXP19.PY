import random

robots = ["Robot 1", "Robot 2", "Robot 3"]

tasks = [
    "Pick Item",
    "Move Item",
    "Deliver Item"
]

print("Multi-Agent Warehouse System")
print("----------------------------")

total_reward = 0

for robot in robots:

    task = random.choice(tasks)

    reward = random.randint(5, 10)

    total_reward += reward

    print(
        robot,
        "is performing:",
        task,
        "| Reward:",
        reward
    )

print("\nTotal Team Reward:", total_reward)

print("\nAll Robots Cooperated Successfully!")