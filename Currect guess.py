import random
randnumber = random.randint(1,100)
usersguess=None
guesses=0

while(usersguess!=randnumber):
    usersguess =int(input("enter your guess: "))
    guesses+=1
    if (usersguess==randnumber):
        print("your guess is correct")
    else:
        if(usersguess>randnumber):
            print("your guess is incorrect please enter a smaller number :")
        else:
            print("your guess is incorrect please enter a larger number :")

print(f"you guessed the number in {guesses} guesses")

with open("score.txt","r") as f:
    score=int(f.read())

if(guesses<score):
    print("you have just broken the highscore")
    with open("highscore1.txt","w") as f:
        f.write(str(guesses))