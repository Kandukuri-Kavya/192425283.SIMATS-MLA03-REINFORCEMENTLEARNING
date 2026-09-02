import random

# Simple warehouse states
states = ["Start", "Path", "Goal"]

# Initialize value function for TD(0)
V = {
    "Start": 0,
    "Path": 0,
    "Goal": 0
}

alpha = 0.1
gamma = 0.9

print("TD(0) Learning")

for episode in range(10):

    state = "Start"

    while state != "Goal":

        if state == "Start":
            next_state = "Path"
            reward = -1

        else:
            next_state = "Goal"
            reward = 10

        # TD(0) Update
        V[state] = V[state] + alpha * (
            reward + gamma * V[next_state] - V[state]
        )

        state = next_state

print("\nTD(0) State Values:")
for state in states:
    print(state, ":", round(V[state], 2))


# Simple Q-Learning example
actions = ["Move"]

Q = {
    "Start": 0,
    "Path": 0
}

print("\nQ-Learning")

for episode in range(10):

    state = "Start"

    while state != "Goal":

        if state == "Start":
            next_state = "Path"
            reward = -1
        else:
            next_state = "Goal"
            reward = 10

        Q[state] = Q[state] + alpha * (
            reward + gamma * Q.get(next_state, 0) - Q[state]
        )

        state = next_state

print("\nQ Values:")
for state in Q:
    print(state, ":", round(Q[state], 2))

print("\nSARSA follows a similar on-policy update process.")