import random

actions = [
    "Increase Temperature",
    "Maintain Temperature",
    "Decrease Temperature"
]

policy = {
    "Increase Temperature": 0.33,
    "Maintain Temperature": 0.34,
    "Decrease Temperature": 0.33
}

print("Smart Home Temperature Control")
print("------------------------------")

for episode in range(10):

    action = random.choices(
        actions,
        weights=list(policy.values())
    )[0]

    # Simulated reward
    if action == "Maintain Temperature":
        reward = 10
    else:
        reward = -2

    # REINFORCE update
    policy[action] += 0.05 * reward

    if policy[action] < 0.01:
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


print("\nFinal Policy:")

for action in actions:
    print(
        action,
        ":",
        round(policy[action], 2)
    )

best_action = max(policy, key=policy.get)

print("\nBest Temperature Action:", best_action)