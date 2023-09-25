# Crypto Technical Analysis

This repository contains Python code that fetches 120 days of hourly Bitcoin price data from Yahoo Finance, calculates various technical indicators, and analyzes the relations between these indicators.

## Features

1. **Fetching Data**: The code fetches 120 days of hourly Bitcoin price data.
2. **Indicator Calculation**: It calculates 12 different technical indicators such as SMA, EMA, MACD, RSI, etc.
3. **Signal Generation**: Based on the close prices, the code generates long, short, or neutral signals.
4. **Indicator Analysis**: It calculates average values of each indicator at points where signals are generated and creates a correlation matrix for the indicators.

## Installation

Make sure you have the following Python packages installed:

- `pandas`
- `yfinance`
- `pandas_ta`

You can install them using `pip`:

```bash
pip install pandas yfinance pandas_ta
```

## Usage

1. Clone this repository.
2. Navigate to the repository's root directory in your terminal.
3. Run the code using the following command:

```bash
python <filename>.py
```

Replace `<filename>` with the name you've saved the provided code as.

## Outputs

- A CSV file (`btc120d.csv`) containing the raw price data.
- Print outputs showcasing:
  - Indicator values for long, short, and neutral signals.
  - Correlation matrix of the technical indicators.

## Upcoming Projects

- [Repo2](<link-to-repo2>): Short description of Repo2.
- [Repo3](<link-to-repo3>): Short description of Repo3.

