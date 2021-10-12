import random
ranNumber=random.randint(1,100)
guesses=0
userguess=None


while userguess!=ranNumber:
    userguess=int(input("Enter your your guess"))
    guesses+=1
    if userguess==ranNumber:
        print("You gussed it right:)")
    else:
        if userguess>ranNumber:
         print("You gussed it wrong!! guess a smaller number...") 
        else:
            print("You gussed it wrong!! guess a larger number...") 
        
print(f"You guessed the number in {guesses}")
with open("hiscore.txt","r") as f:
    highscore=int(f.read())

if guesses>highscore:
    print("you have just broken the high score\n")
    with open("hiscore.txt","w") as f:
     f.write(str(guesses))          


