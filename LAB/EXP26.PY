import random
import math

# Different product prices
prices = [100, 150, 200]

# Probability that a customer purchases at each price
purchase_probability = [0.8, 0.6, 0.4]

rounds = 100


# Epsilon-Greedy Algorithm
def epsilon_greedy():

    counts = [0, 0, 0]
    revenue = [0, 0, 0]

    epsilon = 0.1

    for _ in range(rounds):

        # Exploration
        if random.random() < epsilon:
            action = random.randint(0, 2)

        # Exploitation
        else:
            average = [
                revenue[i] / counts[i]
                if counts[i] > 0 else 0
                for i in range(3)
            ]

            action = average.index(max(average))

        # Simulate customer purchase
        purchase = random.random() < purchase_probability[action]

        if purchase:
            reward = prices[action]
        else:
            reward = 0

        counts[action] += 1
        revenue[action] += reward

    return sum(revenue)


# UCB Algorithm
def ucb():

    counts = [0, 0, 0]
    revenue = [0, 0, 0]

    # Try every price once
    for i in range(3):

        purchase = random.random() < purchase_probability[i]

        reward = prices[i] if purchase else 0

        counts[i] += 1
        revenue[i] += reward

    for t in range(3, rounds):

        ucb_values = []

        for i in range(3):

            average = revenue[i] / counts[i]

            confidence = math.sqrt(
                2 * math.log(t + 1) / counts[i]
            )

            ucb_values.append(average + confidence)

        action = ucb_values.index(max(ucb_values))

        purchase = random.random() < purchase_probability[action]

        reward = prices[action] if purchase else 0

        counts[action] += 1
        revenue[action] += reward

    return sum(revenue)


# Thompson Sampling
def thompson_sampling():

    successes = [1, 1, 1]
    failures = [1, 1, 1]

    total_revenue = 0

    for _ in range(rounds):

        samples = []

        for i in range(3):

            sample = random.betavariate(
                successes[i],
                failures[i]
            )

            # Expected revenue
            samples.append(sample * prices[i])

        action = samples.index(max(samples))

        purchase = (
            random.random()
            < purchase_probability[action]
        )

        if purchase:

            reward = prices[action]
            successes[action] += 1

        else:

            reward = 0
            failures[action] += 1

        total_revenue += reward

    return total_revenue


# Run algorithms

epsilon_revenue = epsilon_greedy()
ucb_revenue = ucb()
thompson_revenue = thompson_sampling()


print("Dynamic Pricing using Multi-Armed Bandits")
print("----------------------------------------")

print("Epsilon-Greedy Revenue:", epsilon_revenue)
print("UCB Revenue:", ucb_revenue)
print("Thompson Sampling Revenue:", thompson_revenue)


results = {
    "Epsilon-Greedy": epsilon_revenue,
    "UCB": ucb_revenue,
    "Thompson Sampling": thompson_revenue
}

best_algorithm = max(results, key=results.get)

print("\nBest Pricing Algorithm:", best_algorithm)