import random


new_game = False
amount = 0
my_list = list(range(1, 100))
rolled_number = random.choice(my_list)
multiplier = 0
start_num = 0

start_again = (input("Type 'Yes/yes' if you want to start again: "))


if start_again == "Yes" or start_again == "yes":
    new_game = True


def get_valid_number():
    while True:
        chosen_number2 = int(input("Enter bet number you wish for it to roll higher than between the numbers 1 and 99: "))
        if chosen_number2 >= my_list[0] and chosen_number2 <= my_list[98]:
            return chosen_number2
        else:
            print("Invalid number. Choose between 1 and 99.")


chosen_number = get_valid_number()


def add_win_to_account():
    global amount
    bet_size = float(input("Enter bet size lot: "))
    if bet_size > amount:
        print("Account size too small for bet")
    elif rolled_number > chosen_number:
        amount = bet_size * multiplier + amount
    return amount


def add_multi():
    global multiplier
    global start_num
    while start_num < chosen_number:
        start_num += 1
        multiplier += 5
    return multiplier


def set_amount():
    while True:
        global amount
        amount = float(input("Enter Account size: "))
        if amount == 0:
            print("Deposit into account")
        else:
            return amount


if new_game:
    set_amount()

run_game_edit = add_multi()
print("Your multiplier is: " + str(run_game_edit))
new_balance = add_win_to_account()
print("the number rolled was: " + str(rolled_number))
print("New balance is: " + str(new_balance))


