# Game Center System

## Description
The Game Center is a collection of interactive Python games that users can run locally on their systems. It provides a simple interface to choose from various games, each offering a unique gaming experience. The game center is designed to be user-friendly, providing clear instructions on how to select and launch games.

## System Requirements
- **Operating System**: Any system that supports Python, including Windows, macOS, and Linux.
- **Python Version**: Python 3.x
- **Additional Libraries**: No additional libraries are required for the launcher itself, but individual games may have their requirements.(`pygame` is needed in `flappy bird.py`)

## Getting Started
To start using the Game Center, follow these simple steps:

1. **Clone the repository or download the files**: Ensure that all game scripts are placed in the `/Users/pusi/PycharmProjects/PYGames1/Games/` directory.
2. **Change the path to `word.txt` in `mainframe.py` to your own path**
2. **Navigate to the Game Center directory**:
   ```bash
   cd /path/to/game_center
   ```
3. **Run the main script**:
   ```bash
   python3 main.py
   ```

## Games Available
Enter the number corresponding to the game to open the corresponding game. The Game Center includes the following games:

1. [**Blackjack**](#1.-blackjack) - Test your luck and strategic thinking in this classic card game.
2. [**Hangman**](#2.-hangman) - Guess the word before you run out of chances.
3. [**Mainframe**](#3.-mainframe) - A simulation game where you manage mainframe resources (details provided in the game).
4. [**Number Guesser**](#4.-number-guesser) - Try to guess the randomly generated number with hints to guide you.
5. [**Tic Tac Toe**](#5.-tic-tac-toe) - Challenge the computer in this timeless grid game.
6. [**Flappy Bird**](#6.-flappy-bird) - Navigate the bird through obstacles without touching them.

## Rules

### 1. Blackjack

#### Objective
The primary goal is to reach a score of 21 or the closest to it without going over, using the cards dealt by the system.

#### Gameplay
- Each player starts with two cards.
- Players can choose to take additional cards (Hit) or stop at their current total (Stand).
- The game continues in rounds, where each player decides their next move.
- Players can view their current hand and total at any time.
- If a player's score exceeds 21, they lose immediately (Bust).

#### Commands
- **'s'** - Stand: Stop taking cards.
- **'c'** - Continue/Hit: Take another card.
- **'l'** - Look: Show your current hand and score.
- **'exit'** - Exit the game: Ends the game session immediately.

#### Game Flow
1. Shuffle the deck and deal two cards to each player.
2. Players take turns deciding their actions based on their current hand.
3. The game checks after each round if all players have finished their turns or have busted.
4. The game ends when all players are either busted or have stopped taking cards.

### 2. Hangman 
#### Objective
The main objective is to guess the word correctly using the least number of incorrect guesses. The hint provided helps in guessing the word related to its meaning.

#### Gameplay
- At the start, a word is selected randomly, and its corresponding hint is displayed.
- The word to guess is represented by question marks (e.g., `???` for a three-letter word).
- Players guess one letter at a time or can choose to guess the whole word.

#### Commands
- **Guess a letter**: Input a single letter to see if it's in the word.
- **'exit'**: Type 'exit' to quit the game at any time.

#### Game Flow
1. The game provides a hint related to the randomly selected word.
2. Players submit their guesses:
   - If the guessed letter is in the word, it replaces the corresponding question mark.
   - If the letter is not in the word, the number of remaining attempts decreases.
3. The game continues until the word is guessed or all attempts are used up.

#### Ending the Game
- If the word is guessed correctly, the player wins.
- If the player runs out of attempts, the hangman is 'hanged', and the game reveals the correct word.
- Players can choose to play another round or exit after each game.

### 3. Mainframe 
#### Objective
The main objective is to score points by creating valid words from a given set of letters. The game rewards longer words and the use of less common letters with higher points.

#### Gameplay
- At the start, players choose the number of characters for their hand and whether they want a wildcard character included.
- The game displays the player's hand of letters.
- Players attempt to form words using the letters in their hand.

#### Commands
- **Enter word**: Input a word using the letters provided. The game will calculate the score based on the word's length and letter values.
- **'exit'**: Type 'exit' at any prompt to quit the game.

#### Game Flow
1. The player specifies how many characters they want in their hand.
2. The player chooses between having a wildcard character in their hand or not.
3. The game displays the player's hand.
4. The player inputs words formed from the hand:
   - Points are calculated based on the letters used and the word's length.
   - The hand is updated after each valid word, removing used letters.
5. The process repeats until the player cannot form new words or chooses to exit.

### 4. Number Guesser
#### Objective
The goal is to guess the randomly selected number as quickly as possible. After each guess, the game provides feedback to help the player adjust their next guess.

#### Gameplay
- The game generates a random number between 1 and 100 at the start.
- Players guess the number, receiving hints to guess higher or lower based on their input.

#### Commands
- **Guess**: Input a number between 1 and 100 to make a guess.
- **'exit'**: Type 'exit' at any prompt to quit the game immediately.

#### Game Flow
1. The game starts and generates a random number.
2. The player enters a guess:
   - If the guess is correct, the game congratulates the player and ends.
   - If the guess is too high, the game advises guessing lower.
   - If the guess is too low, the game advises guessing higher.
3. This process repeats until the correct number is guessed or the player exits the game.

### 5. Tic Tac Toe
#### Objective
Be the first to get three of your marks in a row on the 3x3 grid.

#### Gameplay
- Players choose between being X or O at the start of the game.
- The game randomly decides who goes first.
- Players alternate turns, placing their mark in an empty spot.
- The game ends when one player has three marks in a row or all spaces are filled, resulting in a tie.

#### Commands
- **Number (1-9)**: Input a number to place your mark in the corresponding board position. The board positions are numbered 1 through 9 starting from the bottom left, moving horizontally.
- **'exit'**: Type 'exit' at any prompt to quit the game immediately.

#### Game Flow
1. Start the game and decide whether you are X or O.
2. The game will indicate who goes first.
3. On your turn, input the number of the position where you want to place your mark.
4. The game alternates turns between the player and the computer.
5. The game provides feedback and updates the board each turn.
6. Play continues until one player wins or all spaces are filled, ending in a tie.

### 6. Flappy Bird
#### Objective
Navigate the bird through the gaps between vertical pipes. The game increases in difficulty as you progress, with your score increasing each time you successfully pass through a gap.

#### Gameplay
- Tap the spacebar to make the bird 'flap' and rise slightly in the air; gravity will then pull it back down.
- Avoid colliding with the pipes or the ground.
- Aim to achieve the highest score possible by passing through as many gaps as you can.

#### Commands
- **Spacebar**: Make the bird jump.
- **'exit'**: Close the game window to quit the game.

#### Game Flow
1. The game starts with the bird in a fixed position on the screen.
2. Pipes will continuously move from right to left. New pipes are generated as you progress.
3. Use the spacebar to navigate the bird through the gaps.
4. The game ends if the bird hits a pipe or falls to the ground.

## Exiting the Game Center
To exit the game center, simply type `exit` at the prompt when choosing a game. This will terminate the session and close the application.

## Troubleshooting
If you encounter any issues with launching or playing the games, ensure that the file paths are correctly specified and that your Python environment is properly configured to execute scripts.

## Contribution
Contributions to the Game Center are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

