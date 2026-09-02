import random

# Grid positions
states = [0, 1, 2, 3, 4]

# Actions
actions = ["Left", "Right"]

# Q-table
Q = {}

for state in states:
    Q[state] = {"Left": 0, "Right": 0}

alpha = 0.1
gamma = 0.9
epsilon = 0.2

food_position = 4
ghost_position = 2

print("Q-Learning Grid Game")

# Training
for episode in range(20):

    state = 0

    while state != food_position:

        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        # Move agent
        if action == "Right":
            next_state = min(state + 1, 4)
        else:
            next_state = max(state - 1, 0)

        # Reward
        if next_state == ghost_position:
            reward = -10
        elif next_state == food_position:
            reward = 10
        else:
            reward = -1

        # Q-learning update
        Q[state][action] = Q[state][action] + alpha * (
            reward
            + gamma * max(Q[next_state].values())
            - Q[state][action]
        )

        state = next_state

        # Stop if ghost is reached
        if state == ghost_position:
            break

print("\nTraining Completed!")

print("\nQ-Table:")

for state in states:
    print(state, ":", Q[state])

print("\nLearned Policy:")

for state in states[:-1]:

    best_action = max(Q[state], key=Q[state].get)

    print("State", state, "->", best_action)