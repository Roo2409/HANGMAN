#fahrenheit = int(input("what is the temperature today in fahrenheit"))

#celsius = (round( fahrenheit-32)*5/9)
#print(round(celsius, 1) , "is the temperature in celsuis")

guess = input("enter a single letter")
for letter in guess:
    if len(guess)==1 and guess.isalpha():
        print("good guess")
    else:
        print("Oops! That is not a valid input.")

    
