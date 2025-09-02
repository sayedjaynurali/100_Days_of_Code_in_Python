# ==============================
# Coffee Machine Simulation
# ==============================

# Current resources in the coffee machine
machine_stats = {
    "water" : 500,   # in milliliters
    "milk" : 500,    # in milliliters
    "coffee": 500,   # in grams
    "money" : 500    # in dollars
}

# Units for each resource (used in reporting)
units = {
    "water" : "ml",
    "milk" : "ml",
    "coffee": "g",
    "money" : "$"
}

# Resource requirements + cost for each coffee type
coffee_costs = {
    "espresso" : {"water" : 50, "milk" : 0, "coffee": 18, "money" : 1.5},
    "latte" : {"water" : 200, "milk" : 150, "coffee": 24, "money" : 2.5},
    "cappuccino" : {"water" : 250, "milk" : 100, "coffee": 24, "money" : 3}
}

# ==============================
# Function: Check if enough resources are available
# ==============================
def check_requrements(coffee):
    for j in machine_stats:
        if j in ['water', 'milk', 'coffee']:  # Only check ingredients, not money
            if machine_stats[j] < coffee_costs[coffee][j]:   # Not enough ingredient
                print(f"Insufficient {j.capitalize()} for {coffee.capitalize()}")
                return False
            elif machine_stats[j] >= coffee_costs[coffee][j]:  # Deduct ingredients
                machine_stats[j] -= coffee_costs[coffee][j]
                continue

# ==============================
# Function: Handle payment
# ==============================
def check_money(coffee_name):
    # Values of each coin type
    collected_money = {"quarters" : 0.25, "dimes" : 0.10, "nickles" : 0.05, "pennies" : 0.01}
    total_money = 0

    # Ask user how many coins they insert
    for k in collected_money:
        coin = int(input(f"How many {k} you have entered? "))
        collected_money[k] *= coin

    # Sum all inserted coins
    for l in collected_money:
        total_money += collected_money[l]

    print(f"Total Money Entered is {total_money}.")

    # Check if enough money was inserted
    if total_money < coffee_costs[coffee_name]['money']:
        print("Insufficient Money Entered. Money Refunded!")
        return False
    elif total_money >= coffee_costs[coffee_name]['money']:
        balance_money = total_money - coffee_costs[coffee_name]['money']  # Calculate change
        machine_stats["money"] += coffee_costs[coffee_name]['money']      # Machine keeps only coffee price
        return balance_money

# ==============================
# Main Loop
# ==============================
on_off = True

while on_off == True:

    # Create menu dynamically
    menu = "\nWhat would you like?\n"
    for m in coffee_costs:
        menu += f"{m} - ${coffee_costs[m]['money']}\n"
    user_input = input(f"{menu}Enter your choice: ")

    # Option: Turn off the machine
    if user_input == "off":
        print("Coffee Machine Turned Off! Good Bye!")
        on_off = False

    # Option: Report current machine stats
    elif user_input == "report":
        for i in machine_stats:
            print(f"\n{i.capitalize()}: {machine_stats[i]}{units[i]}")

    # Option: Order a coffee
    elif user_input in coffee_costs:
        if check_requrements(user_input) != False:   # Check if enough ingredients
            print(f"Starting to make a {user_input}... please insert coins.")
            balance = check_money(user_input)        # Ask for coins
            if balance != False:
                print(f"Thank you! Here is your {user_input.capitalize()}. Your balance is ${balance:.2f}. Enjoy your Coffee.")
                continue
