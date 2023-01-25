# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. Therefore we created a file called milestone_2.py and  we will be implementing all the asked tasks in there. 

-Task1 = 
we have to create a list of 5 fruits and assigned it to the "word_list" Variable.

-Task2=
In addition to Task 1, we will be using random.choice method to get the random choices from our list. Firstly import random and then assigned the word_list to the "word" Variable. Print out the possible outcome several times by using random.choicemethod.
``` python 
word_list = ['banana','mango','apple','berry','orange']
print(word_list)

import random
word_list = ['banana','mango','apple','berry','orange']
word = random.choice(word_list)
print(word)
```
-Task3 = In this task we will be using Input method in which we will ask the user to Enter the single letter, and assign it to the "guess"Variable.

-Task4 = In addition to task 3 we will use If and Else statement. where we will reassure that, The length of the input is ==1 and it is an Alphabet.
````python
guess = input("enter a single letter")
for letter in guess:
    if len(guess)==1 and guess.isalpha():
        print("good guess")
    else:
        print("Oops! That is not a valid input.")
````
em Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.