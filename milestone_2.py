import random 

# list of fruits
word_list = ['pomergranate', 'mango', 'banana', 'apple', 'strawberries']
print(word_list)

# Create a random word from list
def choose_random_word(word_list):
  print(word)
  
favorite_fruits = ['pomegranate', 'mango', 'banana', 'apple', 'strawberries']
word_list = favorite_fruits
word = random.choice(word_list)
print("Word List:", word_list)
print("Randomly chosen word:", word)

#task 3
def get_player_guess():
    """Ask the user to input a single letter."""
    return input('Please enter a single letter: ')

#ask user to input letter
guess = input('Enter a single letter: ')

#Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')



