import random

actions = ["Forward", "Left", "Right", "Park"]

# Policy values
policy = {
    "Forward": 0.25,
    "Left": 0.25,
    "Right": 0.25,
    "Park": 0.25
}

episodes = 10

print("Autonomous Parking using REINFORCE")
print("----------------------------------")

for episode in range(episodes):

    action = random.choices(
        actions,
        weights=policy.values()
    )[0]

    # Reward
    if action == "Park":
        reward = 10
    else:
        reward = -1

    # REINFORCE policy update
    policy[action] += 0.1 * reward

    # Prevent negative values
    if policy[action] < 0:
        policy[action] = 0.01

    # Normalize probabilities
    total = sum(policy.values())

    for a in actions:
        policy[a] /= total

    print(
        "Episode:", episode + 1,
        "| Action:", action,
        "| Reward:", reward
    )

print("\nLearned Policy:")

for action in actions:
    print(action, ":", round(policy[action], 2))

best_action = max(policy, key=policy.get)

print("\nBest Parking Action:", best_action)