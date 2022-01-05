line = "-----------------------------------------------------------------------------------------------------------------------------------------------"

title_screen = """ __    __       ___      .__   __.   ______  .___  ___.      ___      .__   __.   +---+ 
|  |  |  |     /   \     |  \ |  |  /  ____| |   \/   |     /   \     |  \ |  |   |   | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |   O   | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |  /|\  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |  / \  | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| =========

WELCOME TO TEXT-BASED SINGLEPLAYER HANGMAN CODED IN PYTHON
Creator: Jan Neal Isaac D. Villamin
"""

game_rules = """GAME PLAY
The program will ask you to select an EDITION, themed sets of words. 
The executer will ask you a RANDOM WORD from that EDITION.

A number of DASHES equivalent to the number of letters in the word will be displayed. 
If a guessing player suggests a LETTER that occurs in the word, the program fills in the blanks with that letter in the right places. 

If the word does not contain the suggested letter, the program draws one element of a hangmans gallows. 
As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word. 

The number of incorrect guesses before the game ends is up to the difficulty of the game, 
but completing a character in a noose provides a minimum of SEVEN wrong answers until the game ends. 

RESTRICTIONS
Follow the input formats given as much as possible. Only lowercase letters are allowed. 
Otherwise, bugs might go flyin' in your screen.

OBJECTIVE
Guess the word or phrase before your hangman gets hanged!
"""

you_win = """ __     __                    _       _ 
 \ \   / /                   (_)     | |
  \ \_/ /__  _   _  __      ___ _ __ | |
   \   / _ \| | | | \ \ /\ / / | '_ \| |
    | | (_) | |_| |  \ V  V /| | | | |_|
    |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
    """

you_lose = """ __     __           _                  _ 
 \ \   / /          | |                | |
  \ \_/ /__  _   _  | | ___  ___  ___  | |
   \   / _ \| | | | | |/ _ \/ __|/ _ \ | |
    | | (_) | |_| | | | (_) \__ \  __/ |_|
    |_|\___/ \__,_| |_|\___/|___/\___| (_)
                                          
    """
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

displays = [line, title_screen, game_rules, you_win, you_lose, hangman_arts]

nba_players = ["lebron james", "stephen curry", "kevin durant", "giannis antetokounmpo", "james harden", "anthony davis", 
    "damian lillard", "chris paul", "luka doncic", "russell westbrook", "joel embiid", "kawhi leonard", "kyrie irving", 
    "karl anthony towns", "demar derozan", "carmelo anthony", "klay thompson", "paul george", "jimmy butler", "draymond green", 
    "kyle lowry", "kobe bryant", "michael jordan", "jayson tatum", "bradley beal", "devin booker", "donovan mitchell", 
    "trae young", "zion williamson", "ja morant", "ben simmons", "zach lavine", "jamal murray"]

filipino_foods = ["adobo", "sinigang", "nilaga", "tinola", "bulalo", "menudo", "afritada", "kwek kwek", "balut", "taho", 
    "lechon", "sisig", "crispy pata", "chicken inasal", "pancit palabok", "arroz caldo", "kare kare", "tapa", "dinuguan", "puto", 
    "pinakbet", "laing", "pancit habhab", "longaniza", "lumpia", "bicol express", "liempo", "halo halo", "champorado", "turon"]

philippines_landmarks = ["chocolate hills", "banaue rice terraces", "mayon volcano", "taal volcano", "fort santiago", 
    "rizal monument", "tarsiers", "boracay", "tubbataha reefs", "puerto princesa subterranean river", "maria cristina falls"]

list_of_editions = [[nba_players, "NBA Players"], [filipino_foods, "Filipino Foods"], [philippines_landmarks, "Philippine Landmarks"]]

dialogues_start = ["Please help me!", "You can do it!", "Focus!", "I love you! So, please save me."]

positive_dialogues = ["Good job!", "Keep it up!", "Whooo!", "GRAPE!"]

negative_dialogues = ["Better guess that word!", "If anything happens, at least know that I love you.", "I know you can do better than that!", 
    "Oh c'mon!"]

all_dialogues = [dialogues_start, positive_dialogues, negative_dialogues]

all_variables = [displays, list_of_editions, all_dialogues]