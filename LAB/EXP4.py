# Bellman Equation for Delivery Robot

states = ["Home", "Road A", "Road B", "Destination"]

cost = {
    "Road A": 5,
    "Road B": 8
}

print("Autonomous Delivery Robot")

print("\nPossible Paths:")
print("Road A Cost:", cost["Road A"])
print("Road B Cost:", cost["Road B"])

# Bellman principle: choose minimum cost
best_road = min(cost, key=cost.get)

print("\nOptimal Path:", best_road)
print("Minimum Travel Cost:", cost[best_road])

print("\nRobot reached the Destination!")