# Warehouse Robot using MDP

states = ["Start", "Storage", "Delivery"]
actions = ["Move Forward", "Pick Item", "Deliver Item"]

current_state = "Start"

print("Warehouse Robot MDP")

while current_state != "Delivery":

    print("\nCurrent State:", current_state)

    if current_state == "Start":
        action = "Move Forward"
        reward = 5
        current_state = "Storage"

    elif current_state == "Storage":
        action = "Pick Item"
        reward = 10
        current_state = "Delivery"

    print("Action:", action)
    print("Reward:", reward)

print("\nItem Delivered Successfully!")