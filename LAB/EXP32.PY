# Simplified Dueling DQN

states = ["Start", "Path", "Goal"]

actions = ["Left", "Right", "Forward"]

# State value function
V = {
    "Start": 2,
    "Path": 5,
    "Goal": 10
}

# Advantage function
A = {
    "Left": -2,
    "Right": 1,
    "Forward": 3
}

print("Dueling DQN Gridworld")
print("----------------------")

for state in states:

    print("\nState:", state)

    q_values = {}

    for action in actions:

        # Dueling DQN:
        # Q(s,a) = V(s) + A(s,a)

        q_values[action] = V[state] + A[action]

        print(
            action,
            "Q-Value:",
            q_values[action]
        )

    best_action = max(
        q_values,
        key=q_values.get
    )

    print("Best Action:", best_action)