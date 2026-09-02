import random

locations = ["Room A", "Room B", "Room C"]

# Initial belief probabilities
belief = {
    "Room A": 0.33,
    "Room B": 0.34,
    "Room C": 0.33
}

print("Search and Rescue Robot using POMDP")
print("-----------------------------------")

# Robot receives limited sensor information
sensor_observation = random.choice(
    ["Sound Detected", "No Sound"]
)

print("\nSensor Observation:", sensor_observation)

# Update beliefs based on observation
if sensor_observation == "Sound Detected":

    belief["Room B"] += 0.3

else:

    belief["Room B"] -= 0.1

# Normalize beliefs
total = sum(belief.values())

for room in belief:
    belief[room] = belief[room] / total

print("\nUpdated Belief Probabilities:")

for room in belief:
    print(room, ":", round(belief[room], 2))

# Choose room with highest probability
best_location = max(belief, key=belief.get)

print("\nRobot decides to search:", best_location)

print("Rescue Search Completed!")