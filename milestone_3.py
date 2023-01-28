def check_guess(guess):
    guess= guess.lower()
    word = "apple"
    if guess in word: 
         print(f"Good guess! {guess} is in the word.")
    
    else:
         print (f"Sorry, {guess} is not in the word. Try again.") 
#check_guess("a")
def ask_for_input():
    while True:
     guess = input("enter a letter").strip()
     if len(guess)==1 and guess.isalpha():
         break
     
     else: 
        print("Invalid letter. Please, enter a single alphabetical character.")
        break

    check_guess(guess)
ask_for_input()

