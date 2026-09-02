import random

# Traffic conditions
traffic = ["Low", "Medium", "High"]

# Simulated waiting times for different algorithms
algorithms = ["DQN", "Double DQN", "Dueling DQN", "PER"]

results = {}

print("Smart Traffic Signal Control")
print("--------------------------")

for algorithm in algorithms:

    total_waiting_time = 0

    for episode in range(10):

        condition = random.choice(traffic)

        if condition == "Low":
            waiting_time = random.randint(1, 5)

        elif condition == "Medium":
            waiting_time = random.randint(5, 10)

        else:
            waiting_time = random.randint(10, 20)

        # Simulated improvement
        if algorithm == "Double DQN":
            waiting_time -= 1

        elif algorithm == "Dueling DQN":
            waiting_time -= 2

        elif algorithm == "PER":
            waiting_time -= 3

        if waiting_time < 0:
            waiting_time = 0

        total_waiting_time += waiting_time

    average_waiting_time = total_waiting_time / 10

    results[algorithm] = average_waiting_time

    print(
        algorithm,
        "Average Waiting Time:",
        round(average_waiting_time, 2)
    )

best_algorithm = min(results, key=results.get)

print("\nBest Algorithm:", best_algorithm)
print("Minimum Waiting Time:", round(results[best_algorithm], 2))