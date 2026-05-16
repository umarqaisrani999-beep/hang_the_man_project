# Problem Set 1, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret1=list(secret_word)
    count=0
    if secret1==letters_guessed:
        return False
    else:
        return True



def get_guessed_word(secret_word, letters_guessed):
    length=len(secret_word)
    i=[]
    j=0
    while j<length:
        i.append("_")
        j=j+1
    for x in i:
        print(x,end=" ")
    print("\n")



def get_available_letters(letters_guessed):
    a=string.ascii_lowercase
    b=list(a)
    for x in b:
        for y in letters_guessed:
            if y==x:
                b.remove(y)
    print("You have Following characters to enter from,")
    for x in b:
        print(x, end=" ")
    
    

def hangman(secret_word):
    print("\n\tWelcome to the game 'HANGMAN'.\t\n")
    print(secret_word)
    print("\nThe word has been guessed!")
    length=len(secret_word)
    print("\nHINT:The word is ",length," characters long!\n")
    
    warnings=3
    guess=6
    print("\nYou have ",warnings," warnings and ",guess," guesses!\nBe carefull!")

    n=True
    lettersguessed=[]
    while n==True:
      user=input("\nEnter the character :")
      while len(user)!=1:
          print("\n!!!Input too long.\nPlease enter a single character!!!")
          user=input("Enter :")
      matchalpha=0
      matchnum=0
      matchpun=0
      
      for x in lettersguessed:
          if user==x:
              print("!!!Same character used again!!!\n warning dedcuted!")
              warnings=warnings-1
              print("Total Warnings :",warnings)
              matchalpha=1
      
      digits=string.digits
      num=list(digits)
      punt=string.punctuation
      pun=list(punt)

      for x in pun:
          if user==x:
              print("!!!Symbol entered!!!\nWarning Deducted!")
              warnings=warnings-1
              print("Warnings:",warnings)
              matchpun=1
              
      for x in digits:
          if user==x:
              print("!!!Number entered!!!\nWarning Deducted!")
              warnings=warnings-1
              print("Warnings:",warnings)
              matchnum=1

      if warnings==0:
          print("\nWarnings lost. \tYou LOST!\t")
          break
    
      if matchalpha==1:
          continue
      if matchnum==1:
          continue
      if matchpun==1:
          continue
      print("Character Entered :",user)
      lettersguessed.append(user)
      print(lettersguessed)

      index=[]
      secret1=list(secret_word)
      for x,y in enumerate(secret1):
          if y==user:
              index.append(x)
      print(index)
      
      if index==[]:
          print("Wrong Guess!.\nGuess Deducted.")
          guess=guess-1
          print("\nGuess:",guess)
      
      if guess==0:
          print("Guesses lost. \tYou LOST!\t")
          break

      get_available_letters(lettersguessed)
      n=is_word_guessed(secret_word,lettersguessed)
      


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

