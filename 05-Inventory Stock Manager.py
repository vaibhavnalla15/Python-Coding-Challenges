""" Create a program to manage a small store’s inventory. """

# Store items with their quantities and prices.
# Allow checking total stock value.
# Allow finding the item with the highest total value (price × quantity).

# Constraints:
# Quantities and prices are positive integers.
# At least one item present in the inventory.

inventory = {
    "apple": {"quantity": 10, "price": 30},
    "banana": {"quantity": 5, "price": 10},
    "mango": {"quantity": 8, "price": 50}
}

total_value = 0
highest_item = None
highest_value = 0

for item, details in inventory.items():
    value = details["quantity"] * details["price"]
    total_value += value
    if value > highest_value:
        highest_value = value
        highest_item = item

print(f"Total stock value: {total_value}")
print(f"Highest value item: {highest_item} ({highest_value})")