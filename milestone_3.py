word = "apple"
while True:
    guess = input("enter a letter").strip()
    if len(guess)==1 and guess.isalpha():

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print (f"Sorry, {guess} is not in the word. Try again.")
            
    else: 
        print("Invalid letter. Please, enter a single alphabetical character.")
        break

    