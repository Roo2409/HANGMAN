guess = input("enter a letter")
x = guess.isalpha()
while x == guess.isalpha():
    if len(guess)==1:
        break
    else: 
        print("Invalid letter. Please, enter a single alphabetical character.")
