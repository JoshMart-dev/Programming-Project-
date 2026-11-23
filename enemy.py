import random

# --- attacks ---
claw_swipe = 10
tail_whip = 6
heavy_slam = 15

# --- skills ---
flame_breath = 20
shadow_strike = 18

def boss_turn():
    move = random.choice(["claw_swipe", "tail_whip", "heavy_slam",
                          "flame_breath", "shadow_strike"])

    if move == "claw_swipe":
        damage = claw_swipe
    elif move == "tail_whip":
        damage = tail_whip
    elif move == "heavy_slam":
        damage = heavy_slam
    elif move == "flame_breath":
        damage = flame_breath
    else:
        damage = shadow_strike

    print(f"Boss used {move}! Damage done to player: {damage}")
    return damage
