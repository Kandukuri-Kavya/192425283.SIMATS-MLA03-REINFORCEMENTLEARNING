import random

actions = ["Move Left", "Stay", "Move Right"]

# Policy values
policy = {
    "Move Left": 0.33,
    "Stay": 0.34,
    "Move Right": 0.33
}

print("Autonomous Lane Keeping System")
print("-------------------------------")

for episode in range(10):

    # Choose action according to policy
    action = random.choices(
        actions,
        weights=list(policy.values())
    )[0]

    # Simulated reward
    if action == "Stay":
        reward = 10
    else:
        reward = -2

    # Update policy
    policy[action] += 0.05 * reward

    # Keep values positive
    if policy[action] < 0.01:
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

for action in actions:
    print(action, ":", round(policy[action], 2))

best_action = max(policy, key=policy.get)

print("\nBest Lane Keeping Action:", best_action)