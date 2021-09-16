import sys
from random import randint

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f"Guess the number ({sys.argv[1]} to {sys.argv[2]}) "))
        print(f"Answer > - {answer}")
        if 0 < guess < 11:
            if guess == answer:
                print("Genius!!")
                break
        else:
            print("I said 1 - 10")
    except ValueError:
        print("Please enter a number (1-10)")
        continue
