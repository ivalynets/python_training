#Бросок кубика. Напиши функцию roll_dice(sides), которая возвращает случайное число от 1 до sides. Вызови её для d6, d10 и d20, выведи результаты.

import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    print(f'd6: {roll_dice(6)}')
    print(f'd10: {roll_dice(10)}')
    print(f'd20: {roll_dice(20)}')
    
if __name__ == "__main__":
    main()