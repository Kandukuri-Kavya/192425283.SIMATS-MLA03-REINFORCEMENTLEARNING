# Road network

roads = {
    "Start": ["A", "B"],
    "A": ["C"],
    "B": ["C"],
    "C": ["Destination"]
}

current_position = "Start"

print("Autonomous Car Navigation")
print("-------------------------")

while current_position != "Destination":

    print("\nCurrent Position:", current_position)

    possible_roads = roads[current_position]

    # Simple policy:
    # Choose the first safe road
    next_position = possible_roads[0]

    print("Following Traffic Rules...")
    print("Moving to:", next_position)

    current_position = next_position

print("\nDestination Reached Safely!")