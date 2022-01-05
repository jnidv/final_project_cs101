# Libraries
import random
import time
from extras import line
from extras import title_screen
from extras import game_rules
from extras import list_of_editions
from extras import you_lose
from extras import you_win
from extras import hangman_arts

# Functions
def main_menu():
    # Main Menu
    print(line)
    print(title_screen)
    print(line)
    time.sleep(2)
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
        id_of_edition_to_play = input("What edition do you want to play? [1 - NBA Players; 2 - Filipino Foods; 3 - Philippine Landmarks]: ")
        print()

        list_of_number_str = []
        for i in range(len(list_of_editions)):
            list_of_number_str.append(str(i+1))

        if id_of_edition_to_play in list_of_number_str:
            edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][0]
            name_of_edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][1]
            incorrect = False
            return edition_to_play, name_of_edition_to_play
            
def play_game():
    # Dialogues
    dialogues_start = ["Please help me!", "You can do it!", "Focus!", "I love you! So please save me."]

    random_index1 = random.randint(0, len(dialogues_start) - 1)
    dialogue = dialogues_start[random_index1]

    negative_dialogues = ["Better guess that word!", "If anything happens, just know that I love you.", "I know you can do better than that!", 
    "Oh c'mon!"]
    
    positive_dialogues = ["Good job!", "Keep it up!", "Whooo!", "GRAPE!"]

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

    print("Let's start the game! " + lives_string)
    print("Edition: " + name_of_edition_to_play)
    print("Word: " + temporary_string)
    print(hangman_arts[len(hangman_arts) - lives - 1])
    print(hangman + ": " + dialogue)
    print()

    guess_word = ""
    letters_used = "Letters already used: "

    # Loop until we win
    while temporary_string != word and lives > 0 and guess_word != word:
        random_index2 = random.randint(0, len(negative_dialogues) - 1)
        negative_dialogue = negative_dialogues[random_index2]

        random_index3 = random.randint(0, len(positive_dialogues) - 1)
        positive_dialogue = positive_dialogues[random_index3]

        guess = input("Guess letter: ")
        guess_word = input("Guess word (press ENTER if you don't have any guess): ")
        print()

        letters_used += guess + " "
        print(line)
        print(letters_used)

        new_temporary_string = temporary_string
        lives_string = "Lives: {}".format(lives)

        if (guess in word and not guess == "" and not guess == " ") and guess_word != word:
            for i in range(len(word)):
                if word[i] == guess:
                    temporary_string = new_temporary_string[:i] + guess + new_temporary_string[i+1:]
                    
                new_temporary_string = temporary_string

            print("Nice work! " + lives_string)
            print("Edition: " + name_of_edition_to_play)
            print("Word: " + new_temporary_string)
            print(hangman_arts[len(hangman_arts) - lives - 1])
            print(hangman + ": " + positive_dialogue)
            print() 

        elif guess_word != word:
            lives = lives - 1
            lives_string = "Lives: {}".format(lives)
            print("Oh no! The letter is not in the word. " + lives_string)

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

while game_status:
    main_menu()
    print(line)

    ask_for_game_rule()
    print(line)

    while play:  
        edition_to_play, name_of_edition_to_play = select_edition()
        print(line)

        play_game()
        print(line)

        again = input("Play again? (y/n): ")
        print()
        print(line)

        if again == "n":
            play = False

    return_to_menu = input("Return to main menu? (y/n): ")
    print()
    print(line)

    if return_to_menu == "n":
        game_status = False
    else:
        play = True
        game_status = True