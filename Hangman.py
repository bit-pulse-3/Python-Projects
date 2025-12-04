import random

animals = [
    "elephant",
    "tiger",
    "dolphin",
    "chimpanzee",
    "penguin",
    "cheetah",
    "giraffe",
    "kangaroo",
    "octopus",
    "leopard",
    "rhinoceros",
]
countries = [
    "canada",
    "brazil",
    "germany",
    "australia",
    "nigeria",
    "india",
    "japan",
    "mexico",
    "egypt",
    "thailand",
    "italy",
]
cities = [
    "newyork",
    "paris",
    "tokyo",
    "dubai",
    "london",
    "beijing",
    "moscow",
    "sydney",
    "istanbul",
    "lagos",
    "toronto",
]
fruits = [
    "apple",
    "banana",
    "mango",
    "strawberry",
    "pineapple",
    "grapes",
    "watermelon",
    "orange",
    "kiwi",
    "blueberry",
    "raspberry",
]
print(len(animals))
body_parts = ["o", "|", "/", "\\", "/", "\\"]


def display_word(word_list):
    list_length = len(word_list)
    selected_word = ""
    index = random.randint(0, list_length - 1)
    word = animals[index]
    word_length = len(word)
    for i in range(word_length - 1):
        if i % 2 != 0:
            print(f"{word[i]}")
            selected_word[i] = word[i]
        else:
            selected_word[i] = "_"
    guess_count = 7
    while guess_count != 0:

        guess = input(f"Enter a letter(you have {guess_count} guess left): ")
        for i in range(word_length - 1):
            if i % 2 != 0:
                guess_count -= 1
                continue
            elif word[i] == guess:
                selected_word[i] = guess
            else:
                guess_count -= 1
                print("Incorrect Guess\n")


choice = input("Enter Y to start game anything else to exit:")
while choice == "Y" or choice == "y":
    word_type = int(
        input("\tChoose one\n1.Animals\n2.Countries\n3.Fruits\n4.Cities\n5.Exit\n")
    )
    match choice:
        case 1:
            display_word(animals)
        case 2:
            display_word(countries)
        case 3:
            display_word(cities)
        case 4:
            display_word(fruits)
        case 5:
            print("Exit Successful")
            break
    choice = input("Do you want to paly again press Y anything else  to exit:")
