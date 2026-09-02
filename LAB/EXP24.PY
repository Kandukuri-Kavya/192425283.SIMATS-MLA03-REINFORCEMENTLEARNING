import random

actions = ["Buy", "Sell", "Hold"]

policy = {
    "Buy": 0.33,
    "Sell": 0.33,
    "Hold": 0.34
}

balance = 1000

print("Automated Trading using REINFORCE")
print("---------------------------------")

for episode in range(10):

    action = random.choices(
        actions,
        weights=policy.values()
    )[0]

    # Simulated market profit/loss
    profit = random.randint(-50, 100)

    balance += profit

    # Policy update
    policy[action] += 0.01 * profit

    if policy[action] < 0.01:
        policy[action] = 0.01

    # Normalize
    total = sum(policy.values())

    for a in actions:
        policy[a] /= total

    print(
        "Action:", action,
        "| Profit:", profit,
        "| Balance:", balance
    )

print("\nFinal Balance:", balance)

best_action = max(policy, key=policy.get)

print("Best Learned Action:", best_action)