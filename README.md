# CodeAlpha_Stock_Portfolio_Tracker
<h1 align="center">
  <br>
  <pre>
  ╔══════════════════════════════════════╗
  ║   STOCK  PORTFOLIO  TRACKER          ║
  ║   ──────────────────────────────     ║
  ║   AAPL   x10   =   $1,800.00         ║
  ║   TSLA   x5    =   $1,250.00         ║
  ║   NVDA   x2    =   $1,900.00         ║
  ║   ──────────────────────────────     ║
  ║   TOTAL        =   $4,950.00         ║
  ╚══════════════════════════════════════╝
  </pre>
  <br>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Task-2%20of%204-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CodeAlpha-Internship-6C63FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-28C840?style=for-the-badge"/>
</p>

<p align="center">
  A terminal-based stock portfolio tracker built with pure Python.<br>
  Enter your stock holdings and instantly see your total investment value.
</p>

---

## Preview

```
====================================================
       STOCK PORTFOLIO TRACKER
====================================================

  Available Stocks
  ──────────────────────────────
  Symbol       Price (USD)
  ──────────────────────────────
  AAPL           $180.00
  TSLA           $250.00
  GOOGL          $140.00
  AMZN           $185.00
  MSFT           $415.00
  NFLX           $605.00
  META           $520.00
  NVDA           $950.00
  ──────────────────────────────

  Enter your stock holdings.
  Type 'done' when finished.

  Stock symbol: AAPL
  Quantity of AAPL: 10
  Added AAPL x 10

  Stock symbol: NVDA
  Quantity of NVDA: 2
  Added NVDA x 2

  Stock symbol: done

  ====================================================
  PORTFOLIO SUMMARY
  ====================================================
  Symbol    Qty   Price (USD)   Value (USD)
  ----------------------------------------------------
  AAPL       10      $180.00     $1,800.00
  NVDA        2      $950.00     $1,900.00
  ----------------------------------------------------
  TOTAL                          $3,700.00
  ====================================================
```

---

## Features

- Displays a list of 8 available stocks with hardcoded prices
- User inputs stock symbols and quantities interactively
- Handles duplicate entries by adding to existing quantity
- Calculates per-stock value and grand total automatically
- Offers to save results as CSV, TXT, or both
- Full input validation — rejects unknown symbols and invalid quantities

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CodeAlpha_StockPortfolioTracker.git

# Navigate into the folder
cd CodeAlpha_StockPortfolioTracker

# Run the program
python stock_portfolio_tracker.py
```

---

## How to Use

| Step | Action |
|------|--------|
| 1 | View the list of available stocks and their prices |
| 2 | Type a stock symbol (e.g. `AAPL`) and press Enter |
| 3 | Enter the quantity you hold |
| 4 | Repeat for as many stocks as you want |
| 5 | Type `done` to finish entering stocks |
| 6 | View your portfolio summary with totals |
| 7 | Choose to save as CSV, TXT, both, or skip |

---

## Available Stocks

| Symbol | Company | Price (USD) |
|--------|---------|-------------|
| AAPL | Apple Inc. | $180.00 |
| TSLA | Tesla Inc. | $250.00 |
| GOOGL | Alphabet Inc. | $140.00 |
| AMZN | Amazon.com Inc. | $185.00 |
| MSFT | Microsoft Corp. | $415.00 |
| NFLX | Netflix Inc. | $605.00 |
| META | Meta Platforms | $520.00 |
| NVDA | NVIDIA Corp. | $950.00 |

---

## Output Files

When saving, the program creates these files in the current directory:

| File | Format | Contents |
|------|--------|----------|
| `portfolio.csv` | CSV | Symbol, Quantity, Price, Value — importable into Excel |
| `portfolio.txt` | Plain text | Formatted summary table |

---

## Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py   # Main program file
└── README.md                    # Project documentation
```

---

## Concepts Used

| Concept | Usage |
|---------|-------|
| `dictionary` | Stores hardcoded stock prices |
| `input / output` | Reads user stock entries from terminal |
| `arithmetic` | Calculates per-stock and total portfolio value |
| `file handling` | Saves results to CSV and TXT files |
| `functions` | Separates logic into clean, reusable blocks |
| `loops` | Keeps accepting stock entries until user types done |

---

## Internship

This project was built as **Task 2** of the **CodeAlpha Python Programming Internship**.

> CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This internship empowers students to master Python fundamentals through real-world projects.

**Intern:** `SAMIRAN HAZRA`  
**Domain:** Python Programming  
**Task:** 2 — Stock Portfolio Tracker  


---
## Connect

<p>

  </a>
  <a href="https://github.com/cypherbytes01">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

<p align="center">
  Made with Python — CodeAlpha Internship 2026
</p>
