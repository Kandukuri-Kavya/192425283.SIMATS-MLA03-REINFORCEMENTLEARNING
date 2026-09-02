# Traffic conditions
states = ["Low Traffic", "Medium Traffic", "High Traffic"]

# Possible traffic signal actions
actions = ["Short Green", "Medium Green", "Long Green"]

# Rewards
rewards = {
    "Low Traffic": {
        "Short Green": 10,
        "Medium Green": 5,
        "Long Green": 2
    },

    "Medium Traffic": {
        "Short Green": 3,
        "Medium Green": 10,
        "Long Green": 5
    },

    "High Traffic": {
        "Short Green": 1,
        "Medium Green": 5,
        "Long Green": 10
    }
}


print("Traffic Light Optimization")
print("--------------------------")

policy = {}

# Policy improvement
for state in states:

    best_action = max(
        actions,
        key=lambda action: rewards[state][action]
    )

    policy[state] = best_action


print("\nOptimal Traffic Light Policy:")

for state in states:

    print(
        state,
        "->",
        policy[state]
    )