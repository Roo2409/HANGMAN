# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. Therefore we created a file called milestone_2.py and  we will be implementing all the asked tasks in there. 

-Milestone2= 
we have to create a list of 5 fruits and assigned it to the "word_list" Variable.

-Milestone3=
In addition to Task 1, we will be using random.choice method to get the random choices from our list. Firstly import random and then assigned the word_list to the "word" Variable. Print out the possible outcome several times by using random.choicemethod.
``` python 
word_list = ['banana','mango','apple','berry','orange']
print(word_list)

import random
word_list = ['banana','mango','apple','berry','orange']
word = random.choice(word_list)
print(word)
```
-Milestone4 = The code has two functions: check_guess and ask_for_input check-guess function takes the guessed letter convert to lower case and check if the guessed letter is in the word. Then accordingly it prints the message for the user. ask_for_input function request for input from user check for two conditions: if input is string value and more than one character. check_for_guess function is called in ask_for_input function first that if the letter is in the word.

-Milestone5 = The game hangman is asking input from users to guess the letters from the list of words. The system picks a random word from list and ask input from user. The input provided is checked against the index of the word and and store the input if guessed correctly. In total user is given 5 lives and for any wrong guess the user looses a life from the game. After 5 guesses, the user lose the game. This game helped to learn very basics of the python like creating functions and class.
