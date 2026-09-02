import random

# Game actions
actions = [
    "Gather Resources",
    "Build Unit",
    "Attack Opponent"
]

# Actor values represent action preferences
actor = {
    "Gather Resources": 0,
    "Build Unit": 0,
    "Attack Opponent": 0
}

print("DDPG Strategy Game")
print("------------------")

for episode in range(10):

    # Actor chooses an action
    action = random.choice(actions)

    # Critic evaluates action
    if action == "Gather Resources":
        reward = 5

    elif action == "Build Unit":
        reward = 7

    else:
        reward = 10

    # Simplified actor update
    actor[action] += 0.1 * reward

    print(
        "Episode:", episode + 1,
        "| Action:", action,
        "| Reward:", reward
    )


print("\nLearned Actor Values:")

for action in actor:
    print(
        action,
        ":",
        round(actor[action], 2)
    )

best_action = max(actor, key=actor.get)

print("\nBest Strategy:", best_action)