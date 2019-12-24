import random

scores = []


def game():
    number = random.randrange(1, 1001)
    guesses = 0
    asking = True
    while asking:
        ans = input("> ")
        if ans.isnumeric():
            ans = int(ans)
        else:
            print("Please enter a number")
            continue
        guesses += 1
        # To determine the message to be returned
        r = check(ans, number)
        if type(r) is str:
            print(r)
        else:
            global scores
            scores.append(guesses)
            if min(scores) == guesses:
                print("Correct! You guessed it in " + str(guesses) + " guesses, which is a new best score!")
            else:
                print("Correct! You guessed it in " + str(guesses) + " guesses. Your personal best is " + str(min(scores)) + ".")
            asking = False


def check(given, number):
    if given > 1000 or given < 1:
        return "OUT OF RANGE"
    elif given > number:
        return "high"
    elif given < number:
        return "low"
    elif given == number:
        return 1


def main():
    print("Number Guessing Game\n"
          "Enter a number between 1 and 1000 and we will tell you if you are high or low. "
          "Try to use the least amount of guesses.")
    playing = True
    while playing:
        game()
        prompt = input("Play again? (yes/no) ")
        if prompt == "yes":
            print("Enter a number")
            continue
        else:
            global scores
            print("Thanks for playing! Your best score was " + str(min(scores)) + " guesses!")
            break


if __name__ == '__main__':
    main()
