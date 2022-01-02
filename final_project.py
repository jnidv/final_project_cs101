import random
# Let us test our algorithm for Hangman
nba = ["lebron james", "stephen curry", "kevin durant", "giannis antetokounmpo", "james harden", "anthony davis", "damian lillard"]
random_index = random.randint(0, len(nba) - 1)
word = nba[random_index]
temporary_string = ""
for letter in word:
    if letter != " ":
        temporary_string += "-"
    else:
        temporary_string += letter
print(temporary_string)
new_temporary_string = ""
lives = 3
guess_word = ""
while temporary_string != word and lives > 0 and guess_word != word:
    guess = input("Guess letter: ")
    guess_word = input("Guess word (press ENTER or type any KEY if you don't have any guess): ")
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
        if temporary_string == new_temporary_string:
            print("Oh no! " + lives_string)
        elif temporary_string != new_temporary_string:
            print(compare_string)
            print("Nice work! " + lives_string)
    else:
        if new_temporary_string == "":
            print(temporary_string)
        else:
            print(new_temporary_string)
        lives = lives - 1
        lives_string = "Lives: {}".format(lives)
        print("Oh no! " + lives_string)         
    temporary_string = new_temporary_string
if temporary_string == word or guess_word == word:
    print("You win!")
else:
    print("You lose!")