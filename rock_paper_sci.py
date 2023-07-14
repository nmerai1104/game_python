import random

print("Rock, Paper, Scissors")

while True:
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print("User has chosen: " + choice_name)
    print("Now its computer turn.......")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer has chosen: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    result = (choice - comp_choice) % 3
    if result == 1:
        print("User wins!")
    elif result == 2:
        print("Computer wins!")
    else:
        print("Draw")

    ans = input("Do you want to play again? (Y/N)")
    if ans == 'n' or ans == 'N':
        break
