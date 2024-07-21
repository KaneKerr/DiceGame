import random


new_game = True
amount = 0
my_list = []
rolled_number = 0
multiplier = 9900


for i in range(1, 100):
    my_list.append(i)
    rolled_number = random.choice(my_list)


def add_win_to_account():
    if rolled_number == 2:
        global amount
        amount += 1
    return amount


def set_amount():
    global amount
    amount = int(input("Enter Account size: "))


if new_game:
    set_amount()

print(rolled_number)
new_balance = add_win_to_account()
print("New balance is: " + str(new_balance))



