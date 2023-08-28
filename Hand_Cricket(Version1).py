# Hand Cricket
import random
import time

while True:
    # Toss
    t = int(input("Enter 0 or 1"))
    toss = random.randint(0,1)
    if t == toss:#like Head or Tail
        ch = "Player"
        print("You won the toss...")
    else:
        ch = "Computer"
        print("Opponent won the toss...")
    if ch == "Player":#like Choosing Bat or Bowl
        t = int(input("Enter 0(For Batting) or 1(For Bowling)"))
        if t == 0:
            o,p = "Bowl","Bat"
        else:
            p,o = "Bowl","Bat"
    else:
        toss = random.randint(0,1)
        if toss == 0:
            p,o = "Bowl","Bat"
        else:
            o,p = "Bowl","Bat"
    print("You -",p)
    print("Opponent -",o)
    print()
    time.sleep(2)

    # Match
    if p == "Bat" and o == "Bowl":
        run = 0
        while True: #Batting
            pno = int(input("Enter a number(1 to 10)"))
            ono = random.randint(1,10)
            print("Opponent Entered-",ono)
            if pno == ono:
                print("[OUT]")
                break
            run = run + pno
        print("Runs Scored:",run)
        crun = 0
        print()
        time.sleep(2)
        print("Now you are bowling")
        while True: #Bowling
            if crun < run:
                pno = int(input("Enter a number(1 to 10)"))
                ono = random.randint(1,10)
                print("Opponent Entered-",ono)
                if pno == ono:
                    print("[OUT]")
                    break
                crun = crun + ono
            else:
                break
        time.sleep(1)
        if crun < run:
            print("You Won the Match")
        else:
            print("Opponent Won the Match")

    if p == "Bowl" and o == "Bat":
        run = 0
        while True: #Bowling
            pno = int(input("Enter a number(1 to 10)"))
            ono = random.randint(1,10)
            print("Opponent Entered-",ono)
            if pno == ono:
                print("[OUT]")
                break
            run = run + ono
        print("Runs Scored:",run)
        crun = 0
        print()
        time.sleep(2)
        print("Now You are Batting...")
        while True: #Batting
            if crun < run:
                pno = int(input("Enter a number(1 to 10)"))
                ono = random.randint(1,10)
                print("Opponent Entered-",ono)
                if pno == ono:
                    print("[OUT]")
                    break
                crun = crun + pno
            else:
                break
        time.sleep(1)
        if crun < run:
            print("Opponent Won the Match")
        else:
            print("You Won the Match")

    time.sleep(2)        
    tp = input("Do you want to play again(Type 'Yes' or 'No')?").lower()
    if tp == "yes":
        print()
        continue
    elif tp == "no":
        break
    else:
        print("Type yes or no proberly next time...")
        break