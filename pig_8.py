import random
def pig(socress):
    sums=0
    nwscore=0
    check=1
    while(sums< 100 and nwscore<100 and check==1):
        die=random.randint(1,6)
        if(sums==0):
            if(die==1):
                print("Roll:",die)
                sums=0
                break
            sums+=die
            print("Roll:",die)
            print("Turn total:",sums)
        else:
            chek=input("Roll/hold")
            if(chek==""):
                if(die==1):
                    print("Roll:",die)
                    sums=0
                    break
                sums+=die
                if(socress+sums<=100):
                    print("Roll:",die)
                    print("Turn total:",sums)
                else:
                    print("Roll:",die)
                    nwscore+=sums
                    break
            else:
                nwscore+=sums
                check=0
                break
    print("Turn total:",sums)
    print("New score:",nwscore)
    return nwscore
def pigs(scoress):
    sums=0
    nwscore=0
    while(sums<20 and nwscore<100):
        die=random.randint(1,6)
        if(die==1):
            print("Roll:",die)
            sums=0
            break
        else:
            sums+=die
        print("Roll:",die)
        if(scoress+sums>=100):
            break
    nwscore+=sums
    print("Turn total:",sums)
    print("New score:",nwscore)
    return nwscore
plselct=random.randint(1,2)
if(plselct==1):
    print("You will be Player",plselct)
    print("Enter nothing to roll; enter anything to hold")
else:
    print("You will be Player",plselct)
    print("Enter nothing to roll; enter anything to hold")
pl1score=0
pl2score=0
count=0
score=0
while (score<100):
    if(count==0):
        print("Player 1 score: ",pl1score)
        print("Player 2 score: ",pl2score)
        print("It is player 1 turn")
        if(plselct==1):
            pl1score+=pig(pl1score)
        else:
            pl1score+=pigs(pl1score)
        count=1
        if(pl1score<100):
            print("It is player 2 turn")
        else:
            break
    else:
        print("Player 1 score: ",pl1score)
        print("Player 2 score: ",pl2score)
        if(plselct==2):
            pl2score+=pig(pl2score)
        else:
            pl2score+=pigs(pl2score)
        count=0
        if(pl2score<100):
            print("It is player 1 turn")
        else:
            break
    if(pl2score>pl1score):
        score=pl2score
    else:
        score=pl1score
if(pl1score>pl2score):
    print("Player 1 wins")
else:
    print("Player 2 wins")
