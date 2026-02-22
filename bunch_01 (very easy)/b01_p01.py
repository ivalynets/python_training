#Характеристики персонажа
#Создай словарь с характеристиками героя (имя, HP, урон, броня). Выведи каждую характеристику в читаемом формате.

def determine_hero(name, hp, damage, armor):
    return {
        "name": name,
        "hp": hp,
        "damage": damage,
        "armor": armor,
    }

def main():
    new_hero = determine_hero('Stellarsson', 100, 20, 10)
    print_horizontal(new_hero)

def print_vertical(data):
    for key, value in data.items():
        print(f"{key}: {value}")

def print_horizontal(data):
    parts = [f"{key}: {value}" for key, value in data.items()]
    print(" | ".join(parts))

if __name__ == "__main__":
    main()