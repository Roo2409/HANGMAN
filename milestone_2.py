import random
word_list = ['banana','mango','apple','berry','orange']
word = random.choice(word_list)
print(word)



word_list = ['banana','mango','apple','berry','orange']
print(word_list)

guess = input("enter a single letter")
for letter in guess:
    if len(guess)==1 and guess.isalpha():
       print("good guess")
    else:
       print("Oops! That is not a valid input.")