
import random

from pygame import mixer

song_file = "Swif7 - The Memory of You.mp3"

mixer.init()
mixer.music.load(song_file)
mixer.music.play(-1)


print("\nAditya Group Of Company presents\n")

print("                     Stone Paper Scissor (SPS)\n")

print("Rule:- If choices are                     Winner\n")
print("       stone and scissor                  stone")
print("       stone and paper                    paper")
print("       paper and scissor                 scissor\n")

print("Player having more number of wins will be the winner.\n")

name=input("Enter your name:-")
print("\n")

Win={'stone':'scissor','paper':'stone','scissor':'paper'}
List1=['stone','paper','scissor']

m=1
while m==1:

    loop=int(input("Enter the best of:-"))
    countp=countc=0

    for j in range(loop):
        user1=input('\nEnter your choice(stone,paper,scissor):-')
        user=user1.lower()
        comp=random.choice(List1)

        print("\ncomputer choice was",comp)
        for i in Win:
            if i==user and Win[i]==comp:
                countp+=1
                break

            elif i==comp and Win[i]==user:
                countc+=1
                break

            elif user==comp:
                print("\nchoices are same.")
                print("no points will be awarded for this.\n")
                break

    print("\nSummary of the game.")
    print(name,"score is",countp)
    print("Computer score is",countc)

    if countp>countc:
        print("\nCongratulation,You win the game.")

    elif countp<countc:
        print("\nBad luck,You lose the game.")

    else:
        print("\nMatch Tied.")

    def cont():
        
        print("\nDo you want to play once more.\n")
        global d
        d=int(input("Press 1 for Yes and 2 for No:-"))
        return d

    cont()
        
    e=1
    while e==1:
        
        if d==1:
            print("\nGood, That's the spirit.\n")
            m=1
            e=0
        
        elif d==2:
            print("\nAs your wish. Thank You")
            m=0
            e=0

        else:
            print("\nInvalid Choice!!!\n")
            cont()

rate=6
while rate>5:
    rate=int(input("\nRate the Game out of 5:-"))

    if rate>5:
        print("Out of range")
    else:
        print("Thanks SIR.")

mixer.music.stop()




        
    
