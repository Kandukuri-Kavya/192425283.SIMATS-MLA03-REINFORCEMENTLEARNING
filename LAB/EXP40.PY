import random

# Student performance states
states = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

# Learning actions
actions = [
    "Easy Lesson",
    "Medium Lesson",
    "Advanced Lesson"
]

# Q-table
Q = {}

for state in states:

    Q[state] = {}

    for action in actions:
        Q[state][action] = 0


print("Personalized Education using RL")
print("-------------------------------")

# Training
for episode in range(20):

    state = random.choice(states)

    action = random.choice(actions)

    # Reward system
    if state == "Beginner" and action == "Easy Lesson":
        reward = 10

    elif state == "Intermediate" and action == "Medium Lesson":
        reward = 10

    elif state == "Advanced" and action == "Advanced Lesson":
        reward = 10

    else:
        reward = -5


    # Update Q-value
    Q[state][action] += 0.1 * (
        reward - Q[state][action]
    )

    print(
        "Student Level:", state,
        "| Selected Content:", action,
        "| Reward:", reward
    )


print("\nLearned Personalized Learning Policy:")

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