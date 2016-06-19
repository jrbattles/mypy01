def compMatch():
    print("You guessed {}.".format(userNum))
    if userNum == myNum:
        print("Wow!  You guessed correctly!!!")
    else:
        print("Nope.  You guessed incorrectly.  Please try again")
        compMatch()

import random
myNum = random.randint(1,10)
compMatch
