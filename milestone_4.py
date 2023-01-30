import random
class Hangman:
 def __init__(self,word_list,num_lives = 5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(self.word_list)
    self.word_guessed = ["_"]*len(self.word)
    
 
 

word_list = ['banana','mango','apple','berry','orange'] 
word_guessed = ['_']
Task1 = Hangman(word_list)
print(Task1.word)
print(Task1.word_guessed)
