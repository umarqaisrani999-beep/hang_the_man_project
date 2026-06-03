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


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret1=list(secret_word)
    unique=list(dict.fromkeys(secret1))
    
    count=0
    for x in letters_guessed:
        for y in unique:
            if y==x:
                count+=1
    
    length=len(unique)

    if length==count:
        return False
    else:
        return True

    



def get_guessed_word(secret_word, letters_guessed):
    index=[]
    letters=[]
    secret1=list(secret_word)
    for x in letters_guessed:
        for y,z in enumerate(secret1):
            if z==x:
                index.append(y)
                letters.append(z)
    print("")
    for x,y in enumerate(secret1):
        run=False
        for e,z in enumerate(index):
            if x==z:
                print(letters[e],end=" ")
                run=True
        if run==True:
            pass
        else:
            print("_",end=" ")
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
    print("\nThe word has been choosen!")
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
          print("\nWarnings lost. \n\tYou LOST!\t\n")
          break
    
      if matchalpha==1:
          continue
      if matchnum==1:
          continue
      if matchpun==1:
          continue
      print("Character Entered :",user)
      

      index=[]
      secret1=list(secret_word)
      for x,y in enumerate(secret1):
          if y==user:
              index.append(x)
      
      if index==[]:
          print("Wrong Guess!.\nGuess Deducted.")
          guess=guess-1
          print("\nGuess:",guess)
      else:
          lettersguessed.append(user)
          print(lettersguessed)
          get_guessed_word(secret_word,lettersguessed)
    
      if guess==0:
          print("Guesses lost. \n\tYou LOST!\t\n")
          break
      
      get_available_letters(lettersguessed)
      n=is_word_guessed(secret_word,lettersguessed)
    
    if n==False:
        print("\n\tCongratulations! You WON!\t\n")
      





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

