# Libraries
import random

# Functions
def main_menu():
    # Main Menu
    print("""
______________________________________________________________________________________________________________________________________________
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █    +---+
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █    |   |
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒   O   |
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒  /|\  |
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░  / \  |
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒        |
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░=========
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
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

    correct = True
    while correct:
        id_of_edition_to_play = input("What edition do you want to play? [Type 1 - NBA players; Type 2 - Filipino Foods; Type 3 - Santa Rosa Places;]: ")
        print("")

        list_of_number_str = []
        for i in range(len(list_of_editions)):
            list_of_number_str.append(str(i+1))

        if id_of_edition_to_play in list_of_number_str:
            edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1]
            correct = False
            return edition_to_play
            

def play_game():
    # Dialogues
    dialogues_start = ["Please help me!", "You can do it!", "Focus!", "I love you! So please save me."]
    random_index1 = random.randint(0, len(dialogues_start) - 1)
    dialogue = dialogues_start[random_index1]

    negative_dialogues = ["Better guess that word!", "Anything happens, just know that I love you", "I know you can do better than that!", 
    "Oh c'mon!"]
    
    positive_dialogues = ["Good job!", "Keep it up!", "Whooo!", "GRAPE!"]

    # Story
    hangman = input("Name your hangman: ")
    gender = input("Gender of your hangman [him/her/them/hir]: ")
    hanged = input("Oh no! " + hangman + " will be hanged! ")
    initialize = input("Guess the word to release " + gender + """ [Press ENTER to start game] """)
    print("")
    print("______________________________________________________________________________________________________________________________________________")

    # Randomly selecting word
    random_index4 = random.randint(0, len(edition_to_play) - 1)
    word = edition_to_play[random_index4]
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
    print("Word: " + temporary_string)
    print(hangman_arts[len(hangman_arts) - lives - 1])
    print(hangman + ": " + dialogue)
    print("")

    new_temporary_string = ""
    guess_word = ""
    letters_used = "Letters already used: "

    while temporary_string != word and lives > 0 and guess_word != word:
        random_index2 = random.randint(0, len(negative_dialogues) - 1)
        negative_dialogue = negative_dialogues[random_index2]

        random_index3 = random.randint(0, len(positive_dialogues) - 1)
        positive_dialogue = positive_dialogues[random_index3]

        guess = input("Guess letter: ")
        guess_word = input("Guess word (press ENTER if you don't have any guess): ")
        print("")
        letters_used += guess + ", "
        print("______________________________________________________________________________________________________________________________________________")
        print(letters_used)

        compare_string = temporary_string
        lives_string = "Lives: {}".format(lives)

        if guess in word and not guess == "" and guess_word != word:
            for i in range(len(word)):
                if word[i] == guess:
                    new_temporary_string = compare_string[:i] + guess + compare_string[i+1:]

                if new_temporary_string == "":
                    new_temporary_string = compare_string
                compare_string = new_temporary_string

            print("Word: " + compare_string)
            print("Nice work! " + lives_string)
            print(hangman_arts[len(hangman_arts) - lives - 1])
            print(hangman + ": " + positive_dialogue)
            print("")

        elif not guess in word or (guess == "" and guess_word != word):
            if new_temporary_string == "":
                print("Word: " + temporary_string)
            else:
                print("Word: " + new_temporary_string)

            lives = lives - 1
            lives_string = "Lives: {}".format(lives)

            print("Oh no! The letter is not in the word. " + lives_string)
            print(hangman_arts[len(hangman_arts) - lives - 1])
            if lives > 0:
                print(hangman + ": " + negative_dialogue)
            else:
                print(hangman + ": Noooooooo-")
            print("")

        if new_temporary_string != "":
            temporary_string = new_temporary_string

    if temporary_string == word or guess_word == word:
        print(""" __     __                    _       _ 
 \ \   / /                   (_)     | |
  \ \_/ /__  _   _  __      ___ _ __ | |
   \   / _ \| | | | \ \ /\ / / | '_ \| |
    | | (_) | |_| |  \ V  V /| | | | |_|
    |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
    """)
        print("The word is " + word + ".")
        print(hangman + ": Thank you!")
        print("")
    else:
        print(""" __     __           _                  _ 
 \ \   / /          | |                | |
  \ \_/ /__  _   _  | | ___  ___  ___  | |
   \   / _ \| | | | | |/ _ \/ __|/ _ \ | |
    | | (_) | |_| | | | (_) \__ \  __/ |_|
    |_|\___/ \__,_| |_|\___/|___/\___| (_)
                                          
    """)
        print("The word is " + word + ".")
        print("")

# Play game
play = True
game_status = True

while game_status:
    main_menu()
    print("______________________________________________________________________________________________________________________________________________")
    ask_for_game_rule()
    print("______________________________________________________________________________________________________________________________________________")
    while play:  
        edition_to_play = select_edition()
        print("______________________________________________________________________________________________________________________________________________")
        play_game()
        print("______________________________________________________________________________________________________________________________________________")
        again = input("Play again? (y/n): ")
        print("______________________________________________________________________________________________________________________________________________")
        if again == "n":
            play = False
    return_to_menu = input("Return to main menu? (y/n): ")
    print("______________________________________________________________________________________________________________________________________________")
    if return_to_menu == "n":
        game_status = False
    else:
        play = True
        game_status = True
