import sys
from market_data import get_price
from risk_manager import calculate_risk

symbol = sys.argv[1]
quantity = float(sys.argv[2])

price = get_price(symbol)
value, risk = calculate_risk(price, quantity)

print("Symbol:", symbol)
print("Price:", price)
print("Quantity:", quantity)
print("Trade Value:", value)
print("Risk Level:", risk)