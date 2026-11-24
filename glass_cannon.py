glass_cannon_hp = 75
glass_cannon_max_hp = 75

glass_cannon_mp = 30
glass_cannon_max_mp = 30

# Attacks and damage value
melee = 4

# Skills and damage value
shatter_strike = 8
mighty_slash = 20

# Skill MP Costs
shatter_strike_mp = 5
mighty_slash_mp = 10

def user_skill (current_mp, damage, cost):
    global glass_cannon_mp
    if glass_cannon_mp < cost:
        print("Not enough MP!")
        return 0
    glass_cannon_mp -= cost
    return damage, current_mp
