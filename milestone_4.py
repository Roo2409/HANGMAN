import random
class Hangman:
 def __init__(self,word_list,num_lives = 5):
    self.num_lives = num_lives
    self.word = random.choice(word_list)
    self.word_guessed = ["_"]*len(self.word)
    
 
    # if guess in word:
    #   print(guess,)

    # word_guessed = "_"
    # while True:
    #  guess = input("enter a letter")
    #  word_guessed += guess
    #  if guess == word:
    #   print( guess)
    #  break
 

word_list = ['banana','mango','apple','berry','orange'] 
word_guessed = ['_']
Task1 = Hangman(word_list)
print(Task1.word)
print(Task1.word_guessed)
