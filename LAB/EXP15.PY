import random

algorithms = ["PPO", "TRPO"]

results = {}

print("Humanoid Robot Walking")
print("-----------------------")

for algorithm in algorithms:

    total_balance = 0

    for episode in range(10):

        # Simulated walking stability
        balance = random.randint(50, 100)

        # Simulated algorithm improvement
        if algorithm == "PPO":
            balance += 5

        else:
            balance += 3

        if balance > 100:
            balance = 100

        total_balance += balance

    average_balance = total_balance / 10

    results[algorithm] = average_balance

    print(
        algorithm,
        "Average Balance:",
        round(average_balance, 2)
    )

best_algorithm = max(results, key=results.get)

print("\nBest Algorithm:", best_algorithm)
print(
    "Highest Stability:",
    round(results[best_algorithm], 2)
)
