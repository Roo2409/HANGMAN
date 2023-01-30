import random
class Hangman:
 def __init__(self,word_list,num_lives = 5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(self.word_list)
    self.word_guessed = ["_"]*len(self.word)
    self.num_letters = len(set(self.word))
    self.list_of_guesses = [ ]

 def check_guess(self,guess):
   self.guess = guess
   guess = guess.lower()
   if guess in self.word:
     print("Good guess! {guess} is in the word.")
 def ask_for_input():
   while True:
     guess = input("enter a letter")
     for letter in guess:
       if len(guess)!= 1 and not guess.isalpha():
         print("Invalid letter. Please, enter a single alphabetical character.")
       elif guess in list_of_guesses:
         print("You already tried that letter!")
     if len(guess)==1 not in list_of_guesses:
       print(" ")
     else:
        Hangman.check_guess(guess)
   

word_list = ['banana','mango','apple','berry','orange'] 
word_guessed = ['_']
list_of_guesses = []
Task1 = Hangman(word_list)
# print(Task1.word_guessed)
# print(Task1.word_list)
# print(Task1.num_letters)
# print(Task1.list_of_guesses)
Hangman.ask_for_input()
