# Simple robot navigation graph

transitions = {
    "Start": {
        "Path A": ("A", -2),
        "Path B": ("B", -4)
    },

    "A": {
        "Goal": ("Goal", 10)
    },

    "B": {
        "Goal": ("Goal", 10)
    }
}


# Goal state value
V = {
    "Goal": 0
}


# Bellman equation calculation

# Value of A
V["A"] = 10 + V["Goal"]

# Value of B
V["B"] = 10 + V["Goal"]

# Calculate values for Start actions

value_A = -2 + V["A"]

value_B = -4 + V["B"]

V["Start"] = max(value_A, value_B)


print("Bellman's Optimality Equation")
print("-----------------------------")

print("Value of Path A:", value_A)
print("Value of Path B:", value_B)

print("\nOptimal State Value:", V["Start"])

if value_A > value_B:
    print("Optimal Path: Start -> A -> Goal")
else:
    print("Optimal Path: Start -> B -> Goal")