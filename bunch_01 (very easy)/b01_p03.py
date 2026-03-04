#Жив ли персонаж? Напиши функцию, которая возвращает True/False.
#Затем напиши функцию которая возвращает новое значение HP (не ниже 0). Проверь на примере.

import b01_p01, random

def is_alive(hp):
    return hp > 0

def take_damage(hp, damage):
    new_hp = hp - damage
    return max(0, new_hp)

def main():
    new_hero = b01_p01.determine_hero('Stellarsson',10,5,3)
    print(f"Hero HP: {new_hero['hp']}")
    damage = random.randint(1,20)
    new_hero['hp'] = take_damage(new_hero['hp'],damage)
    print(f"Taken damage: {damage}")
    print(f"New hero HP: {new_hero['hp']}")
    print(is_alive(new_hero['hp']))

if __name__ == "__main__":
    main()