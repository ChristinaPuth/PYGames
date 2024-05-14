import random
import wordandmeaning

print("Hangman game .....................")
print("Guessing was never so much fun.............. ")

while True:
    j = random.randint(0, 9)
    str1 = wordandmeaning.word(j)
    str2 = wordandmeaning.meaning1(j)
    print("Hint for the word = ", str2)

    n = len(str1)
    lists = ['?'] * n  # Simplified way to initialize the list
    attempts = 4

    while attempts > 0:
        char = input("Guess a letter or type 'exit' to quit: ")
        if char.lower() == 'exit':
            print("Exiting game...")
            exit()

        found = False
        for idx in range(len(str1)):
            if str1[idx] == char:
                lists[idx] = char
                found = True

        print("".join(lists))

        if "".join(lists) == str1:
            print("You got the word, Congratulations :)")
            break

        if not found:
            attempts -= 1
            print(f"No such letter. You have {attempts} attempts left.")

    if "".join(lists) != str1:
        print("""(x x)
|
|
/\\ ,Hanged..............""")
        print("The word was ", str1)

    # If you want the game to loop, you could ask here if they want to play another round
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
