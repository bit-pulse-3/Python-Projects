import random


start = input("To Start game press Y and press anything else to stop: ")
if start == "Y" or start == "y":
    while start != "N" and start != "n":
        print("Guess the number. You have three tries.")
        guess_count = 3
        key = random.randint(1, 10)
        while guess_count != 0:
            Guess = input(f"Enter a guess from 1 to 10:")
            guess_count -= 1
            try:
                Guess = int(Guess)
            except ValueError:
                print("Invalid Guess, Enter a integer.")
                continue
            if Guess > 10 or Guess < 1:
                print("Guess out of range.")
            elif Guess == key:
                print("You are the Winner!!!")
                start = input("Do you want to play again(Y/N):")
                if start == "N" or start == "n":
                    print("Game Exited")
                break
            elif Guess != key:
                print("Wrong Guess.")
                if guess_count == 0:
                    print("You Lost!!!")
                    start = input("Do you want to play again(Y/N):")
                    if start == "N" or start == "n":
                        print("Game Exited")
else:
    print("Game Exited.")
