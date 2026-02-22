#Характеристики персонажа
#Создай словарь с характеристиками героя (имя, HP, урон, броня). Выведи каждую характеристику в читаемом формате.

def determineHero(name, hp, damage, armor):
    return {
        "name": name,
        "hp": hp,
        "damage": damage,
        "armor": armor,
    }

def main():
    newHero = determineHero('Stellarsson', 100, 20, 10)
    printHorizontal(newHero)

def printVertical(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

def printHorizontal(dict):
    for key, value in dict.items():
        print(f"{key}: {value}", end=' | ')
    print()

if __name__ == "__main__":
    main()