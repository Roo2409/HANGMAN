import random
class hangman:
 def __init__(self,word_list,num_of_lives = 5):
    self.num_of_lives = int(5)
    print (num_of_lives)
    self.word = random.choice(word_list)
    word = self.word
    print(word)
    self.word_guessed = ['_', '_', '_', '_', '_']
    print
    word_guessed = "_"
    while True:
     guess = input("enter a letter")
     word_guessed += guess
     if guess == word:
      print( guess)
      break
    # guesses = '_'
    # guess = input("enter a letter")
    # guesses += guess
    # while True:
    #  if guess in word:
    #   print(guess, end=" ")
    #  else:
    #   num_of_lives -=1
    #   print("wrong letter")
    #   print("you have", + num_of_lives ,"attempts left")

#   self.word = random.choice(word_list) 
#   self.word_guessed = ['_', '_', '_', '_', '_']
#   self.num_letter = len(random.choice(word_list))
#   self.list_of_guesses = []
word_list = ['banana','mango','apple','berry','orange'] 
Task1 = hangman(word_list)
print(Task1)

#task2 = task1.num_of_lives

    # def word():
    #  word = "apple"
    #  return word
    # def word_guesses():
    #    word = "apple"
    #    guesses = '-'
    #    num_of_lives = 5
    #    while num_of_lives > 0:
    #       failed = 0
    #       for i in word:
    #          if i in guesses:
    #           print(i,end = " ")
    #          else:
    #           print('_')
    #           failed +=1
    #       if failed == 0:
    #           print("Right guess")
    #           break
    #       guess = input("enter a letter")
    #       guesses += guess
    #       if guess not in word:
    #        num_of_lives -= 1
    #        print("wrong letter")
    #        print("you have", + num_of_lives ,"attempts left")
    #       if num_of_lives ==0:
    #        print("Better luck next time")
    # def num_letter():
    #   word = "apple"
    #   return len(word)
        
    
        

#print(hangman.word_list)
# print(hangman.num_lives)
# print(hangman.word())
#print(hangman.word_guesses())
# print(hangman.num_letter())
