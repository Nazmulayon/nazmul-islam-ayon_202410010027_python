def food_order(price, quantity):
    if price <= 0:
        return "invalid price"

    if quantity <= 0:
        return "invalid quantity"

    return calculate_total(price, quantity)


def calculate_total(price, quantity):
    return price * quantity