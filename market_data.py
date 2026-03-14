from client import get_client

def get_price(symbol):
    client = get_client()
    data = client.get_symbol_ticker(symbol=symbol)
    return float(data["price"])