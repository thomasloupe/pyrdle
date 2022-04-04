import random

# Set the default word string to nothing.
chosen_word = ""
# Set the amount of guesses the player has
guesses = 6


# Choose the word from the text file provided.
chosen_word = random.choice(open("words_alpha.txt").readlines())

def main_loop():
    # Access the global variable.
    global guesses
    # Take away one guess.
    guesses -= 1
    # Check if we ran out of guesses first and act accordingly.
    if guesses >= 0:
        print ("\nGuess the five letter word! You have", guesses, "guesses left...")
        # Read the user's input
        prompt = input()
        # Set up a variable so we can see how many letters matched, if any.
        matched_letters = 0
        if prompt == chosen_word:
            print("YOU WIN!!!")
        else:
            # Enter a for loop that checks each letter the user chose against each letter in the chosen 
            # random word and see if there's any matches in letters
            for letter in chosen_word:
                for each_letter in prompt:
                    if each_letter == letter:
                        print ("The letter " + letter + " is in the word!")
                        matched_letters += 1
                        if matched_letters == 0:
                            print ("No matched letters found in your choice...")
    # End the game when we run out of guesses.
    elif guesses < 0:
        print ("You lose, the word was", chosen_word + ".")

# Start the loop and only break when we're at negative guesses
while guesses < 7 and guesses > -1:
    main_loop()