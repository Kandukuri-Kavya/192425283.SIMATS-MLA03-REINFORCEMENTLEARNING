import random

actions = ["Move Left", "Move Right", "Pick", "Place"]

# Initial policy probabilities
policy = {
    "Move Left": 0.25,
    "Move Right": 0.25,
    "Pick": 0.25,
    "Place": 0.25
}

print("Industrial Robotic Arm")
print("----------------------")

for episode in range(10):

    # Select action based on policy
    action = random.choices(
        actions,
        weights=policy.values()
    )[0]

    # Reward for successful actions
    if action == "Pick" or action == "Place":
        reward = 10
    else:
        reward = -1

    # Simple policy update
    policy[action] += 0.05 * reward

    # Keep probabilities positive
    if policy[action] < 0:
        policy[action] = 0.01

    # Normalize policy
    total = sum(policy.values())

    for a in actions:
        policy[a] = policy[a] / total

    print(
        "Episode:", episode + 1,
        "| Action:", action,
        "| Reward:", reward
    )

print("\nFinal Policy:")

for action in policy:
    print(action, ":", round(policy[action], 2))

best_action = max(policy, key=policy.get)

print("\nBest Action Learned:", best_action)