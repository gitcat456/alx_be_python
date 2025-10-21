import random

def play_game():
    secret_number = random.randint(1, 10)
    guesses = 0  # counter

    while True:
        guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
        guesses += 1

        match guess:
            case x if x == secret_number:
                print(f"Congratulations, you guessed it in {guesses} tries!")
                break
            case x if x > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case x if x < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye")
        break
