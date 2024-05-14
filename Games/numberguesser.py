import random as r

num = r.randint(1, 100)
guessed = False

while not guessed:
    guess = input("Guess my number (1-100) or type 'exit' to quit: ")
    if guess.lower() == 'exit':
        print("Exiting the game. Goodbye!")
        break
    try:
        numberChoosen = int(guess)
        if numberChoosen == num:
            print("You guessed correctly!")
            guessed = True
        elif numberChoosen > num:
            print("Lower")
        else:
            print("Higher")
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")
