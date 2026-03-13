#import numero_random
#if numero_random >

def input_response(secret_number, user_guess):
    if user_guess < secret_number:
        return ("Too low! Try a higher number.",False)
    elif user_guess > secret_number:
        return ("Too high! Try a lower number.", False)
    else:
        return ("Correct! You guessed the number!", True)