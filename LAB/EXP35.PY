# Historical returns of different portfolios

portfolios = {
    "Portfolio A": [5, 7, 6, 8, 9],
    "Portfolio B": [4, 5, 6, 5, 7],
    "Portfolio C": [6, 8, 7, 9, 10]
}

predicted_values = {}

print("Investment Portfolio Prediction")
print("-------------------------------")

for portfolio in portfolios:

    returns = portfolios[portfolio]

    # Simple value prediction using average return
    predicted_value = sum(returns) / len(returns)

    predicted_values[portfolio] = predicted_value

    print(
        portfolio,
        "Predicted Return:",
        round(predicted_value, 2)
    )


best_portfolio = max(
    predicted_values,
    key=predicted_values.get
)

print(
    "\nBest Predicted Portfolio:",
    best_portfolio
)

print(
    "Expected Return:",
    round(predicted_values[best_portfolio], 2)
)