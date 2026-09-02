# Experiment 36
# Simplified MAXQ Framework

agents = ["Agent 1", "Agent 2"]

# Main task and subtasks
tasks = {
    "Complete Task": [
        "Collect Materials",
        "Process Materials",
        "Deliver Result"
    ]
}

# Rewards for subtasks
rewards = {
    "Collect Materials": 5,
    "Process Materials": 10,
    "Deliver Result": 15
}

total_reward = 0

print("MAXQ Multi-Agent System")
print("------------------------")

for main_task in tasks:

    print("\nMain Task:", main_task)

    for i, subtask in enumerate(tasks[main_task]):

        # Assign agents alternately
        agent = agents[i % len(agents)]

        reward = rewards[subtask]

        total_reward += reward

        print(
            agent,
            "performs:",
            subtask,
            "| Reward:",
            reward
        )

print("\nTotal Reward:", total_reward)
print("Overall Task Completed Successfully!")