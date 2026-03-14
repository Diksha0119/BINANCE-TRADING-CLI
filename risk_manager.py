def calculate_risk(price, quantity):
    value = price * quantity

    if value < 100:
        level = "LOW"
    elif value < 1000:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return value, level