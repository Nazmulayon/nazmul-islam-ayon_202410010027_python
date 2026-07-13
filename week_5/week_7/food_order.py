def food_order(price, quantity):
    if price < 0:
        return "invalid price"
    if quantity < 0:
        return "invalid quantity"
    return price * quantity


def main():
    price = float(input("Price (RM): "))
    quantity = int(input("Quantity: "))

    total = food_order(price, quantity)

    if isinstance(total, str):
        print(total)
    else:
        print(f"Total Payment = RM {total:.2f}")


if __name__ == "__main__":
    main()