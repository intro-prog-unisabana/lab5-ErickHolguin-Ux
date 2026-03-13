from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

def play_game():
    seed = int(input("Enter a seed number:\n"))
    seed_secret_numbers(seed)

    secret = generate_secret_number()

    tries = 0
    guessed = False

    while not guessed:
        guess = int(input("What is your guess:\n"))
        tries += 1
        message, guessed = input_response(secret, guess)
        print(message)

    print(f"It took you {tries} tries!")

if __name__ == "__main__":
    play_game()
