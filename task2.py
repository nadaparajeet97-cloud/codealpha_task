# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

# Number of stocks to enter
n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

# Display portfolio
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}")

print(f"\nTotal Investment Value = ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("----- Portfolio Summary -----\n")

        for stock, qty in portfolio.items():
            file.write(
                f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n"
            )

        file.write(f"\nTotal Investment Value = ${total_investment}")

    print("Report saved as portfolio_report.txt")