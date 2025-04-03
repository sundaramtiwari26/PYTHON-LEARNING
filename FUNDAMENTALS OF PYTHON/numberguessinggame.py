import random
def number_game():
    print("Welcome to number guessing game!.")
    target=random.randint(1,100)
    attempts=0
    try:
        while True:
            user_guess=int(input("Guess the number 1 to 100..."))
            attempts+=1
            if user_guess==target:
                print(f"Congratulations you guessed it {target} in {attempts} attempts")
                break
            elif user_guess<target:
                print("guess high number,try again")
            else:
                print("too high,try again")

    except ValueError:
        print("Error: pls enter a valid number..")

number_game()