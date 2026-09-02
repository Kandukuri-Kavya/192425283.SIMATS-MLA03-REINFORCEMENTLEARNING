import random

actions = ["Increase Energy", "Maintain Energy", "Reduce Energy"]

# Q-values
Q = {
    "Low Demand": [0, 0, 0],
    "Medium Demand": [0, 0, 0],
    "High Demand": [0, 0, 0]
}

states = list(Q.keys())

alpha = 0.1
gamma = 0.9

print("Smart Energy Management System")
print("------------------------------")

for episode in range(10):

    state = random.choice(states)

    action_index = random.randint(0, 2)

    # Reward based on energy decision
    if state == "High Demand" and action_index == 0:
        reward = 10

    elif state == "Low Demand" and action_index == 2:
        reward = 10

    elif action_index == 1:
        reward = 5

    else:
        reward = -5

    # Q-value update
    Q[state][action_index] = Q[state][action_index] + alpha * (
        reward - Q[state][action_index]
    )

    print(
        "State:", state,
        "| Action:", actions[action_index],
        "| Reward:", reward
    )

print("\nLearned Energy Policy:")

for state in states:

    best_action = Q[state].index(max(Q[state]))

    print(
        state,
        "->",
        actions[best_action]
    )