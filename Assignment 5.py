import random
def intro():
    print("Welcome to Stone|Paper|Scissor")
    print("Enter 0 to select Stone")
    print("Enter 1 to select Paper")
    print("Enter 2 to select Scissor")
    
sc=0
su=0
r=5
intro()
choice=True
while(choice and r>0):
    lis=["Stone","Paper","Scissor"]
    value=random.randint(0,2)
    try:
        i1=int(input("Enter a number: "))
        try:
            print("You choose " +lis[i1])
            print("I choose " +lis[value])
        except:
            print("Error!! Please enter a valid number")
        else:
            if value<i1:
                if value==0:
                    if i1==1:
                        print("Ugghh!! I lost this round")
                        su=su+1
                    else:
                        print("Yes!! I won this round")
                        sc=sc+1
                else:
                    print("Ugghh!! I lost this round")
                    su=su+1
            elif value!=i1:
                if value==2:
                    if i1==1:
                        print("Yes!! I won this round")
                        sc=sc+1
                    else:
                        print("Ugghh!! I lost this round")
                        su=su+1
                else:
                    print("Yes!! I won this round")
                    sc=sc+1
            else:
                print("It is a draw")
            print("---Score----\nUser: ", +su)
            print("Computer: ",sc)
            r=r-1
            if r==0:
                if sc>su:
                    print("I won the match. Better luck next time!")
                elif sc<su:
                    print("You won the match. I will see you next time")
                else:
                    print("It is a draw")
                c=input("Do you want to play one more game?(y/n): ")
                if c=="n":
                    choice=False
                else:
                    r=5
                    sc=0
                    su=0
                    intro()
                    continue
    except:
        print("Error!! Please enter a valid number")

        
