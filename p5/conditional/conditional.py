
# control flow sederhana pake if elif else

my_input = input("Type something: ")

if len(my_input) < 5:
    print("Your input is less than 5 characters long.")
elif len(my_input) > 5:
    print("Your input is greater than 5 characters long.")
else:
    print("Your input is 5 characters long.")


# guessing number pake conditional

print("I'm thinking of a number between 1 and 10. Guess which one.")
my_guess = input("Type in your guess: ")

if my_guess == "3":
    print("You win!")
else:
    print("You lose.")
