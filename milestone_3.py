while True:
    guess = input("enter a letter")
    if len(guess)==1 and guess.isalpha():
        print(guess)
    else: 
        print("Invalid letter. Please, enter a single alphabetical character.")
        break
