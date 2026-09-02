import random

# Advertisement rewards
ads = ["Ad A", "Ad B", "Ad C"]

estimated_rewards = [0, 0, 0]
number_of_clicks = [0, 0, 0]

epsilon = 0.2
rounds = 10

print("Epsilon-Greedy Advertisement System")

for i in range(rounds):

    # Exploration
    if random.random() < epsilon:
        selected_ad = random.randint(0, 2)
        print("\nExploration")

    # Exploitation
    else:
        selected_ad = estimated_rewards.index(max(estimated_rewards))
        print("\nExploitation")

    # Simulated user click
    reward = random.randint(0, 1)

    number_of_clicks[selected_ad] += 1

    # Update estimated reward
    estimated_rewards[selected_ad] += (
        reward - estimated_rewards[selected_ad]
    ) / number_of_clicks[selected_ad]

    print("Selected:", ads[selected_ad])
    print("Reward:", reward)

print("\nFinal Estimated Rewards:")

for i in range(3):
    print(ads[i], ":", round(estimated_rewards[i], 2))