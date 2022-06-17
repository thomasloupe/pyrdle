import random
import enchant

# Set dictionary for word checking.
d = enchant.Dict("en_US")
# Set the default word string to nothing.
chosen_word = ""
# Set the amount of guesses the player has
guesses = 6


# Choose the word from the text file provided.
chosen_word = random.choice(open("words_alpha.txt").readlines())

def main_loop():
    # Access the global variable.
    global guesses
    # Check if we ran out of guesses first and act accordingly.
    if guesses == 6:
        print ("\nGuess the five letter word. You have six attempts to guess it correctly. Good luck!")
    elif guesses >= 1 and guesses < 6:
        print("\n")
        print (guesses, "tries left...")
    elif guesses == 0:
        print ("\nThis is your last chance. Good luck!")
        # End the game when we run out of guesses.
    elif guesses < 0:
        print ("\nThe word was", chosen_word + ".")
        quit()
    # Read the user's input
    prompt = input().strip().casefold()
    # If the length of the word isn't 5 characters, return. This also fixes the "pick every character cheat"
    if len(prompt) != 5:
        print("That word isn't 5 letters!")
        return
        # If the word isn't actually in the English dictionary, don't count this as a guess.
    if d.check(prompt) != True:
        print ("Not a valid word.")
        return
    # Set up a variable so we can see how many letters matched, if any.
    if prompt.casefold().strip() == chosen_word.casefold().strip():
        print("YOU WIN!!!")
        quit()
    else:
        # Enter a for loop that checks each letter the user chose against each letter in the chosen 
        # random word and see if there's any matches in letters.
        # Take away one guess.
        guesses -= 1
        # Create empty list to store letters in.
        characters_in_chosen_word = []
        # Check if any letter exists in the chosen word and if so, add it to the list once.
        for letter in prompt:
            if letter in chosen_word:
                if letter in characters_in_chosen_word:
                    pass
                else:
                    characters_in_chosen_word.append(letter)
        # Let the player know about a letter that exists in the chosen word.
        if len(characters_in_chosen_word) != 0:
            print ("\n")
            for char in characters_in_chosen_word:
                print ("The letter", char, "is in the word!")
        # Let the player know if no letters in their word were found in the chosen word.
        else:
            print ("\n")
            print("None of the letters are in the word.")
                

# Start the loop and only break when we're at negative guesses.
while guesses < 7 and guesses >= -1:
    main_loop()