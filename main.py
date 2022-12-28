import random


def continuegame():
    playagain = False
    response = input("Do you want to play again? y/n ")
    if response == "y":
        playagain = True
    return playagain


def guessanumber():
    guessint = int(input("Guess a number from 1 - 100: "))
    return guessint


def numberoftries():
    number = 10
    response = input("Difficulty level 'h' Hard or 'e' Easy: ")
    print("__________________________________")
    if response == "h":
        number = 5
    return number


def gameover(result, number, guessesleft):
    print("_________________________________________________________")
    if result == "win":
        print(f"You Win! The number was {number} and you had {guessesleft-1} tries left.")
    elif result == "lose":
        print(f"You Lost. The number was {number}. Better luck next time.")
    print("_________________________________________________________")


playing = True
while playing:
    gamenumber = random.randint(1, 100)
    triesleft = numberoftries()

    while triesleft > 0:
        guess = guessanumber()
        if guess == gamenumber:
            gameover("win", gamenumber, triesleft)
        elif guess > gamenumber:
            print("Guess is too high.")
            print("__________________________________")
            triesleft -= 1
        elif guess < gamenumber:
            print("Guess is too low.")
            print("__________________________________")
            triesleft -= 1
    if triesleft == 0:
        gameover("lose", gamenumber, triesleft)
    playing = continuegame()
