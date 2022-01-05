# Libraries
import random
import time

# Variables from extras.py
from extras import line
from extras import title_screen
from extras import game_rules
from extras import you_win
from extras import you_lose
from extras import hangman_arts
from extras import list_of_editions
from extras import dialogues_start
from extras import positive_dialogues
from extras import negative_dialogues

# Functions
def main_menu():
    # Main Menu
    print(line)
    print(title_screen)
    print(line)
    time.sleep(1)
    play = input("Press ENTER to play!: ")
    print()

def ask_for_game_rule():
    # Game Rules
    yes_no_game_rules = input("Do you want to read the game rules? (y/n): ")
    print()

    if yes_no_game_rules == "y":
        print(game_rules)

def select_edition():
    # Editions and selecting editions
    incorrect = True
    while incorrect:
        id_of_edition_to_play = input("What edition do you want to play? {}: ".format([str(i+1) + " - " + list_of_editions[i][1] for i in range(len(list_of_editions))]))

        list_of_number_str = []
        for i in range(len(list_of_editions)):
            list_of_number_str.append(str(i+1))

        if id_of_edition_to_play in list_of_number_str:
            edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][0]
            name_of_edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][1]
            incorrect = False
            return edition_to_play, name_of_edition_to_play
        else:
            print("You have to enter a number from {first} to {second}.".format(first=1, second=len(list_of_editions)))
        
        print()
            
def play_game():
    # Dialogues
    random_index1 = random.randint(0, len(dialogues_start) - 1)
    dialogue = dialogues_start[random_index1]

    # Story
    hangman = input("Name your hangman: ")
    gender = input("Gender of your hangman [him/her/them/hir]: ")
    print()
    time.sleep(1)
    print("Oh no! " + hangman + " will be hanged!")
    time.sleep(1)
    print("Guess the word to release " + gender + ".")
    time.sleep(1)
    print()
    print(line)

    # Randomly selecting word
    random_index4 = random.randint(0, len(edition_to_play) - 1)
    word = edition_to_play[random_index4]
    
    temporary_string = ""
    for letter in word:
        if letter != " ":
            temporary_string += "-"
        else:
            temporary_string += letter

    # Solo game main algorithm
    lives = len(hangman_arts) - 1
    lives_string = "Lives: {}".format(lives)

    print("Let's start the game!")
    time.sleep(1) 
    print(lives_string)
    print("Edition: " + name_of_edition_to_play)
    print("Word: " + temporary_string)
    print(hangman_arts[len(hangman_arts) - lives - 1])
    print(hangman + ": " + dialogue)
    print()

    guess_word = ""
    letters_used = ""

    # Loop until we win or lose
    while temporary_string != word and lives > 0 and guess_word != word:
        random_index2 = random.randint(0, len(negative_dialogues) - 1)
        negative_dialogue = negative_dialogues[random_index2]

        random_index3 = random.randint(0, len(positive_dialogues) - 1)
        positive_dialogue = positive_dialogues[random_index3]

        guess_raw = input("Guess letter: ")
        guess = guess_raw.strip().lower()

        while not guess in "abcdefghijklmnopqrstuvwxyz":
            print("Guess is not a letter!")
            print()
            time.sleep(1)
            guess_raw = input("Guess letter: ")
            guess = guess_raw.strip().lower()

        while guess in letters_used and guess != "":
            print("Letter is already used.")
            print()
            time.sleep(1)
            guess_raw = input("Guess letter: ")
            guess = guess_raw.strip().lower()

        guess_word_raw = input("Guess word (press ENTER if you don't have any guess): ")
        guess_word = guess_word_raw.strip().lower()
        print()

        letters_used += guess + " "
        print(line)
        print("Letter used: " + letters_used)

        new_temporary_string = temporary_string
        lives_string = "Lives: {}".format(lives)

        if (guess in word and guess != "") and guess_word != word:
            for i in range(len(word)):
                if word[i] == guess:
                    temporary_string = new_temporary_string[:i] + word[i] + new_temporary_string[i+1:]
                    
                new_temporary_string = temporary_string

            if temporary_string != word:
                print("Nice work!")
                print(lives_string)
                print("Edition: " + name_of_edition_to_play)
                print("Word: " + new_temporary_string)
                print(hangman_arts[len(hangman_arts) - lives - 1])
                print(hangman + ": " + positive_dialogue)
                print() 

        elif guess_word != word:
            lives = lives - 1
            lives_string = "Lives: {}".format(lives)
            print("The letter is not in the word.")
            print(lives_string)

            print("Edition: " + name_of_edition_to_play)
            print("Word: " + new_temporary_string)

            print(hangman_arts[len(hangman_arts) - lives - 1])
            
            if lives > 0:
                print(hangman + ": " + negative_dialogue)
            else:
                print(hangman + ": Noooooooo-")
            print()

        temporary_string = new_temporary_string

    if temporary_string == word or guess_word == word:
        print(you_win)
        print("The word is " + word + ".")
        print(hangman + ": Thank you!")
        print()
    else:
        print(you_lose)
        print("The word is " + word + ".")
        print()

# Play game
play = True
game_status = True

# While loop for the status of the game
while game_status:
    main_menu()
    print(line)

    ask_for_game_rule()
    print(line)

    # Gameplay
    while play:  
        edition_to_play, name_of_edition_to_play = select_edition()
        print(line)

        play_game()
        print(line)

        # Option to terminate gameplay
        again = input("Play again? (y/n): ")
        print()
        print(line)

        if again == "n":
            play = False

    # Option to terminate the status of the game
    return_to_menu = input("Return to main menu? (y/n): ")
    if return_to_menu == "n":
        game_status = False
    else:
        play = True
        game_status = True

    print()
    print(line)