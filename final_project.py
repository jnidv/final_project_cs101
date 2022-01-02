import random
# Let us test our algorithm for Hangman
nba = ["lebron james", "stephen curry", "kevin durant", "giannis antetokounmpo", "james harden", "anthony davis"]
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
tries = 3
guess_word = ""
while temporary_string != word and tries > 0 and guess_word != word:
    guess = input("Guess letter: ")
    guess_word = input("Guess word (press ENTER or type any KEY if you don't have any guess): ")
    compare_string = temporary_string
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                new_temporary_string = compare_string[:i] + guess + compare_string[i+1:]
            compare_string = new_temporary_string
        if temporary_string == new_temporary_string:
            print("Oh no!")
        elif temporary_string != new_temporary_string:
            print(new_temporary_string)
            print("Nice work!")
    else:
        if new_temporary_string == "":
            print(temporary_string)
        else:
            print(new_temporary_string)
        print("Oh no!")
        tries = tries - 1         
    temporary_string == new_temporary_string
if temporary_string == word or guess_word == word:
    print("You win!")
else:
    print("You lose!")