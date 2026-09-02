# Hierarchical Reinforcement Learning
# Household Robot

tasks = {
    "Clean House": [
        "Go to Room",
        "Find Dirt",
        "Clean Floor"
    ],
    "Serve Water": [
        "Go to Kitchen",
        "Take Glass",
        "Give Water"
    ]
}

print("Household Robot using Hierarchical RL")
print("--------------------------------------")

for main_task in tasks:

    print("\nMain Task:", main_task)

    for subtask in tasks[main_task]:

        print("Performing Subtask:", subtask)

        print("Reward: +5")

print("\nAll Tasks Completed Successfully!")