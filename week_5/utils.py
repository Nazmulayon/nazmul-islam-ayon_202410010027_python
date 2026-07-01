# utils.py

COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee, tea, sandwich):
    total = (coffee * COFFEE_PRICE) + (tea * TEA_PRICE) + (sandwich * SANDWICH_PRICE)
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    print("\n====== RECEIPT ======")
    print("Customer :", customer_name)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)
    print("---------------------")
    print(f"Total = RM {total:.2f}")