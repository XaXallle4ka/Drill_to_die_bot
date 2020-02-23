import os, json
from translator import *

data = {}
with open("C:/Users/vlad0/Documents/GitHub/Drill_to_Die_TELEGRAM_BOT/Files/data.json") as file:
    data = json.load(file)

def parseItems():
    items = []
    for item in data["items"]:
        items.append([item["name"], item["price"], str(' '.join(translate_me(item['destription'])['text']))])
    return items

def find_item_cost(item, items):
    for i in items:
        if i[0].lower() == item.lower():
            return i[1]

def find_item_description(item, items):
    for i in items:
        if i[0].lower() == item.lower():
            return i[2]

def parseShips():
    ships = []
    for ship in data["ships"]:
        upgrade_list = {}
        sum_upgrades = 0
        for upgrade in ship['upgrades']:
            for lev_up in upgrade['levelUpgrades']:
                upgrade_list[' '.join(translate_me(upgrade['name'])['text']) + ' уровень ' + str(lev_up['level'])] = 'цена = ' + str(lev_up['price']) + '\n' + '\n'
                sum_upgrades += lev_up['price']
        ships.append([ship["name"], sum_upgrades, ' '.join(translate_me(ship['description'])['text']), upgrade_list])

    return ships

def find_ship_cost(ship, ships):
    for name in ships:
        if ship == name[0]:
            return name[1]

def find_ship_description(ship, ships):
    for name in ships:
        if ship == name[0]:
            return name[2]

def find_ship_upgrades(ship, ships):
    output = ''
    for name in ships:
        if ship == name[0]:
            for upgrade in name[3].keys():
                output += upgrade + ':' + '\n'
                for n in name[3][upgrade]:
                    output += n
            return output
 