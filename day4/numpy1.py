import numpy as np
stock_prices = np.random.randint(100, 501, size=(30, 5))
average_prices = np.mean(stock_prices, axis=0)
max_price = np.max(stock_prices)
max_day, max_company = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
normalized_prices = (stock_prices - np.min(stock_prices, axis=0)) / (np.max(stock_prices, axis=0) - np.min(stock_prices, axis=0))
risky_investment_days = []
for day in range(30):
    risky_stocks = stock_prices[day] < 200
    if np.any(risky_stocks):
        risky_investment_days.append((day, stock_prices[day][risky_stocks].tolist()))
print("Average stock prices:", average_prices)
print("Highest price recorded:", max_price, "at Day", max_day, "Company", max_company)
print("Normalized prices:", normalized_prices)
print("Risky Investment Days:", risky_investment_days)
