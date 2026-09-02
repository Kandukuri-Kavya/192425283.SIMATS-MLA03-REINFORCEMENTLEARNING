import random

# Healthcare states
states = [
    "Low Patient Load",
    "Medium Patient Load",
    "High Patient Load"
]

# Possible actions
actions = [
    "Assign More Staff",
    "Maintain Resources",
    "Reduce Resources"
]

# Q-table
Q = {}

for state in states:

    Q[state] = {}

    for action in actions:
        Q[state][action] = 0


print("Healthcare Management using RL")
print("------------------------------")

# Training
for episode in range(20):

    state = random.choice(states)

    action = random.choice(actions)

    # Reward system
    if state == "High Patient Load" and action == "Assign More Staff":
        reward = 10

    elif state == "Low Patient Load" and action == "Reduce Resources":
        reward = 8

    elif action == "Maintain Resources":
        reward = 5

    else:
        reward = -5


    # Q-value update
    Q[state][action] += 0.1 * (
        reward - Q[state][action]
    )

    print(
        "State:", state,
        "| Action:", action,
        "| Reward:", reward
    )


print("\nOptimal Healthcare Policy:")

for state in states:

    best_action = max(
        Q[state],
        key=Q[state].get
    )

    print(
        state,
        "->",
        best_action
    )