from client import get_client

client = get_client()
price = client.get_symbol_ticker(symbol="BTCUSDT")

print("Connected to Binance successfully!")
print("BTCUSDT price:", price["price"])