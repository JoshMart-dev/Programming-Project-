import glass_cannon
import silver_rose
import vanguard

inventory = {"Heal Potion": 1, "Elixir":1}
heal_potion = 10
elixir = 25

def use_item_heal():
    glass_cannon.glass_cannon_hp
    player_item_choice = int(input("Choose your item: 1 for Heal Potion, 2 for Elixir"))
    if player_item_choice == 1:
        if inventory["Heal Potion"] == 0:
            print("You're out of healing potions!")
        elif inventory["Heal Potion"] == 1:
            print("You used a healing potion!")
            glass_cannon.glass_cannon_hp += 10
    if player_item_choice == 2:
        if inventory["Elixir"] == 0:
            print("You're out of elixirs!")
        elif inventory["Elixir"] == 1:
            print("You used an elixir!")

    silver_rose.silver_rose_hp
    player_item_choice = int(input("Choose your item: 1 for Heal Potion, 2 for Elixir"))
    if player_item_choice == 1:
        if inventory["Heal Potion"] == 0:
            print("You're out of healing potions!")
        elif inventory["Heal Potion"] == 1:
            print("You used a healing potion!")
            silver_rose.silver_rose_hp += 10
    if player_item_choice == 2:
        if inventory["Elixir"] == 0:
            print("You're out of elixirs!")
        elif inventory["Elixir"] == 1:
            print("You used an elixir!")

    vanguard.vanguard_Hp
    player_item_choice = int(input("Choose your item: 1 for Heal Potion, 2 for Elixir"))
    if player_item_choice == 1:
        if inventory["Heal Potion"] == 0:
            print("You're out of healing potions!")
        elif inventory["Heal Potion"] == 1:
            print("You used a healing potion!")
            vanguard.vanguard_Hp += 10
    if player_item_choice == 2:
        if inventory["Elixir"] == 0:
            print("You're out of elixirs!")
        elif inventory["Elixir"] == 1:
            print("You used an elixir!")
