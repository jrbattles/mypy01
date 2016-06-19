def compMatch():
    print("You guessed {}.".format(int(userNum)))
    #print("myNum = {}.".format(int(myNum)))
    if userNum == myNum:
        print("Wow!  You guessed correctly!!!")
    else:
        print("Nope.  You guessed incorrectly.  Please try again")
        
import random
myNum = random.randint(1,10)
# print(myNum)
userNum = input("Guess a Number between 1 and 10: ")
userNum = int(userNum)
# print("userNum = {}.".format(int(userNum)))
compMatch()
