import random


def prompt_to_int(prompt, min_value=None, max_value=None):
    while True:
        str_value = input(prompt)
        if not str_value.isdigit():
            print('enter a numerical value')
            continue
        int_value = int(str_value)
        if max_value and int_value > max_value:
            print(f'enter digit that will be lower or equal then {max_value}')
            continue
        if min_value and int_value < min_value:
            print(f'enter digit that will be higher or equal then {min_value}')
            continue
        return int_value


def fahrenheit(temperature):
    celsius = (temperature - 32) * 5/9
    if celsius < 10:
        print('cold')
    elif 10 < celsius < 28:
        print('not cold')
    elif 28 < celsius < 36:
        print('warm')
    elif celsius > 36:
        print('very warm')
    return celsius


def prompt_for_bool(prompt):
    while True:
        str_value = input(prompt)
        if str_value not in ['yes', 'no']:
            print('please enter yes or no')
            continue
        return str_value


part_of_the_task = prompt_to_int('please enter which task do you want to see (just number 1-4): ', 1, 4)

# task_1
if part_of_the_task == 1:
    helper = 0
    amount_of_food = prompt_to_int('pleas write how much meals do you want to order: ', 0)  # you can not order negative number of dishes
    for item in range(amount_of_food):
        price_of_dish = prompt_to_int('pleas write the price of the dishes that you ordered: ', 0)  # price can not be negative
        helper += price_of_dish  # total amount of meal

    tips_in_percent = prompt_to_int('pleas enter how much tips do you wont to keep: ', 0, 100)
    if helper > 2000:
        with_discount = helper * 0.9
        tip = with_discount * tips_in_percent / 100
        total_amount = with_discount + tip
        print(f'total amount of meal: {helper}$, total amount of meal with discount: {with_discount}$, '
              f'amount of tip: {tip}$,total amount with tips: {total_amount}$')
    else:
        tip = helper * tips_in_percent / 100
        total_amount = helper + tip
        print(f'total amount of meal: {helper}%, amount of tip: {tip}%, '
              f'final price: {total_amount}%')

# task_2
if part_of_the_task == 2:
    total_temperature = 0
    helper_list = []
    for i in range(7):
        temperature_in_F = prompt_to_int(f'please enter temperature for day {i+1} in fahrenheit: ')
        temperature_in_C = fahrenheit(temperature_in_F)
        helper_list.append(temperature_in_C)
        total_temperature += temperature_in_C
    min_temperature = min(helper_list)
    max_temperature = max(helper_list)
    print(f'min temperature: {min_temperature}, max temperature: {max_temperature}, average: {total_temperature / 7}')

# task_3
if part_of_the_task == 3:
    your_hp = 50
    enemy_hp = 50
    enemy_attack = random.randint(5, 20)
    my_attack = random.randint(5, 15)
    my_heal = random.randint(5, 10)
    while your_hp >= 0 and enemy_hp >= 0:
        user_choice = input(f'your hp = {your_hp}, and your enemy hp = {enemy_hp} '
                            f'pleas enter "a" if you wont to attack, and enter "h" if you want to heal: ')
        if user_choice not in ['a', 'h']:
            print('you must chose "a" or "h"!')
            continue
        if user_choice == 'a':
            enemy_hp -= my_attack
            your_hp -= enemy_attack
        if user_choice == 'h':
            your_hp += my_heal
            your_hp -= enemy_attack
    if your_hp > 0:
        print('congratulations! You won)')
    else:
        print('uncongratulations( You lose')

# task_4
if part_of_the_task == 4:
    saving_money = 0
    salary_total = prompt_to_int('please enter your total salary: ', 0)  # no upper limit
    saving_percent = prompt_to_int('please enter how much you can save each month (in percents) ', 0, 100)
    interest_in_the_bank = prompt_to_int('please enter your monthly interest in the bank ', 0, 100)
    i = 1
    while True:
        saving_from_salary = salary_total * saving_percent / 100
        saving_money += (saving_money * interest_in_the_bank / 100) + saving_from_salary
        print(f'{saving_money} - balance of money in the bank {i} month')
        if i == 12:
            option = prompt_for_bool('Do you want to continue saving money: ')
            if option == 'yes':
                i = 1
                continue
            else:
                print(f'removed {saving_money}$, we hope that you will choose our bank again in the future, good luck!')
                break
        i += 1
