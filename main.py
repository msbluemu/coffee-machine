MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}



espresso_water = 50
expresso_milk = 0
expresso_coffee = 1.8
expresso_cost = 1.5

latte_water = 200
latte_milk = 150
latte_coffee = 24
latte_cost = 2.5

cappuccino_water = 250
cappuccino_milk = 100
cappuccino_coffee = 24
cappuccino_cost = 3.0

money = 0
are_resources_enough = True

def handle_coin(coffee_cost):
  print("Please insert coins")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies: "))
  total_coin_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
  if total_coin_value > coffee_cost:
      change = total_coin_value - expresso_cost
      print(f"Here is ${change} in change")
  else:
      print("Sorry that's not enough money. Money refunded.")

def serve_coffee(coffee_water, coffee_milk, coffee_coffee, coffee_cost):
    if resources["water"] >= coffee_water and resources["milk"] >= coffee_milk and resources["coffee"] >= coffee_coffee:
        handle_coin(coffee_cost)
        reduce_resources(coffee_water, coffee_milk, coffee_coffee, coffee_cost)
        print("Here is your coffee☕")
    else:
        if resources["water"] < coffee_water:
            print("Sorry, there is not enough water.")
        elif resources["milk"] < coffee_milk:
            print("Sorry, there is not enough milk.")
        elif resources["coffee"] < coffee_coffee:
            print("Sorry, there is not enough coffee.")

def reduce_resources(coffee_water, coffee_milk, coffee_coffee, coffee_cost):
    resources["water"] = resources["water"] - coffee_water
    resources["milk"] = resources["milk"] - coffee_milk
    resources["coffee"] = resources["coffee"] - coffee_coffee
    resources["money"] = resources["money"] + coffee_cost

def coffee_machine():
    is_machine_on = True
    while is_machine_on:
        choice = input("What would you like? (expresso/latte/cappuccino)")
        if choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk'] }ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: ${resources['money']}")
        elif choice == "expresso":
            serve_coffee(espresso_water, expresso_milk, expresso_coffee, expresso_cost)
        elif choice == "latte":
            serve_coffee(latte_water, latte_milk, latte_coffee, latte_cost)
        elif choice == "cappuccino":
            serve_coffee(cappuccino_water, cappuccino_milk, cappuccino_coffee, cappuccino_cost)
        else:
            is_machine_on = False

coffee_machine()