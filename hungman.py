def stickman():
    if l==4:
        print(" O")
    elif l==3:
        print(" O\n |")
    elif l==2:
        print(" O\n\|/")
    elif l==1:
        print(" O\n\|/\n L \n/|\\")
    elif l==0:
        print("DEAD")
w=input("Enter word: ").lower()
for i in range(150):
    print()
s=[]
for i in range(len(w)):
    if w[i]!=' ':
        s=s+["_"]
    if w[i]==' ':
        s=s+[" "]
l=5
while True:
    for i in range(len(w)):
        print(s[i], end=" ")
    c=input("\n\n Enter character")
    x=y=True
    for i in range(len(w)):
        if w[i]==c:
            if x:
                print("Correct letter")
            s[i]=c
            x=False
            y=False
    if y:
        print("\n Letter",c,"isn't there. Try again.")
        l-=1
        print("Lives left: ",l)
        stickman()
    x=True
    for i in range(len(w)):
        if s[i]=="_":
            x=False
    if x:
        for i in range(len(w)):
            print(s[i],end=" ")
        print("You won!")
        break
    if l==0:
        print("You lost :(")
        print("Word was",w)
        break
