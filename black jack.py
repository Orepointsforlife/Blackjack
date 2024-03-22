import random
types=["diamonds","spades","clubs","heart"]
beginplayer=random.randint(2,11)
begincomputer=random.randint(1,11)
beginplayer2=random.randint(2,11)
begincomputer2=random.randint(1,11)
x=beginplayer+beginplayer2
y=begincomputer+begincomputer2
c= random.choice(types)
d= random.choice(types)
e= random.choice(types)
f= random.choice(types)

print("you start with (",beginplayer,"of",c,"and",beginplayer2,"of",e,")\n"
        "with a total of (",x,")\n"
        "dealer starts with (",begincomputer,"of",d,"and",begincomputer2,"of",f,")\n"
        "with a total of (",y,")")
if x > 22:
    print("busted, You lost")
if x == 21:
    print("you won")
if y == 21:
    print("you lost")
if y > 22:
    print("you won")

while True:
    while y<21:
        a = random.choice(types)
        b = random.choice(types)
        player = input("hit or stay")
        playerran = random.randint(1, 10)
        computer = random.randint(1, 10)
        if player == ("hit"):
            x = x+playerran
            print("you got dealt", playerran, "of", a, "\n"
                "your total cards are (", x, ")\n")
        if player == ("stay"):
            y= y+computer
            print("you got dealt",playerran,"of",a,"\n"
              "your total cards are (",x,")\n"
                "the dealer got dealt",computer,"of",b,"\n" 
                "dealers total cards(",y,")")
            break

    if x>22:
        print("busted, You lost")
    if x ==21:
        print("you won")
    if y == 21:
        print("you lost")
    if y>22:
        print("you won")
    if x!=21:
        if x>y:
            if x<21:
                print ("you won")
                break
if y!=21:
    if y>x:
        if y<21:
            print ("you lost")






