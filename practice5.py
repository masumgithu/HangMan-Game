#HangMan Game
from Tools.scripts.pep384_macrocheck import ifdef_level_gen

word = "Masum"
chances = 5
GuessAdd = []
Done = False

while not Done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end = " ")
        else:
            print(" ", end = "")

    UserGuess = input(f"Your Changes Is {chances}, Guess The Letter: ")
    GuessAdd.append(UserGuess.lower())
    if UserGuess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = False

if done:
     print(f"yes, you won the game, the word is {word}")
else:
     print("you lose the game")