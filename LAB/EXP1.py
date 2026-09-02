# Simplified Chess Game using MDP

states = ["Start", "Middle", "Win"]
actions = ["Attack", "Defend"]

rewards = {
    ("Start", "Attack"): 5,
    ("Start", "Defend"): 2,
    ("Middle", "Attack"): 10,
    ("Middle", "Defend"): 3
}

current_state = "Start"

print("Simplified Chess MDP")

while current_state != "Win":

    print("\nCurrent State:", current_state)

    best_action = max(
        actions,
        key=lambda action: rewards.get((current_state, action), 0)
    )

    print("Best Action:", best_action)

    reward = rewards.get((current_state, best_action), 0)
    print("Reward:", reward)

    if current_state == "Start":
        current_state = "Middle"
    else:
        current_state = "Win"

print("\nGame Won!")