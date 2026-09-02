import random

# Possible locations
locations = ["Room A", "Room B", "Room C"]

# Initial belief probabilities
belief = {
    "Room A": 0.33,
    "Room B": 0.34,
    "Room C": 0.33
}

print("POMDP Robot Navigation")
print("-----------------------")

# Robot receives sensor information
observation = random.choice([
    "Obstacle Detected",
    "Clear Path"
])

print("\nSensor Observation:", observation)

# Update belief
if observation == "Obstacle Detected":

    belief["Room B"] += 0.20
    belief["Room A"] -= 0.10
    belief["Room C"] -= 0.10

else:

    belief["Room C"] += 0.20
    belief["Room A"] -= 0.10
    belief["Room B"] -= 0.10


# Normalize probabilities
total = sum(belief.values())

for room in belief:
    belief[room] = belief[room] / total


print("\nUpdated Belief State:")

for room in belief:
    print(room, ":", round(belief[room], 2))


# Select location with highest belief
best_location = max(
    belief,
    key=belief.get
)

print("\nRobot decides to move towards:", best_location)

print("\nNavigation Decision Completed!")