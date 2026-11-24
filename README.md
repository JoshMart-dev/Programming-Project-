boss_hp = 150
boss_max_hp = 150

def boss_take_damage(amount):
    global boss_hp
    boss_hp = max(boss_hp - amount, 0)   # max() stops it going below 0
    print(f"Boss HP: {boss_hp}/{boss_max_hp}")
