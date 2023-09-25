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
python ta_mean.py
```

## Outputs

- A CSV file (`btc120d.csv`) containing the raw price data.
- Print outputs showcasing:
  - Indicator values for long, short, and neutral signals.
  - Correlation matrix of the technical indicators.

```
Candle Look: 1

Long Indicators:
SMA_50           28049.622684
EMA_50           28051.898934
WMA_50           28047.986334
MACD_12_26_9        -2.209715
MACDh_12_26_9        1.611152
MACDs_12_26_9       -3.552037
RSI_14              51.390689
BBL_20_2.0       27767.701992
BBM_20_2.0       28042.665220
BBU_20_2.0       28317.628447
BBB_20_2.0           1.972844
BBP_20_2.0           0.586180
ADX_14              25.466383
DMP_14              23.919982
DMN_14              23.383517
STOCHk_14_3_3       49.057302
STOCHd_14_3_3       47.089886
WILLR_14           -43.710521
ROC_10               0.126203
CCI_20_0.015        17.634792
ATRr_14            108.337790

Short Indicators:
SMA_50           28104.670147
EMA_50           28102.504471
WMA_50           28098.732513
MACD_12_26_9        -5.598095
MACDh_12_26_9       -1.697540
MACDs_12_26_9       -3.774258
RSI_14              46.295607
BBL_20_2.0       27820.099935
BBM_20_2.0       28091.858225
BBU_20_2.0       28363.616515
BBB_20_2.0           1.945306
BBP_20_2.0           0.387167
ADX_14              25.191744
DMP_14              22.266426
DMN_14              24.917250
STOCHk_14_3_3       46.417236
STOCHd_14_3_3       48.421410
WILLR_14           -60.797696
ROC_10              -0.160188
CCI_20_0.015       -27.087475
ATRr_14            105.609088
```

## Upcoming Projects

- [Finding Features with XGBoost](https://github.com/tzelalouzeir/XGBoost_Indicators_2): Training and evaluating an XGBoost classifier on the Bitcoin technical indicators dataset. It aims to predict trading signals (like 'long', 'short', or 'neutral') based on the values of various indicators.
- [XGBoost Model Optimization](https://github.com/tzelalouzeir/XGBoost_Indicators_3): Up Comming...

## 🤝 Let's Connect!
Connect with me on [LinkedIn](https://www.linkedin.com/in/tzelalouzeir/).

For more insights into my work, check out my latest project: [tafou.io](https://tafou.io).

I'm always eager to learn, share, and collaborate. If you have experiences, insights, or thoughts about RL, Prophet, XGBoost, SARIMA, ARIMA, or even simple Linear Regression in the domain of forecasting, please create an issue, drop a comment, or even better, submit a PR! 

_Let's learn and grow together!_ 🌱


