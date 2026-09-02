# Dynamic Programming for Autonomous Taxi Routing

roads = {
    "Start": {"A": 4, "B": 2},
    "A": {"Destination": 3},
    "B": {"Destination": 6}
}

# Cost from each state to destination
value = {
    "Destination": 0
}

# Calculate optimal cost using Bellman principle
value["A"] = roads["A"]["Destination"] + value["Destination"]
value["B"] = roads["B"]["Destination"] + value["Destination"]

cost_A = roads["Start"]["A"] + value["A"]
cost_B = roads["Start"]["B"] + value["B"]

value["Start"] = min(cost_A, cost_B)

print("Autonomous Taxi Routing using Dynamic Programming")
print("\nCost through A:", cost_A)
print("Cost through B:", cost_B)

if cost_A < cost_B:
    print("\nOptimal Route: Start -> A -> Destination")
else:
    print("\nOptimal Route: Start -> B -> Destination")

print("Minimum Cost:", value["Start"])