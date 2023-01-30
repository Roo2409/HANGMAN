import random
class Hangman:
 def __init__(self,word_list,num_lives = 5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(self.word_list)
    self.word_guessed = ["_"]*len(self.word)
    self.num_letters = len(set(self.word))
    self.list_of_guesses = list_of_guesses
    
 
 


word_list = ['banana','mango','apple','berry','orange'] 
word_guessed = ['_']
list_of_guesses = []
Task1 = Hangman(word_list)
print(Task1.word)
print(Task1.word_guessed)
#print(Task1.word_list)
print(Task1.num_letters)
print(Task1.list_of_guesses)
