# Stratosphere Trading Bot

A Python-based trading bot that uses Alpaca's API to fetch market data and execute trades based on predictive strategies. This bot primarily focuses on stock trading using SPY (S&P 500 ETF) and can be adapted for options trading based on market analysis

- Fetches historical stock price data (SPY) from Alpaca's API.
- Implements a simple moving average (SMA) strategy to predict price movements.
- Places orders for stocks (or options, once integrated) based on price predictions.
- Allows real-time monitoring of SPY price changes and auto-execution of trades.

![istockphoto-155149307-612x612](https://github.com/user-attachments/assets/f775990f-f5f3-45ac-91a9-9303303a60f2)

# Installation

    Clone the repository:

    git clone https://github.com/bryantmluong/stratosphere.git

Install dependencies: You can install the required libraries using pip:

pip install -r requirements.txt

Set up Alpaca API credentials:

    Sign up for an Alpaca account at Alpaca Markets.
    Obtain your API_KEY and SECRET_KEY from the Alpaca dashboard.
    Create a config.py file in the src directory and add your credentials:
