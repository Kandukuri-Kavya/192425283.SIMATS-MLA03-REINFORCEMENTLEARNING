import random
import math

# True click probabilities for advertisements
click_probabilities = [0.3, 0.5, 0.7]

ads = ["Ad A", "Ad B", "Ad C"]

rounds = 100


# --------------------------------
# Epsilon-Greedy
# --------------------------------

def epsilon_greedy():

    counts = [0, 0, 0]
    rewards = [0, 0, 0]

    epsilon = 0.1

    for _ in range(rounds):

        if random.random() < epsilon:
            ad = random.randint(0, 2)
        else:

            averages = [
                rewards[i] / counts[i]
                if counts[i] > 0 else 0
                for i in range(3)
            ]

            ad = averages.index(max(averages))

        reward = 1 if random.random() < click_probabilities[ad] else 0

        counts[ad] += 1
        rewards[ad] += reward

    return sum(rewards)


# --------------------------------
# UCB
# --------------------------------

def ucb():

    counts = [0, 0, 0]
    rewards = [0, 0, 0]

    for i in range(3):

        reward = 1 if random.random() < click_probabilities[i] else 0

        counts[i] += 1
        rewards[i] += reward

    for t in range(3, rounds):

        ucb_values = []

        for i in range(3):

            average = rewards[i] / counts[i]

            confidence = math.sqrt(
                2 * math.log(t + 1) / counts[i]
            )

            ucb_values.append(average + confidence)

        ad = ucb_values.index(max(ucb_values))

        reward = 1 if random.random() < click_probabilities[ad] else 0

        counts[ad] += 1
        rewards[ad] += reward

    return sum(rewards)


# --------------------------------
# Thompson Sampling
# --------------------------------

def thompson_sampling():

    successes = [1, 1, 1]
    failures = [1, 1, 1]

    total_reward = 0

    for _ in range(rounds):

        samples = [
            random.betavariate(
                successes[i],
                failures[i]
            )
            for i in range(3)
        ]

        ad = samples.index(max(samples))

        reward = 1 if random.random() < click_probabilities[ad] else 0

        total_reward += reward

        if reward == 1:
            successes[ad] += 1
        else:
            failures[ad] += 1

    return total_reward


# Run algorithms

epsilon_result = epsilon_greedy()
ucb_result = ucb()
thompson_result = thompson_sampling()

print("Advertisement Bandit Comparison")
print("--------------------------------")

print("Epsilon-Greedy Clicks:", epsilon_result)
print("UCB Clicks:", ucb_result)
print("Thompson Sampling Clicks:", thompson_result)

results = {
    "Epsilon-Greedy": epsilon_result,
    "UCB": ucb_result,
    "Thompson Sampling": thompson_result
}

best_algorithm = max(results, key=results.get)

print("\nBest Algorithm:", best_algorithm)