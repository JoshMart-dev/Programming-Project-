#Vanguard's Health
vanguard_Hp = 115
vanguard_max_Hp = 115

#Vanguard's Shield Health & Strength
vanguard_shield_Health = 50
vanguard_max_shield_Health = 50
vanguard_Strength = 100

#Vanguard attacks
shield_Bash = 10
slashing_Flurry = 15

#Vanguard's shield skill & Cost
iron_Wall = 100
iron_wall_Cost = 20

#Use of skill check
guarding = False

#Uses the shield
def use_iron_Wall():
    global vanguard_Strength, guarding

    if vanguard_Strength>= iron_wall_Cost:
        vanguard_Strength -= iron_wall_Cost
        guarding = True
        print(f"You used Iron Wall! "
              "All incoming damage makes no effect! "
              f"(Strength left {vanguard_Strength})")

    else:
        print("You're not strong enough to use Iron Wall anymore!")

#Vanguard Shield Passive Damage Mitigation
def take_damage (damage):
    global vanguard_shield_Health, vanguard_Hp, guarding

    if guarding:
        print("Your shield stopped all damage! You took 0 damage!")
        guarding = False
        return

    if vanguard_shield_Health:
        damage = round(damage * 0.7)

    if vanguard_shield_Health >= damage:
        vanguard_shield_Health -= damage
    else:
        passive_Protection = damage - vanguard_shield_Health
        vanguard_shield_Health = 0
        vanguard_Hp = max(0, vanguard_Hp - passive_Protection)










