import random
from collections import Counter


def loader(wlists1):
    """Function for loading the words"""
    wfile = open("/Users/pusi/PycharmProjects/PYGames1/Games/words.txt", 'r')
    for line in wfile:
        wlists1.append(line.strip().lower())
    print(len(wlists1), "words are loaded !")


def displayhand(hand1):
    str1 = ''
    co = Counter(hand1)
    for i in co.elements():
        str1 = str1 + i + " "
    print(str1)


def calcword(word1, hand1, count):
    co1 = Counter(hand1)
    sum = 0
    sum1 = 0
    sum2 = 0
    if count[word1] != 0:
        for i in word1:
            sum += slv[i]
        sum1 = max(7 * len(word1) - 3 * (len(co1) - len(word1)), 1)
        sum2 = sum + sum1
        print("You have earned ", sum2, "points")
        return sum2
    else:
        print("Invalid word, Try again!")
        return 0


def updatehand(word1, count):
    lis1 = list(word1)
    co1 = Counter(lis1)
    count.subtract(co1)
    return count


def generatehand(n):
    str1 = ''
    co2 = Counter()
    for _ in range(n):
        num = random.randint(97, 122)
        str1 += chr(num)
    co2.update(list(str1))
    return co2


def generatewild(n):
    str1 = ''
    co2 = Counter()
    b = random.randint(1, n)
    for i in range(1, n + 1):
        if i == b:
            str1 += "*"
        else:
            num = random.randint(97, 122)
            str1 += chr(num)
    co2.update(list(str1))
    return co2


vowels = 'aeiou'
HAND_SIZE = 7

slv = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
       'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

wlists = []
loader(wlists)
count = Counter(wlists)

print("NOW, LET'S BEGIN THE GAME .......")

while True:
    try:
        n1 = input("No. of characters you want = ")
        if n1.lower() == 'exit':
            print("Exiting the game...")
            break
        n1 = int(n1)
        x = input("Now press 'W' if you want characters with wildcard entry too else, press 'H': ")
        if x.lower() == 'exit':
            print("Exiting the game...")
            break

        hand = generatewild(n1) if x.upper() == 'W' else generatehand(n1)

        displayhand(hand)
        hand_count = Counter(hand)

        while True:
            word = input("Enter word = ")
            if word.lower() == 'exit':
                print("Exiting the game...")
                break

            if not set(word).issubset(set(hand_count)):
                print("Invalid word, not all letters are in the hand.")
                continue

            points = calcword(word, hand, count)
            print(f"Scored {points} points.")
            hand_count = updatehand(word, hand_count)
            displayhand(hand_count)

    except KeyboardInterrupt:
        print("\nGame interrupted.")
        break
