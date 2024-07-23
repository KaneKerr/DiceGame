import random


new_game = True
amount = 0
my_list = []
rolled_number = 0
multiplier = 0
chosen_number = int(input("Enter bet number you wish for it to roll higher than: "))
start_num = 0

for i in range(1, 100):
    my_list.append(i)
    rolled_number = random.choice(my_list)


def add_win_to_account():
    bet_size = float(input("Eneter bet size lot: "))
    global amount
    if amount == 0:
        print("Deposit into account")
    elif bet_size > amount:
        print("Account size too small for bet")
    elif rolled_number > chosen_number:
        amount = bet_size * multiplier + amount
    return amount


def run_game():
    global multiplier
    global start_num
    while start_num < chosen_number:
        start_num += 1
        multiplier += 5
    return multiplier


def set_amount():
    global amount
    amount = int(input("Enter Account size: "))


if new_game:
    set_amount()


run_game_edit = run_game()
print("Your multiplier is: " + str(run_game_edit))
print("the number rolled was: " + str(rolled_number))
new_balance = add_win_to_account()
print("New balance is: " + str(new_balance))



