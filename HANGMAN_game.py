import random

word_list = ("computer", "dog", "batman", "apple", "tree", "cat")

chosen_word = random.choice(word_list)

def print_with_spaces(mylst):
    for i in mylst:
        print(i, " ", end="")

    print(" ")
        
#test code
#print("Cheat: the word is ", chosen_word)

lives = 6
end_of_game = False

print("\nWelcome to the game of hangman")
print("You have, lives", lives, "to guess the correct word")

word_length = len(chosen_word)

#create blanks
display = []
for i in range(word_length):
    display += "_"

print_with_spaces(display)

while not end_of_game:

    guess = input("\nGuess a letter: ")

    correct_guess = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            correct_guess = True
            display[position]= letter

    if not correct_guess:
        print("You guessed", guess, "but that's not in the word. You lose a life.")
        lives -= 1
        print("You have", lives, "left.")

        if lives == 0:
            end_of_game = True
            print("\nYou lose")
            print("The correct word was", chosen_word)

    if "_" not in display:
        end_of_game = True
        print("You win.")
        

    print_with_spaces(display)
        

        

