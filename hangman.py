import random
from words import words
from hangmanVisual import hangman_visual_dict
import string

#a function to choose right word as it has many words including '-' & space
def get_valid_word(words):
    word = random.choice(words)     #chooses randomly from the list
    #this loop will run till we get the word not containing, '-' or space
    while '-' in word or ' ' in word:
        word=random.choice(words)
    
    return word.upper()         #to get upper casse of the word (can take, lower too)

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)      #set of letters in the word to keep track of the letters in word
    alphabet=set(string.ascii_uppercase)            #uppercase leeters' in ascii as set of alphabet
    used_letters=set()       #to keep track of what what the user has guessed

    #life count of the guy
    lives=9
    
    #this must happen until user guesses the right word, so we gotta loop it
    while len(word_letters)>0 and lives>0:

        #we need to show the user what they've used so---
        #' '.join['a', 'b', 'cd'] ---> 'a b cd'
        print(f"\n\tYou have {lives} lifes and you have used ", ' '.join(used_letters), "letters till now.")

        #and printing '-' for not guessd one with right guesses
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print(hangman_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_input=input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                lives=lives-1
                print("\n\tWrong guess babe.")

        elif user_input in used_letters:
            print("\n\tYou've already used it. Please try another.")

        else:
            print("\n\tInvalid input.")
    
    if lives==0:
        print(hangman_visual_dict[lives])
        print(f"\n\tSorry! The word was {word}. You are hanged till death.\n")
    else:
        print('\n\tYay! You guessed the word: ', word)
        print("\n")

hangman()