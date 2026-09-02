import random

# States
states = ["Clear Road", "Slow Vehicle", "Obstacle"]

# Actions
actions = ["Accelerate", "Brake", "Change Lane"]

# Q-table
Q = {}

for state in states:

    Q[state] = {}

    for action in actions:
        Q[state][action] = 0


# Rewards

rewards = {
    "Clear Road": {
        "Accelerate": 10,
        "Brake": 2,
        "Change Lane": 5
    },

    "Slow Vehicle": {
        "Accelerate": -5,
        "Brake": 5,
        "Change Lane": 10
    },

    "Obstacle": {
        "Accelerate": -10,
        "Brake": 10,
        "Change Lane": 8
    }
}


print("Autonomous Highway Driving")

# Training

for episode in range(20):

    state = random.choice(states)

    action = random.choice(actions)

    reward = rewards[state][action]

    # Simple Q-value update
    Q[state][action] = (
        Q[state][action]
        + 0.1 * (
            reward - Q[state][action]
        )
    )


print("\nLearned Driving Policy:")

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