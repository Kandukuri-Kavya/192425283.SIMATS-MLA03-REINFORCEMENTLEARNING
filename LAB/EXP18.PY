import random

tasks = [
    "Assemble Part",
    "Weld Component",
    "Move Object"
]

# Store learned experience
experience = {}

print("Meta Reinforcement Learning")
print("---------------------------")

for task in tasks:

    print("\nNew Task:", task)

    # Simulated learning
    reward = random.randint(1, 10)

    experience[task] = reward

    print("Learning Reward:", reward)

print("\nPreviously Learned Knowledge:")

for task in experience:
    print(task, ":", experience[task])

best_task = max(experience, key=experience.get)

print("\nBest Learned Task:", best_task)