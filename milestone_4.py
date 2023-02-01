import random
class Hangman:
   def __init__(self,word_list,num_lives = 5):
      self.word_list = word_list
      self.num_lives = num_lives
      self.word =  random.choice(self.word_list)   
      self.word_guessed = ["_"]*len(self.word)
      self.num_letters = len(set(self.word))
      self.list_of_guesses = [ ]
   
   def check_guess(self,guess):
      self.guess = guess.lower()
      self.list_of_guesses.append(guess)
      if guess in self.word:
         print(f"Good guess! {guess} is in the word.")
         self.num_letters-=1  
         
         index = 0
         for letter in self.word:  #apple        
            if letter == guess:
            #Find index   
               self.word_guessed[ index ] = guess
            index += 1
         print (f"The word list is {self.word_guessed}")
      else:
         self.num_lives-=1
         print(f"sorry, {guess} is not in the word")
         print(f"you have {self.num_lives} lives left")
      self.list_of_guesses.append(guess)
               
   
               
            
            #print(enumerate(self.word_guessed))
          
   def ask_for_input(self):
      while True:
         guess = input("enter a letter")
         if len(guess)!= 1 and not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
         elif guess in self.list_of_guesses:
            print("You already tried that letter!")
         else:
         #lif ( len(guess)==1 ) and (guess not in list_of_guesses):
          self.check_guess(guess)
          break
          


word_list = ['banana','mango','apple','orange'] 
word_guessed = ['_']
list_of_guesses = []
t1 = Hangman(word_list)
# print(Task1.word_guessed)
# print(Task1.word_list)
# print(Task1.num_letters)
# print(Task1.list_of_guesses)
t1.ask_for_input()
#t1.check_guess("a")
      # for letter in range(len(self.word)):
      #       if self.word[letter] == guess:
      #          self.word_guessed[letter] = guess
      #          print(self.word_guessed)     