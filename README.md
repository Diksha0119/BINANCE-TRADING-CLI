#Binance Trading CLI

A modular Python command-line application that connects to the Binance Futures Testnet API to fetch real-time cryptocurrency prices and perform basic trade risk analysis.

## Features
- Fetch real-time crypto prices from Binance Futures Testnet
- Calculate trade value based on user-defined quantity
- Evaluate risk level of a trade (LOW / MEDIUM / HIGH)
- Simple command-line interface for quick market checks
- Modular code structure for easy extension

## Project Structure
cli.py – Command-line interface for executing the tool  
client.py – Binance API connection setup  
market_data.py – Fetches market price data  
risk_manager.py – Calculates trade risk levels  
config.py – Stores API credentials  
test.py – Test script for validating API connection

## Installation
Clone the repository
git clone https://github.com/Diksha0119/BINANCE-TRADING-CLI.git
Navigate to the project folder
cd BINANCE-TRADING-CLI
Install dependencies
pip install python-binance

## Usage

Run the CLI tool with a trading pair and quantity:
python3 cli.py BTCUSDT 0.01
Example Output

Symbol: BTCUSDT  
Price: 70688.83  
Quantity: 0.01  
Trade Value: 706.88  
Risk Level: MEDIUM

## Notes
This project uses the Binance Futures Testnet API for testing purposes only. No real trades are executed.
