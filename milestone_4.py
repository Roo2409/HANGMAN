import random
class Hangman:
 def __init__(self,word_list,num_of_lives = 5):
    self.num_of_lives = int(5)
    print (num_of_lives)
    self.word = random.choice(word_list)
    word = self.word
    print(word)
    self.word_guessed = word_guessed
    guess = input("enter the letter")
    if guess in word:
      print(guess,)

    # word_guessed = "_"
    # while True:
    #  guess = input("enter a letter")
    #  word_guessed += guess
    #  if guess == word:
    #   print( guess)
    #  break
 

word_list = ['banana','mango','apple','berry','orange'] 
word_guessed = ['_', '_', '_', '_', '_']
Task1 = hangman(word_list)
print(Task1)
