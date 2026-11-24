import random

silver_rose_hp = 100
silver_rose_max_hp = 100

silver_rose_mp = 30
silver_rose_max_mp = 30

#Silver Rose Attacks
melee = 4

#Silver Rose Skills
axe_chop = 7
thorn_throw = 9
vine_clasp = 10

#Skills Cost
axe_chop_cost = 5
thorn_throw_cost = 8
vine_clasp_cost = 12

#Silver Rose Healing
rose_water = 10
#MP cost
rose_water_cost = 6

def user_skill (damage, cost):
    global silver_rose_mp
    if silver_rose_mp < cost:
        print("Not enough MP!")
        return 0
    silver_rose_mp -= cost
    return damage

def use_rose_water():
    global silver_rose_hp, silver_rose_mp
    if silver_rose_mp < rose_water_cost:
        print("Not enough MP!")
        return
    silver_rose_mp -= rose_water_cost
    silver_rose_hp = min(silver_rose_hp + rose_water, silver_rose_max_hp)


