# limit the number of guesses
# catch when someone submit a non-integer value
# print "too high" or "too low" messages for bad guesses
# let peaple play again


# generate a random number between 1 to 10
import random
secret_number = random.randint(1, 10)
# get a number guess from the player

def run_gmae():
    guesses = []
    guess=0
    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number between 1 to 10: "))
        except ValueError :
            print("{} isn't a number.".format(guess))
        else:
            # compare guess the secret number 
            # print hit/miss
            if guess==secret_number:
                print("you got it :D, my number was {}".format(secret_number))
                break
            elif guess < secret_number:
                print("My number is higher than {}".format(guess))
            elif guess > secret_number:
                print("My number is lower than {}".format(guess))
            else:
                print("that's not it :(")
        guesses.append(guess)
    else:
        print("you didn't win! my number was {}".format(secret_number))
    play_again = input("do you want to play again? [y/n]")
    if play_again.lower()=='y':
        run_gmae()
    else:
        print("Bye!")    
run_gmae()
# print('Hi, I am Alireza :D.')

