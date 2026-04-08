import json

FILE_NAME = "inventory.txt"

# Load data from file
def load_inventory():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}

# Save data to file
def save_inventory(inventory):
    with open(FILE_NAME, "w") as f:
        json.dump(inventory, f)

# Add item
def add_item(inventory):
    name = input("Enter item name: ")
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    if qty < 0 or price < 0:
        print("Invalid input!")
        return

    inventory[name] = {"quantity": qty, "price": price}
    save_inventory(inventory)
    print("Item added!")

# Update item
def update_item(inventory):
    name = input("Enter item name: ")

    if name in inventory:
        qty = float(input("Enter new quantity: "))
        price = float(input("Enter new price: "))

        if qty < 0 or price < 0:
            print("Invalid input!")
            return

        inventory[name]["quantity"] = qty
        inventory[name]["price"] = price
        save_inventory(inventory)
        print("Item updated!")
    else:
        print("Item not found!")

# Display items
def display(inventory):
    if not inventory:
        print("Inventory is empty")
        return

    for item, details in inventory.items():
        print(item, "-> Qty:", details["quantity"], "Price:", details["price"])

# Main program
inventory = load_inventory()

while True:
    print("\n1.Add  2.Update  3.Display  4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_item(inventory)
    elif choice == '2':
        update_item(inventory)
    elif choice == '3':
        display(inventory)
    elif choice == '4':
        break
    else:
        print("Wrong choice")