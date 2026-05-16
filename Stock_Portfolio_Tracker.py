import csv
import os

# ─────────────────────────────────────────────
#  Stock Portfolio Tracker — CodeAlpha Python Internship
#  Task 2
# ─────────────────────────────────────────────

# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL":  180.00,
    "TSLA":  250.00,
    "GOOGL": 140.00,
    "AMZN":  185.00,
    "MSFT":  415.00,
    "NFLX":  605.00,
    "META":  520.00,
    "NVDA":  950.00,
}


def show_available_stocks() -> None:
    """Display all available stocks and their prices."""
    print("\n  Available Stocks")
    print("  " + "-" * 30)
    print(f"  {'Symbol':<10} {'Price (USD)':>12}")
    print("  " + "-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>11.2f}")
    print("  " + "-" * 30)


def get_portfolio() -> dict:
    """Prompt the user to enter stock symbols and quantities."""
    portfolio = {}

    print("\n  Enter your stock holdings.")
    print("  Type 'done' when finished.\n")

    while True:
        symbol = input("  Stock symbol: ").strip().upper()

        if symbol == "DONE":
            if not portfolio:
                print("  No stocks entered. Please add at least one stock.")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not in the available list. Try again.")
            continue

        qty_input = input(f"  Quantity of {symbol}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("  Quantity must be a positive integer.")
                continue
        except ValueError:
            print("  Invalid quantity. Please enter a whole number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"  Updated {symbol} — total quantity: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"  Added {symbol} x {quantity}")

    return portfolio


def calculate_portfolio(portfolio: dict) -> list:
    """Return a list of rows: (symbol, quantity, price, total_value)."""
    rows = []
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        total = price * quantity
        rows.append((symbol, quantity, price, total))
    return rows


def display_summary(rows: list) -> float:
    """Print a formatted portfolio summary and return the grand total."""
    print("\n  " + "=" * 52)
    print("  PORTFOLIO SUMMARY")
    print("  " + "=" * 52)
    print(f"  {'Symbol':<8} {'Qty':>5} {'Price (USD)':>13} {'Value (USD)':>13}")
    print("  " + "-" * 52)

    grand_total = 0.0
    for symbol, quantity, price, total in rows:
        print(f"  {symbol:<8} {quantity:>5} ${price:>12.2f} ${total:>12.2f}")
        grand_total += total

    print("  " + "-" * 52)
    print(f"  {'TOTAL':<8} {'':>5} {'':>13} ${grand_total:>12.2f}")
    print("  " + "=" * 52)
    return grand_total


def save_to_csv(rows: list, grand_total: float, filename: str = "portfolio.csv") -> None:
    """Save the portfolio summary to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for symbol, quantity, price, total in rows:
            writer.writerow([symbol, quantity, f"{price:.2f}", f"{total:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{grand_total:.2f}"])
    print(f"\n  Portfolio saved to '{os.path.abspath(filename)}'.")


def save_to_txt(rows: list, grand_total: float, filename: str = "portfolio.txt") -> None:
    """Save the portfolio summary to a plain text file."""
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write("=" * 52 + "\n")
        f.write(f"{'Symbol':<8} {'Qty':>5} {'Price (USD)':>13} {'Value (USD)':>13}\n")
        f.write("-" * 52 + "\n")
        for symbol, quantity, price, total in rows:
            f.write(f"{symbol:<8} {quantity:>5} ${price:>12.2f} ${total:>12.2f}\n")
        f.write("-" * 52 + "\n")
        f.write(f"{'TOTAL':<8} {'':>5} {'':>13} ${grand_total:>12.2f}\n")
        f.write("=" * 52 + "\n")
    print(f"  Portfolio saved to '{os.path.abspath(filename)}'.")


def ask_save_option(rows: list, grand_total: float) -> None:
    """Ask the user whether to save the results and in what format."""
    print("\n  Would you like to save the portfolio?")
    print("  1 - Save as CSV")
    print("  2 - Save as TXT")
    print("  3 - Save both")
    print("  4 - Do not save")

    choice = input("\n  Enter choice (1/2/3/4): ").strip()

    if choice == "1":
        save_to_csv(rows, grand_total)
    elif choice == "2":
        save_to_txt(rows, grand_total)
    elif choice == "3":
        save_to_csv(rows, grand_total)
        save_to_txt(rows, grand_total)
    elif choice == "4":
        print("  Results not saved.")
    else:
        print("  Invalid choice. Results not saved.")


def main() -> None:
    print("=" * 52)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 52)

    show_available_stocks()

    portfolio = get_portfolio()
    rows = calculate_portfolio(portfolio)
    grand_total = display_summary(rows)
    ask_save_option(rows, grand_total)

    print("\n  Thank you for using the Stock Portfolio Tracker.\n")


if __name__ == "__main__":
    main()
