import random
import string

WORDLIST_FILENAME = "wordlist.txt"

def loadWords():
  print("Loading word list from file...")
  with open(WORDLIST_FILENAME) as f:
    wordlist = f.read().splitlines()
  print(f"  {len(wordlist)} words loaded.")
  return wordlist


def isWordGuessed(secretWord, lettersGuessed):
  count = 0
  for i, c in enumerate(secretWord):
    if c in lettersGuessed:
      count += 1
  return count == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
  count = 0
  blank = ['_ '] * len(secretWord)

  for i, c in enumerate(secretWord):
    if c in lettersGuessed:
      count += 1
      blank.insert(count-1,c)
      blank.pop(count)
      if count == len(secretWord):
        return ''.join(str(e) for e in blank)
    else:
      count += 1
      blank.insert(count-1,'_')
      blank.pop(count)
      if count == len(secretWord):
        return ''.join(str(e) for e in blank)
        
def getAvailableLetters(lettersGuessed):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  alphabet2 = alphabet[:]

  def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e in L1:
      if e in L1Start:
        L2.remove(e)
    return ''.join(str(e) for e in L2)

  return removeDupsBetter(lettersGuessed, alphabet2)


def hangman(secretWord):
  lettersGuessed = []
  guess = str
  mistakesMade = 8
  wordGuessed = False
  
  print("Welcome to the game, Hangman!")
  print(f"I am thinking of a word that is {len(secretWord)} letters long.")
  print("------------")

  while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
    if secretWord == getGuessedWord(secretWord, lettersGuessed):
      wordGuessed = True
      break
    print(f"You have {mistakesMade} guesses left.")
    print(f"Available letters: {getAvailableLetters(lettersGuessed)}") 
    guess = input('Please guess a letter: ').lower()
    if guess in secretWord:
      if guess in lettersGuessed:
        print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        print("------------")
      else:
        lettersGuessed.append(guess)
        print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
        print("------------")
    else:
      if guess in lettersGuessed:
        print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}") 
        print("------------")
      else:
        lettersGuessed.append(guess)
        mistakesMade -= 1
        print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
        print("------------")

  if wordGuessed == True:
    return("Congratulations, you won!")
  elif mistakesMade == 0:
    return(f"Sorry, you ran out of guesses. The word was {secretWord}") 

secretWord = random.choice(loadWords())
print(hangman(secretWord))

