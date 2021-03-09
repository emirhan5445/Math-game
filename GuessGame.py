import random
def who_goes_first():   
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"
def player_guess():
    guess = int(input("find the target number"))
    player_guesses = []
    if guess not in player_guesses:
        player_guesses.append(guess)
    else:
        print("bunu zaten seçmiştin")
def computer_guess():
    find_number = random.choice([*range(21)])
    computer_guesses = []
    if find_number not in computer_guesses:
        computer_guesses.append(find_number)
    else:
        None
def winner(target_number,find_number,guess):
    if turn == "computer":
        if guess == target_number:
            print("tebrikler 5 denemede buldunuz")
        else:
            None
    elif turn == "player":
        if find_number == target_number:
            print("the computer is win ")
        else:
            None
win = True
turn = who_goes_first()
if turn == "computer":
    print("the computer goes first! find the target number")
    target_number = random.choice([*range(21)])
    while win:
        player_guess()
        winner(find_number,guess)
        win = False
elif turn == "player":
    print("the player goes first!")
    target_number = int(input("choose a number between 0 and 20\t"))
    while win:
        computer_guess()
        winner(find_number,guess)
        win = False
    
