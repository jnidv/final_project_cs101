# Libraries
import random

# Classes

# Functions
def main_menu():
    # Main Menu
    print("""
______________________________________________________________________________________________________________________________________________
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                                                    +---+
                                                                    |   |
                                                                    O   |
                                                                   /|\  |
                                                                   / \  |
                                                                        |
                                                                 =========
______________________________________________________________________________________________________________________________________________
WELCOME TO SINGLEPLAYER HANGMAN IN PYTHON
By: Jan Neal Isaac D. Villamin
""")
    play = input("Press ENTER to play!: ")
    print("")

def ask_for_game_rule():
    # Game Rules
    game_rules = """GAME PLAY
The program will ask you to select an EDITION, themed sets of words. The executer will ask you a
random word from that EDITION.

A number of dashes equivalent to the number of letters in the word will be displayed. If a guessing 
player suggests a letter that occurs in the word, the program fills in the blanks with that 
letter in the right places. 

If the word does not contain the suggested letter, the program draws one element of a hangmans 
gallows. As the game progresses, a segment of the gallows and of a victim is added for every suggested 
letter not in the word. 

The number of incorrect guesses before the game 
ends is up to the difficulty of the game, but completing a character in a noose provides a minimum of 
six wrong answers until the game ends. The first player to guess the correct answer thinks of the word 
for the next game.

OBJECTIVE
Guess the word or phrase before your man gets hung!
"""

    yes_no_game_rules = input("Do you want to read the game rules? (y/n): ")
    print("")

    if yes_no_game_rules == "y":
        print(game_rules)

def select_edition():
    # Editions and selecting editions
    nba_players = ["lebron james", "stephen curry", "kevin durant", "giannis antetokounmpo", "james harden", "anthony davis", "damian lillard"]
    filipino_foods = ["adobo", "sinigang", "nilaga", "tinola", "bulalo", "menudo", "afritada", "kwek kwek", "balot", "taho"]
    santa_rosa_places = ["nuvali", "sm santa rosa", "robinsons santa rosa", "sports complex", "plaza", "target mall", "waltermart", "enchanted kingdom"]

    list_of_editions = [nba_players, filipino_foods, santa_rosa_places]

    id_of_edition_to_play = input("What edition do you want to play? [Type 1 - NBA players; Type 2 - Filipino Foods; Type 3 - Santa Rosa Places]: ")
    print("")

    edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1]
    return edition_to_play

def play_game():
    # Randomly selecting word
    random_index = random.randint(0, len(edition_to_play) - 1)
    word = edition_to_play[random_index]
    temporary_string = ""

    for letter in word:
        if letter != " ":
            temporary_string += "-"
        else:
            temporary_string += letter
    
    # Hangman ASCII arts
    hangman_arts = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
      |
 /|\  |
 / \  |
=========''']

    # Solo game main algorithm
    lives = len(hangman_arts) - 1
    print(temporary_string)
    print(hangman_arts[len(hangman_arts) - lives - 1])
    new_temporary_string = ""
    guess_word = ""

    while temporary_string != word and lives > 0 and guess_word != word:
        guess = input("Guess letter: ")
        guess_word = input("Guess word (press ENTER or type any KEY if you don't have any guess): ")
        print("")

        compare_string = temporary_string
        lives_string = "Lives: {}".format(lives)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    new_temporary_string = compare_string[:i] + guess + compare_string[i+1:]

                if new_temporary_string == "":
                    new_temporary_string = compare_string
                compare_string = new_temporary_string

            print(compare_string)
            print("Nice work! " + lives_string)
            print(hangman_arts[len(hangman_arts) - lives - 1])
            print("")

        else:
            if new_temporary_string == "":
                print(temporary_string)
            else:
                print(new_temporary_string)

            lives = lives - 1
            lives_string = "Lives: {}".format(lives)

            print("Oh no! The letter is not in the word. " + lives_string)
            print(hangman_arts[len(hangman_arts) - lives - 1])
            print("")

        if new_temporary_string != "":
            temporary_string = new_temporary_string

    if temporary_string == word or guess_word == word:
        print("You win! The word is " + word + ".")
    else:
        print("You lose! The word is " + word + ".")

# Play game
play = True
game_status = True

while game_status:
    main_menu()
    ask_for_game_rule()
    while play:  
        edition_to_play = select_edition()
        play_game()
        again = input("Play again? (y/n): ")
        if again == "n":
            play = False
    return_to_menu = input("Return to main menu? (y/n): ")
    if return_to_menu == "n":
        game_status = False


