# Number Classifier and Inventory Manager
# Student Name: Luis Patino
# Date: 10/21/2026
inventory = {} 
def add_item() :
    item = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity to add: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"{item} updated. Current quantity: {inventory[item]}")
    except ValueError:
        print("Invalid quantity. Please enter a number.")
def remove_item() :
    item = input("Enter item name to remove: ")
    if item in inventory:
        del inventory[item]
        print(f"(item) remove from inventory.")
    else:
        print("Item not found.") 
def classify_number():
    try:
        number = float(input("Enter a number: "))
        if number > 0:
            print("Positive number")
        elif number < 0:
            print("Negative number")
        else:
            print("Zero")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items() :
            print(f"- {item}: {quantity}")
while True:
    print("\nMenu")
    print("1. Classify a number")
    print("2. Add an inventory item")
    print("3. Remove an inventory item")
    print("4. View inventory")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        classify_number()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("Invalid menu choice. Try again.")                                                                                      