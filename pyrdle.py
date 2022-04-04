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
    if guesses >= 1:
        print ("\n", guesses, "tries left...")
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
        characters_in_chosen_word = []
        
        for letter in prompt:
            if letter in chosen_word:
                if letter in characters_in_chosen_word:
                    pass
                else:
                    characters_in_chosen_word.append(letter)
        if len(characters_in_chosen_word) != 0:
            for char in characters_in_chosen_word:
                print ("The letter", char, "is in the word!")
        else:
            print("None of the letters are in the word.")
                

# Start the loop and only break when we're at negative guesses
while guesses < 7 and guesses >= -1:
    main_loop()