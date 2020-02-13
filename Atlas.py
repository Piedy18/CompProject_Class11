#Atlas
import time
from datetime import datetime
with open ("Cities.txt","r") as f:
    x=((f.read()).lower()).split()
a=input("Name a city in India").lower()
for i in range(500):
    b=a[::-1]
    if a in x and a[-1]==b[0]:
        print("You have 10 seconds to name a city in India that starts with ", a[-1])
        datetimeobj1=datetime.now()
        timeobj1=datetimeobj1.time()
        seconds_start=timeobj1.second
        time.sleep(1)
        for j in range(9):
            print(9-j, "seconds")
            time.sleep(1)
        print("Name a city in India that starts with ", a[-1])
        b=input().lower()
        datetimeobj2=datetime.now()
        timeobj2=datetimeobj2.time()
        seconds_finish=timeobj2.second
        if b in x and b[0]==a[-1]:
            if seconds_finish-seconds_start>15.0:
                print("Oops, you have run out of time!")
                print("You lost :(")
                break
            elif seconds_finish-seconds_start<15:
                a=b
                continue
        else:
            print("Oops, that's not a city in India")
            break
    else:
        print("Oops, that's not a city in India")
        break
