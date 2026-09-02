import random

actions = ["Stay", "Change Left", "Change Right"]

# Policy probabilities
policy = {
    "Stay": 0.33,
    "Change Left": 0.34,
    "Change Right": 0.33
}

print("Autonomous Highway Lane Changing")
print("--------------------------------")

for episode in range(10):

    slow_vehicle_ahead = random.choice([True, False])

    action = random.choices(
        actions,
        weights=policy.values()
    )[0]

    # Reward
    if slow_vehicle_ahead:

        if action != "Stay":
            reward = 10
        else:
            reward = -5

    else:

        if action == "Stay":
            reward = 10
        else:
            reward = -2

    # Simplified PPO policy update
    policy[action] += 0.05 * reward

    if policy[action] < 0.01:
        policy[action] = 0.01

    # Normalize probabilities
    total = sum(policy.values())

    for a in actions:
        policy[a] /= total

    print(
        "Slow Vehicle:",
        slow_vehicle_ahead,
        "| Action:",
        action,
        "| Reward:",
        reward
    )

print("\nFinal Policy:")

for action in actions:
    print(action, ":", round(policy[action], 2))