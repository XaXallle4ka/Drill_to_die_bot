import os, json

data = {}
with open("C:/Users/vlad0/Documents/GitHub/Drill_to_Die_TELEGRAM_BOT/Files/data.json") as file:
    data = json.load(file)

def __ParseItems():
    items = []
    for item in data["items"]:
        items.append([item["name"], item["price"], item['destription']])

    return items

def find_item_cost(item, items):
    for i in items:
        if i[0].lower() == item.lower():
            return i[1]

def find_item_description(item, items):
    for i in items:
        if i[0].lower() == item.lower():
            return i[2]

def __ParseShips():
    ships = []
    for ship in data["ships"]:
        sum_upgrades = 0
        for upgrade in ship['upgrades']:
            for lev_up in upgrade['levelUpgrades']:
                sum_upgrades += lev_up['price']
        ships.append([ship["name"], sum_upgrades, ship['description']])

    return ships

def find_ship_cost(ship, ships):
    for name in ships:
        if ship == name[0]:
            return name[1]

def find_ship_description(ship, ships):
    for name in ships:
        if ship == name[0]:
            return name[2]
