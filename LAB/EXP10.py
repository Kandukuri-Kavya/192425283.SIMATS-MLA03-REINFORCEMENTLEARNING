import random

# Drone states
states = ["Start", "Flying", "Low Battery", "Delivered"]

# Actions
actions = ["Fly", "Recharge"]

# Q-table
Q = {}

# Initialize Q-values
for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0

# Rewards
rewards = {
    "Fly": 5,
    "Recharge": -2
}

# Training
episodes = 10
alpha = 0.1
gamma = 0.9

print("Autonomous Drone Delivery System")
print("\nTraining Started...\n")

for episode in range(episodes):

    state = "Start"
    battery = 100

    while state != "Delivered":

        # Choose random action during training
        action = random.choice(actions)

        # Battery decreases when flying
        if action == "Fly":
            battery -= 30

        # Battery increases when recharging
        elif action == "Recharge":
            battery += 20

            if battery > 100:
                battery = 100

        reward = rewards[action]

        # Decide next state
        if battery <= 20:
            next_state = "Low Battery"

        elif state == "Start":
            next_state = "Flying"

        elif state == "Flying" and battery > 20:
            next_state = "Delivered"

        elif state == "Low Battery" and action == "Recharge":
            next_state = "Flying"

        else:
            next_state = "Flying"

        # Find maximum future Q-value
        max_future_q = max(Q[next_state].values())

        # Q-learning update
        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max_future_q - Q[state][action]
        )

        state = next_state

print("Training Completed!")

print("\nQ-Table:")

for state in Q:
    print(state, ":", Q[state])

print("\nTesting the Drone")

state = "Start"

while state != "Delivered":

    best_action = max(Q[state], key=Q[state].get)

    print("Current State:", state)
    print("Best Action:", best_action)

    if state == "Start":
        state = "Flying"

    elif state == "Flying":
        state = "Delivered"

print("\nPackage Delivered Successfully!")