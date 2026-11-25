import math
import enemy
import silver_rose
import glass_cannon
import vanguard

glasscannon = 0
silverrose = 1

boss_hp = 150
boss_max_hp = 150

def userInterface (health, damage, current_mp):
    glass_cannon.glass_cannon_max_hp
    silver_rose.silver_rose_max_hp
    vanguard.vanguard_max_Hp

print()

print(
    "Who do you feel closest to? Are you strong & brittle, a technical"
    " strategist, or a protector of the masses?"
)
player_Hero = int(
    input("Choose a Character: Glass Cannon (0), Silver Rose (1), Vanguard(2): ")
)
if player_Hero == 0:
  print("You have chosen Glass Cannon!")
elif player_Hero == 1:
  print("You have chosen Silver Rose!")
elif player_Hero == 2:
  print("You have chosen Vanguard!")
print()

while boss_hp > 0:
  if player_Hero == 0 and glass_cannon.glass_cannon_hp <= 0:
    print("Glass Cannon has been defeated!")
    break
  elif player_Hero == 1 and silver_rose.silver_rose_hp <= 0:
    print("Silver Rose has been defeated!")
    break
  elif player_Hero == 2 and vanguard.vanguard_Hp <= 0:
    print("Vanguard has been defeated!")
    break

  player_choice = int(
      input("What's your move?: Melee (0), Skill (1), Item (2), Guard (3): ")
  )

  # --- PLAYERS FIRST ---
  if player_Hero == 0:
    if player_choice == 0:
      print("You did a melee attack!")
      boss_hp = max(0, boss_hp - glass_cannon.melee)
      print(f"Boss HP: {boss_hp}/{boss_max_hp}")
    elif player_choice == 1:
      player_skill_choice = int(
          input(
              "Which skill do you want to use?: 1 for Shatter Strike (8 dmg, 5"
              " mp), 2 for Mighty Slash (20 dmg, 10 mp): "
          )
      )
      if player_skill_choice == 1:
        result = glass_cannon.user_skill(
            glass_cannon.glass_cannon_mp,
            glass_cannon.shatter_strike,
            glass_cannon.shatter_strike_mp,
        )
        if result != 0:
          print("You used Shatter Strike!")
          boss_hp = max(0, boss_hp - result[0])
          print(f"Boss HP: {boss_hp}/{boss_max_hp}")
      elif player_skill_choice == 2:
        result = glass_cannon.user_skill(
            glass_cannon.glass_cannon_mp,
            glass_cannon.mighty_slash,
            glass_cannon.mighty_slash_mp,
        )
        if result != 0:
          print("You used Mighty Slash!")
          boss_hp = max(0, boss_hp - result[0])
          print(f"Boss HP: {boss_hp}/{boss_max_hp}")

  elif player_Hero == 1:
    if player_choice == 0:
      print("You did a melee attack!")
      boss_hp = max(0, boss_hp - silver_rose.melee)
      print(f"Boss HP: {boss_hp}/{boss_max_hp}")
    elif player_choice == 1:
      player_skill_choice = int(
          input(
              "Which skill do you want to use?: 1 for Axe Chop (7 dmg, 5 mp), 2"
              " for Thorn Throw (9 dmg, 8 mp), 3 for Vine Clasp (10 dmg, 12 mp),"
              " 4 for Rose Water (+10 HP, 6 mp): "
          )
      )
      if player_skill_choice == 1:
        dmg = silver_rose.user_skill(
            silver_rose.axe_chop, silver_rose.axe_chop_cost
        )
        if dmg > 0:
          print("You used Axe Chop!")
          boss_hp = max(0, boss_hp - dmg)
          print(f"Boss HP: {boss_hp}/{boss_max_hp}")
      elif player_skill_choice == 2:
        dmg = silver_rose.user_skill(
            silver_rose.thorn_throw, silver_rose.thorn_throw_cost
        )
        if dmg > 0:
          print("You used Thorn Throw!")
          boss_hp = max(0, boss_hp - dmg)
          print(f"Boss HP: {boss_hp}/{boss_max_hp}")
      elif player_skill_choice == 3:
        dmg = silver_rose.user_skill(
            silver_rose.vine_clasp, silver_rose.vine_clasp_cost
        )
        if dmg > 0:
          print("You used Vine Clasp!")
          boss_hp = max(0, boss_hp - dmg)
          print(f"Boss HP: {boss_hp}/{boss_max_hp}")
      elif player_skill_choice == 4:
        silver_rose.use_rose_water()
        print(
            f"Silver Rose healed! HP: {silver_rose.silver_rose_hp} | MP:"
            f" {silver_rose.silver_rose_mp}"
        )

  elif player_Hero == 2:
    if player_choice == 0:
      print("You used Shield Bash!")
      boss_hp = max(0, boss_hp - vanguard.shield_Bash)
      print(f"Boss HP: {boss_hp}/{boss_max_hp}")
    elif player_choice == 1:
      player_skill_choice = int(
          input(
              "Which skill do you want to use?: 1 for Slashing Flurry (15 dmg),"
              " 2 for Iron Wall (Block All Damage, 20 Strength): "
          )
      )
      if player_skill_choice == 1:
        print("You used Slashing Flurry!")
        boss_hp = max(0, boss_hp - vanguard.slashing_Flury)
        print(f"Boss HP: {boss_hp}/{boss_max_hp}")
      elif player_skill_choice == 2:
        vanguard.use_iron_Wall()
    elif player_choice == 3:
      vanguard.use_iron_Wall()

  if boss_hp > 0:
    if player_Hero == 0:
      glass_cannon.glass_cannon_hp -= enemy.boss_turn()
      glass_cannon.glass_cannon_hp = max(0, glass_cannon.glass_cannon_hp)
      print(
          f"{glass_cannon.glass_cannon_hp} HP |"
          f" {glass_cannon.glass_cannon_mp} MP"
      )
    elif player_Hero == 1:
      silver_rose.silver_rose_hp -= enemy.boss_turn()
      silver_rose.silver_rose_hp = max(0, silver_rose.silver_rose_hp)
      print(
          f"{silver_rose.silver_rose_hp} HP | {silver_rose.silver_rose_mp} MP"
      )
    elif player_Hero == 2:
      vanguard.take_damage(enemy.boss_turn())
      print(
          f"{vanguard.vanguard_Hp} HP | Shield:"
          f" {vanguard.vanguard_shield_Health} | Strength:"
          f" {vanguard.vanguard_Strength}"
      )
    print()

if boss_hp <= 0:
  print("You defeated the boss!")