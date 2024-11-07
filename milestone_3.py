import random

def check_guess(guess, random_word):
    """
    Checks if the guessed letter is present in the randomly selected word.

    Parameters:
    - guess (str): The player's guess, which is converted to lowercase.
    - random_word (str): The randomly selected word.

    Returns:
    - bool: True if the guess is correct, False otherwise.
    """
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in random_word:
        print(f'Good guess! {guess} is in the word.')
        return True
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        return False

def ask_for_input(random_word):
    """
    Ask the user to guess a letter.
    Returns: 
    - None: Breaks out of the loop if a valid single alphabetical character is entered.
      Otherwise, prints an error message and continues the loop.
    """
    while True:
        # Step 2: Move the code for asking the user to guess a letter
        guess = input('Guess a letter: ')

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 3: Call the check_guess function to check if the guess is in the word
            if check_guess(guess, random_word):
                break
        else:
            # If the guess does not pass the checks, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Generate a random word
word_list = ['pomergranate', 'dates', 'mango', 'blueberries', 'strawberries']
random_word = random.choice(word_list)

# Step 5: Call the ask_for_input function with the random word to test the code
ask_for_input(random_word)
