import random

# Simplified game states
states = ["Start", "Middle", "Win", "Lose"]

# Possible actions
actions = ["Attack", "Defend"]

# Q-table
Q = {}

for state in states:
    Q[state] = {}

    for action in actions:
        Q[state][action] = 0


alpha = 0.1
gamma = 0.9
epsilon = 0.2


print("SARSA for Simplified Tic-Tac-Toe")
print("--------------------------------")


# Training
for episode in range(20):

    state = "Start"

    # Choose initial action
    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        action = max(Q[state], key=Q[state].get)

    while state not in ["Win", "Lose"]:

        # Transition
        if state == "Start":

            next_state = "Middle"
            reward = 0

        else:

            # Random game result
            next_state = random.choice(["Win", "Lose"])

            if next_state == "Win":
                reward = 10
            else:
                reward = -10

        # Choose next action using epsilon-greedy
        if random.random() < epsilon:
            next_action = random.choice(actions)
        else:
            next_action = max(Q[next_state], key=Q[next_state].get)

        # SARSA update
        Q[state][action] = Q[state][action] + alpha * (
            reward
            + gamma * Q[next_state][next_action]
            - Q[state][action]
        )

        state = next_state
        action = next_action


print("\nTraining Completed!")

print("\nLearned Q-Values:")

for state in Q:
    print(state, ":", Q[state])