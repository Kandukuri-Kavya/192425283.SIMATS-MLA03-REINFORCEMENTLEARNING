import random

# Rooms in the smart home
rooms = ["Kitchen", "Hall", "Bedroom", "Charging Station"]

current_room = "Kitchen"
goal = "Charging Station"

print("Smart Home Robot Navigation")

while current_room != goal:

    print("\nRobot is in:", current_room)

    next_room = random.choice(rooms)

    print("Robot moves to:", next_room)

    current_room = next_room

    if current_room == goal:
        print("\nReward: +10")
    else:
        print("Reward: -1")

print("\nRobot reached the Charging Station!")