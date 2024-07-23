import random


new_game = True
amount = 0
my_list = []
rolled_number = 0
multiplier = 9900
chosen_number = int(input("Enter bet number you wish for it to roll higher than: "))
bet_size = 0


for i in range(1, 100):
    my_list.append(i)
    rolled_number = random.choice(my_list)


def add_win_to_account():
    bet_size = float(input("Enetr bet size lot: "))
    global amount
    if amount == 0:
        print("Deposit into account")
    elif bet_size > amount:
        print("Account size too small for bet")
    elif rolled_number > chosen_number:
        amount = bet_size * multiplier + amount
    return amount


def set_amount():
    global amount
    amount = int(input("Enter Account size: "))


if new_game:
    set_amount()



print(rolled_number)
new_balance = add_win_to_account()
print("New balance is: " + str(new_balance))



