import random

class Hangman:
    """
    The Hangman class represents the game of Hangman.

    Attributes:
    - word_list: A list of words to choose from.
    - num_lives: The number of lives the player starts with (default is 5).
    - word: The randomly selected word for the current game.
    - word_guessed: A list representing the current state of the guessed word.
    - num_letters: The number of unique letters in the selected word.
    - list_of_guesses: A list to store the letters guessed by the player.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialises a new instance of the Hangman class.

        Parameters:
        - word_list: A list of words to choose from.
        - num_lives: The initial number of lives for the player (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.pick_new_word()

    def pick_new_word(self):
        """
        Picks a new word for the game and initialises game-related attributes.
        """ 
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def display_word_guessed(self):
        """
        Displays the current state of the guessed word.
        """
        print("Word guessed so far:", ' '.join(self.word_guessed))

    def update_word_guessed(self, guess):
        """
        Updates the word_guessed attribute based on the correct guesses.
        
        Parameters:
        - guess: The letter guessed by the player.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess

        self.num_letters -= 1

    def handle_correct_guess(self, guess):
        """
        Handles the case when the player makes a correct guess.

        Parameters:
        - guess: The correct letter guessed by the player.
        """
        print(f'Good guess! {guess} is in the word.')
        self.update_word_guessed(guess)

    def handle_incorrect_guess(self, guess):
        """
        Handles the case when the player makes an incorrect guess.

        Parameters:
        - guess: The incorrect letter guessed by the player.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        """
        Checks whether the player's guess is correct and updates the game state accordingly.

        Parameters:
        - guess: The letter guessed by the player.
        """
        guess = guess.lower()

        if guess in self.word:
            self.handle_correct_guess(guess)
        else:
            self.handle_incorrect_guess(guess)

    def ask_for_input(self):
        """
        Asks the player for input until a valid guess is received.
        """
        while True:
            guess = input('Guess a letter: ')

            # Check that the guess is a single alphabetical character
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                self.display_word_guessed()
                break
