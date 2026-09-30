# Asks user for their favorite color

colors = ["Red", "Blue", "Green", "Yellow", "Pink"]
answer = input("What is your favourite color? ")

if answer in colors:
    print("You color is at index", colors.index(answer), "in my list")
else:
    print("Sorry, I could not find your color")